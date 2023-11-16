import os
import threading
from . import jlink
from . import log
from .utils import *
from PyQt5.QtWidgets import QFileDialog

mac_id_list = []
header = ['macId', 'note']

IS_MOCK = 0
mock_cnt = 1

current_program_path = ''


def power_on_event():
    jlink.power_on()


def power_off_event():
    jlink.power_off()


def flash_event(ui):
    thr = threading.Thread(target=flashing_thread_callback, args=[ui])
    thr.start()
    ui.flashStatusLabel.setText(
        "Flash Status : <span style=\"color:yellow\">In Progress</span></p>")


def flashing_thread_callback(ui):
    jlink.power_on()
    if ui.programFileComboBox.currentText() == '':
        ui.flashStatusLabel.setText(
            "Flash Status : <span style=\"color:red\">Can located the program file</span></p>")
        return
    file_path = os.path.join(
        current_program_path, ui.programFileComboBox.currentText())
    result = jlink.flash_program(file_path)
    if result:
        ui.flashStatusLabel.setText(
            "Flash Status : <span style=\"color:green\">Success</span></p>")
    else:
        ui.flashStatusLabel.setText(
            "Flash Status : <span style=\"color:red\">Fail</span></p>")


def program_combobox_click_event(ui, directory):
    global current_program_path

    # Clear the current items in the combobox
    currentText = ui.programFileComboBox.currentText()
    ui.programFileComboBox.clear()

    # Check if the folder exists
    if os.path.exists(directory) and os.path.isdir(directory):
        # Get a list of file names in the folder
        file_names = os.listdir(directory)

        # Filter out only the files (not directories) and add them to the combobox
        for file_name in file_names:
            file_path = os.path.join(directory, file_name)
            if os.path.isfile(file_path) and (file_name.endswith('.hex') or file_name.endswith('.bin')):
                ui.programFileComboBox.addItem(file_name)
                ui.programFileComboBox.setCurrentText(currentText)

    current_program_path = directory


def add_good_device_event(ui):
    global mac_id_list
    global header

    if IS_MOCK:
        global mock_cnt
        mac_id = f'dev_{mock_cnt}'
        mock_cnt += 1
    else:
        jlink.power_on()
        mac_id = jlink.mac_id_check()
    if not mac_id:
        ui.addDeviceStatusLabel.setText(
            "<span style=\"color:red\">Can't read MAC address</span></p>")
        return

    is_mac_id_duplicated = check_value_in_lists(mac_id_list, mac_id)

    if is_mac_id_duplicated:
        ui.addDeviceStatusLabel.setText(
            "<span style=\"color:red\">MAC address is duplicated</span></p>")
        return
    else:
        ui.addDeviceStatusLabel.setText(
            "<span style=\"color:green\">Okay</span></p>")

    note = ui.noteLineEdit.text()
    timestamp = get_date_time()
    data = (mac_id, '0', timestamp, note)

    res = log.insert_child_device(data)

    if res:
        log_directory = os.path.join(
            os.path.dirname(os.path.realpath(__file__)), "log/devicesLog.csv")
        mac_id_list.append([mac_id, note])
        log.log_mac_id(mac_id, note, log_directory)
    else:
        ui.addDeviceStatusLabel.setText(
            "<span style=\"color:red\">Data Already in DB</span></p>")

    populate_table_view(ui.devicesTableView, header, mac_id_list)
    if len(mac_id_list) == 3:
        print_now_event(ui)


def add_bad_device_event(ui):
    global mac_id_list
    global header

    note = ui.noteLineEdit.text()
    if note == '':
        note = 'Faulty'
    mac_id_list.append(['Faulty', note])

    populate_table_view(ui.devicesTableView, header, mac_id_list)
    if len(mac_id_list) == 3:
        print_now_event(ui)


def print_now_event(ui):
    global mac_id_list
    log_directory = os.path.join(
        os.path.dirname(os.path.realpath(__file__)), "log/devicesLog.csv")
    log.write_csv(['macID', 'note'], mac_id_list, log_directory)
    for device in mac_id_list:
        if 'Faulty' not in device:
            log.update_print_label_by_mac_id(device[0])  # device 0 equal macId
    clear_list_event(ui)


def clear_list_event(ui):
    global mac_id_list
    mac_id_list = []

    populate_table_view(ui.devicesTableView, header, mac_id_list)


def show_directory_dialog(ui, parent):
    options = QFileDialog.Options()
    options |= QFileDialog.DontUseNativeDialog
    directory_dialog = QFileDialog()
    directory_dialog.setOptions(options)

    directory_dialog.setFileMode(QFileDialog.Directory)

    selected_directory = directory_dialog.getExistingDirectory(
        parent, "Select Directory")

    program_combobox_click_event(ui, selected_directory)
