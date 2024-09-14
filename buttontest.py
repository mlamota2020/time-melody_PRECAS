from pyfirmata2 import Arduino, util
import time

board = Arduino('COM3')  # Check your port number
time.sleep(2)  # Delay to allow the connection to stabilize
it = util.Iterator(board)
it.start()

analog_pin = board.get_pin('a:0:i')  # Reading from an analog pin (A0)
analog_pin.enable_reporting()

while True:
    reading = analog_pin.read()
    print("Analog Pin Value:", reading)
    time.sleep(1)
