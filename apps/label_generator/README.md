# Label Generator

This is a program that made for generate QR code and getting mac address for given microcontroller.

## Features

- Flashing firmware
- Read Mac Address
- Send data to database

## Getting Started

### Prerequisites

1. [JLINK](https://www.segger.com/downloads/jlink/)

2. [NRFJPROG](https://www.nordicsemi.com/Products/Development-tools/nrf-command-line-tools)

### Installation

1. firstly, add jlink directory to path variable.

   1.1. In Search, search for and then select: System (Control Panel)

   1.2 Then search for `Edit environment variables for your account`

   1.3 In user variable section (at the top). Click path then edit.

![Alt text](img/image.png)

    1.4 Click new and add you jlink directory
    (mine is `C:\Program Files (x86)\SEGGER\JLink`)

![Alt text](img/image_1.png)

2. running .exe file and enjoy!

### Note

- to add more firmware you need to put it at `program_files` folder
- all database contain in `database` directory
