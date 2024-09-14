from pyfirmata2 import Arduino
import time

board = Arduino('COM3')  # Check your port number
time.sleep(2)  # Delay to allow the connection to stabilize
analog_pin = board.get_pin('d:11:p')  # Reading from an analog pin (A0)
#analog_pin.enable_reporting()

while True:
    board.digital[13].write(1)
    time.sleep(0.050)
    board.digital[13].write(0)
    time.sleep(0.050)
    reading = analog_pin.read()
    print("Pin Value:", reading)
    time.sleep(1)

while True:
    reading = analog_pin.read()
    print("Pin Value:", reading)
    time.sleep(1)
