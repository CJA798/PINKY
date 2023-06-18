# UART Control
#
# This example shows how to use the serial port on your OpenMV Cam.

import time
from pyb import UART

# Init UART object.
uart = UART('LP1', 19200)

while(True):
    uart.write("From Nicla\r\n")
    msg = uart.readline()
    print(msg)
    time.sleep_ms(1000)
