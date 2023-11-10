# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(580, 764)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName("tabWidget")
        self.kittingTab = QtWidgets.QWidget()
        self.kittingTab.setObjectName("kittingTab")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.kittingTab)
        self.verticalLayout.setObjectName("verticalLayout")
        self.groupBox = QtWidgets.QGroupBox(self.kittingTab)
        self.groupBox.setStyleSheet("font-family: Arial, Helvetica, sans-serif;\n"
"font-size: 12pt;")
        self.groupBox.setObjectName("groupBox")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.groupBox)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.edgeLabel = QtWidgets.QLabel(self.groupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.edgeLabel.sizePolicy().hasHeightForWidth())
        self.edgeLabel.setSizePolicy(sizePolicy)
        self.edgeLabel.setMinimumSize(QtCore.QSize(300, 0))
        self.edgeLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.edgeLabel.setObjectName("edgeLabel")
        self.verticalLayout_2.addWidget(self.edgeLabel)
        self.gridLayout_2 = QtWidgets.QGridLayout()
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.edgeSearchButton = QtWidgets.QPushButton(self.groupBox)
        self.edgeSearchButton.setStyleSheet("QPushButton {\n"
"                background-color: #3498db;\n"
"                color: #ffffff;\n"
"                border: 2px solid #3498db;\n"
"                border-radius: 5px;\n"
"                padding: 0px 10px;\n"
"            }\n"
"            \n"
"            QPushButton:hover {\n"
"                background-color: #2980b9;\n"
"                border: 2px solid #2980b9;\n"
"            }\n"
"            \n"
"            QPushButton:pressed {\n"
"                background-color: #1f618d;\n"
"                border: 2px solid #1f618d;\n"
"            }")
        self.edgeSearchButton.setObjectName("edgeSearchButton")
        self.gridLayout_2.addWidget(self.edgeSearchButton, 0, 1, 1, 1)
        self.edgeSearchLineEdit = QtWidgets.QLineEdit(self.groupBox)
        self.edgeSearchLineEdit.setText("")
        self.edgeSearchLineEdit.setObjectName("edgeSearchLineEdit")
        self.gridLayout_2.addWidget(self.edgeSearchLineEdit, 0, 0, 1, 1)
        self.edgeNoteLabel = QtWidgets.QLabel(self.groupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.edgeNoteLabel.sizePolicy().hasHeightForWidth())
        self.edgeNoteLabel.setSizePolicy(sizePolicy)
        self.edgeNoteLabel.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.edgeNoteLabel.setWordWrap(True)
        self.edgeNoteLabel.setObjectName("edgeNoteLabel")
        self.gridLayout_2.addWidget(self.edgeNoteLabel, 2, 0, 1, 2)
        self.edgeComboBox = QtWidgets.QComboBox(self.groupBox)
        self.edgeComboBox.setObjectName("edgeComboBox")
        self.gridLayout_2.addWidget(self.edgeComboBox, 1, 0, 1, 2)
        self.verticalLayout_2.addLayout(self.gridLayout_2)
        self.noteTextBrowser = QtWidgets.QTextBrowser(self.groupBox)
        self.noteTextBrowser.setMaximumSize(QtCore.QSize(16777215, 100))
        self.noteTextBrowser.setObjectName("noteTextBrowser")
        self.verticalLayout_2.addWidget(self.noteTextBrowser)
        self.line = QtWidgets.QFrame(self.groupBox)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.verticalLayout_2.addWidget(self.line)
        self.childLabel = QtWidgets.QLabel(self.groupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.childLabel.sizePolicy().hasHeightForWidth())
        self.childLabel.setSizePolicy(sizePolicy)
        self.childLabel.setObjectName("childLabel")
        self.verticalLayout_2.addWidget(self.childLabel, 0, QtCore.Qt.AlignHCenter)
        self.gridLayout_3 = QtWidgets.QGridLayout()
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.childSearchLineEdit = QtWidgets.QLineEdit(self.groupBox)
        self.childSearchLineEdit.setObjectName("childSearchLineEdit")
        self.gridLayout_3.addWidget(self.childSearchLineEdit, 0, 0, 1, 1)
        self.childComboBox = QtWidgets.QComboBox(self.groupBox)
        self.childComboBox.setObjectName("childComboBox")
        self.gridLayout_3.addWidget(self.childComboBox, 1, 0, 1, 3)
        self.childSearchButton = QtWidgets.QPushButton(self.groupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.childSearchButton.sizePolicy().hasHeightForWidth())
        self.childSearchButton.setSizePolicy(sizePolicy)
        self.childSearchButton.setStyleSheet("QPushButton {\n"
"                background-color: #3498db;\n"
"                color: #ffffff;\n"
"                border: 2px solid #3498db;\n"
"                border-radius: 5px;\n"
"                padding: 0px 10px;\n"
"            }\n"
"            \n"
"            QPushButton:hover {\n"
"                background-color: #2980b9;\n"
"                border: 2px solid #2980b9;\n"
"            }\n"
"            \n"
"            QPushButton:pressed {\n"
"                background-color: #1f618d;\n"
"                border: 2px solid #1f618d;\n"
"            }")
        self.childSearchButton.setObjectName("childSearchButton")
        self.gridLayout_3.addWidget(self.childSearchButton, 0, 1, 1, 1)
        self.verticalLayout_2.addLayout(self.gridLayout_3)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.bomLabel = QtWidgets.QLabel(self.groupBox)
        self.bomLabel.setObjectName("bomLabel")
        self.verticalLayout_3.addWidget(self.bomLabel)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.bomComboBox = QtWidgets.QComboBox(self.groupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.bomComboBox.sizePolicy().hasHeightForWidth())
        self.bomComboBox.setSizePolicy(sizePolicy)
        self.bomComboBox.setObjectName("bomComboBox")
        self.horizontalLayout_6.addWidget(self.bomComboBox)
        self.bomRefreshButton = QtWidgets.QPushButton(self.groupBox)
        self.bomRefreshButton.setStyleSheet("QPushButton {\n"
"                background-color: #3498db;\n"
"                color: #ffffff;\n"
"                border: 2px solid #3498db;\n"
"                border-radius: 5px;\n"
"                padding: 0px 10px;\n"
"            }\n"
"            \n"
"            QPushButton:hover {\n"
"                background-color: #2980b9;\n"
"                border: 2px solid #2980b9;\n"
"            }\n"
"            \n"
"            QPushButton:pressed {\n"
"                background-color: #1f618d;\n"
"                border: 2px solid #1f618d;\n"
"            }")
        self.bomRefreshButton.setObjectName("bomRefreshButton")
        self.horizontalLayout_6.addWidget(self.bomRefreshButton)
        self.verticalLayout_3.addLayout(self.horizontalLayout_6)
        self.label = QtWidgets.QLabel(self.groupBox)
        self.label.setObjectName("label")
        self.verticalLayout_3.addWidget(self.label)
        self.groupListTableView = QtWidgets.QTableView(self.groupBox)
        self.groupListTableView.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustIgnored)
        self.groupListTableView.setSelectionMode(QtWidgets.QAbstractItemView.MultiSelection)
        self.groupListTableView.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.groupListTableView.setObjectName("groupListTableView")
        self.groupListTableView.horizontalHeader().setCascadingSectionResizes(True)
        self.groupListTableView.horizontalHeader().setStretchLastSection(False)
        self.verticalLayout_3.addWidget(self.groupListTableView)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.fixedStatusLabel = QtWidgets.QLabel(self.groupBox)
        self.fixedStatusLabel.setObjectName("fixedStatusLabel")
        self.horizontalLayout_2.addWidget(self.fixedStatusLabel)
        self.addStatusLabel = QtWidgets.QLabel(self.groupBox)
        self.addStatusLabel.setText("")
        self.addStatusLabel.setObjectName("addStatusLabel")
        self.horizontalLayout_2.addWidget(self.addStatusLabel)
        self.verticalLayout_3.addLayout(self.horizontalLayout_2)
        self.verticalLayout_2.addLayout(self.verticalLayout_3)
        self.addGroupButton = QtWidgets.QPushButton(self.groupBox)
        self.addGroupButton.setStyleSheet("QPushButton {\n"
"                background-color: #3498db;\n"
"                color: #ffffff;\n"
"                border: 2px solid #3498db;\n"
"                border-radius: 5px;\n"
"                padding: 0px 10px;\n"
"            }\n"
"            \n"
"            QPushButton:hover {\n"
"                background-color: #2980b9;\n"
"                border: 2px solid #2980b9;\n"
"            }\n"
"            \n"
"            QPushButton:pressed {\n"
"                background-color: #1f618d;\n"
"                border: 2px solid #1f618d;\n"
"            }")
        self.addGroupButton.setObjectName("addGroupButton")
        self.verticalLayout_2.addWidget(self.addGroupButton)
        self.horizontalLayout_5.addLayout(self.verticalLayout_2)
        self.horizontalLayout_3.addLayout(self.horizontalLayout_5)
        self.verticalLayout.addWidget(self.groupBox)
        self.tabWidget.addTab(self.kittingTab, "")
        self.bomTab = QtWidgets.QWidget()
        self.bomTab.setStyleSheet("font-family: Arial, Helvetica, sans-serif;\n"
"font-size: 12pt;")
        self.bomTab.setObjectName("bomTab")
        self.horizontalLayout_11 = QtWidgets.QHBoxLayout(self.bomTab)
        self.horizontalLayout_11.setObjectName("horizontalLayout_11")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout()
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.verticalLayout_7.addLayout(self.horizontalLayout_9)
        self.macPrefixLebel = QtWidgets.QLabel(self.bomTab)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.macPrefixLebel.sizePolicy().hasHeightForWidth())
        self.macPrefixLebel.setSizePolicy(sizePolicy)
        self.macPrefixLebel.setObjectName("macPrefixLebel")
        self.verticalLayout_7.addWidget(self.macPrefixLebel)
        self.macPrefixLineEdit = QtWidgets.QLineEdit(self.bomTab)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.macPrefixLineEdit.sizePolicy().hasHeightForWidth())
        self.macPrefixLineEdit.setSizePolicy(sizePolicy)
        self.macPrefixLineEdit.setObjectName("macPrefixLineEdit")
        self.verticalLayout_7.addWidget(self.macPrefixLineEdit)
        self.DeviceTypeLabel = QtWidgets.QLabel(self.bomTab)
        self.DeviceTypeLabel.setObjectName("DeviceTypeLabel")
        self.verticalLayout_7.addWidget(self.DeviceTypeLabel)
        self.deviceTypeComboBox = QtWidgets.QComboBox(self.bomTab)
        self.deviceTypeComboBox.setObjectName("deviceTypeComboBox")
        self.verticalLayout_7.addWidget(self.deviceTypeComboBox)
        self.controllerTypeLabel = QtWidgets.QLabel(self.bomTab)
        self.controllerTypeLabel.setObjectName("controllerTypeLabel")
        self.verticalLayout_7.addWidget(self.controllerTypeLabel)
        self.controllerTypeComboBox = QtWidgets.QComboBox(self.bomTab)
        self.controllerTypeComboBox.setObjectName("controllerTypeComboBox")
        self.verticalLayout_7.addWidget(self.controllerTypeComboBox)
        self.locationLabel = QtWidgets.QLabel(self.bomTab)
        self.locationLabel.setObjectName("locationLabel")
        self.verticalLayout_7.addWidget(self.locationLabel)
        self.locationComboBox = QtWidgets.QComboBox(self.bomTab)
        self.locationComboBox.setObjectName("locationComboBox")
        self.verticalLayout_7.addWidget(self.locationComboBox)
        self.label_2 = QtWidgets.QLabel(self.bomTab)
        self.label_2.setObjectName("label_2")
        self.verticalLayout_7.addWidget(self.label_2)
        self.roomLineEdit = QtWidgets.QLineEdit(self.bomTab)
        self.roomLineEdit.setObjectName("roomLineEdit")
        self.verticalLayout_7.addWidget(self.roomLineEdit)
        spacerItem = QtWidgets.QSpacerItem(20, 25, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Maximum)
        self.verticalLayout_7.addItem(spacerItem)
        self.addProfileButton = QtWidgets.QPushButton(self.bomTab)
        self.addProfileButton.setObjectName("addProfileButton")
        self.verticalLayout_7.addWidget(self.addProfileButton)
        self.line_4 = QtWidgets.QFrame(self.bomTab)
        self.line_4.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_4.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_4.setObjectName("line_4")
        self.verticalLayout_7.addWidget(self.line_4)
        self.label_3 = QtWidgets.QLabel(self.bomTab)
        self.label_3.setObjectName("label_3")
        self.verticalLayout_7.addWidget(self.label_3)
        self.bomNameLineEdit = QtWidgets.QLineEdit(self.bomTab)
        self.bomNameLineEdit.setObjectName("bomNameLineEdit")
        self.verticalLayout_7.addWidget(self.bomNameLineEdit)
        self.bomTableView = QtWidgets.QTableView(self.bomTab)
        self.bomTableView.setSelectionMode(QtWidgets.QAbstractItemView.MultiSelection)
        self.bomTableView.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.bomTableView.setObjectName("bomTableView")
        self.verticalLayout_7.addWidget(self.bomTableView)
        self.addBomButton = QtWidgets.QPushButton(self.bomTab)
        self.addBomButton.setObjectName("addBomButton")
        self.verticalLayout_7.addWidget(self.addBomButton)
        self.horizontalLayout_10 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")
        self.deleteRowButton = QtWidgets.QPushButton(self.bomTab)
        self.deleteRowButton.setObjectName("deleteRowButton")
        self.horizontalLayout_10.addWidget(self.deleteRowButton)
        self.clearBomButton = QtWidgets.QPushButton(self.bomTab)
        self.clearBomButton.setObjectName("clearBomButton")
        self.horizontalLayout_10.addWidget(self.clearBomButton)
        self.verticalLayout_7.addLayout(self.horizontalLayout_10)
        self.horizontalLayout_11.addLayout(self.verticalLayout_7)
        self.tabWidget.addTab(self.bomTab, "")
        self.horizontalLayout.addWidget(self.tabWidget)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.groupBox.setTitle(_translate("MainWindow", "Console"))
        self.edgeLabel.setText(_translate("MainWindow", "Edge Mac Address"))
        self.edgeSearchButton.setText(_translate("MainWindow", "Search"))
        self.edgeSearchLineEdit.setPlaceholderText(_translate("MainWindow", "keyword"))
        self.edgeNoteLabel.setText(_translate("MainWindow", "Notes :"))
        self.childLabel.setText(_translate("MainWindow", "Child Mac Address"))
        self.childSearchLineEdit.setPlaceholderText(_translate("MainWindow", "keyword"))
        self.childSearchButton.setText(_translate("MainWindow", "Search"))
        self.bomLabel.setText(_translate("MainWindow", "BOM"))
        self.bomRefreshButton.setText(_translate("MainWindow", "Refresh"))
        self.label.setText(_translate("MainWindow", "Configuration List"))
        self.fixedStatusLabel.setText(_translate("MainWindow", "Status :"))
        self.addGroupButton.setText(_translate("MainWindow", "Add Group"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.kittingTab), _translate("MainWindow", "Kitting Tool"))
        self.macPrefixLebel.setText(_translate("MainWindow", "Mac Address Prefix"))
        self.macPrefixLineEdit.setPlaceholderText(_translate("MainWindow", "xx_xx"))
        self.DeviceTypeLabel.setText(_translate("MainWindow", "Device Type"))
        self.controllerTypeLabel.setText(_translate("MainWindow", "Controller Type"))
        self.locationLabel.setText(_translate("MainWindow", "Location"))
        self.label_2.setText(_translate("MainWindow", "Room"))
        self.addProfileButton.setText(_translate("MainWindow", "Add Profile"))
        self.label_3.setText(_translate("MainWindow", "BOM Name"))
        self.addBomButton.setText(_translate("MainWindow", "Add Group"))
        self.deleteRowButton.setText(_translate("MainWindow", "Delete Selected Row"))
        self.clearBomButton.setText(_translate("MainWindow", "Clear Group"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.bomTab), _translate("MainWindow", "BOM Setting"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
