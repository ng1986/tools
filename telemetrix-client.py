#!/usr/local/bin/python3

import sys
import time

from telemetrix import telemetrix


DIGITAL_PIN = 7

board = telemetrix.Telemetrix()

# Set the DIGITAL_PIN as an output pin
board.set_pin_mode_digital_output(DIGITAL_PIN)

# Blink the LED and provide feedback as
# to the LED state on the console.
for blink in range(5):
    # When hitting control-c to end the program
    # in this loop, we are likely to get a KeyboardInterrupt
    # exception. Catch the exception and exit gracefully.
    try:
        print('1')
        board.digital_write(DIGITAL_PIN, 1)
        time.sleep(1)
        print('0')
        board.digital_write(DIGITAL_PIN, 0)
        time.sleep(1)
    except KeyboardInterrupt:
        board.shutdown()
        sys.exit(0)
