from pad4pi import rpi_gpio
import RPi.GPIO as GPIO
import time
import os


GPIO.setwarnings(False)

KEYPAD = [
    [6,4,5], # [1, 2, 3], 
    [1,2,3], # [4, 5, 6], 
    [0,"#","*"], # [7, 8, 9], 
    [7,8,9] # ["*", 0, "#"] 
]

ROW_PINS = [4, 14, 15, 17] # BCM numbering
COL_PINS = [23, 24, 25] # BCM numbering

factory = rpi_gpio.KeypadFactory()

# Try factory.create_4_by_3_keypad
# and factory.create_4_by_4_keypad for reasonable defaults
keypad = factory.create_keypad(keypad=KEYPAD, row_pins=ROW_PINS, col_pins=COL_PINS)

def printKey(key):
    print(key)
    print('aplay ' + os.path.dirname(__file__) + '/speak_and_spell/alphabet/.wav')
    os.system('aplay ' + os.path.dirname(__file__) + '/speak_and_spell/alphabet/' + str(key) + '.wav')

# printKey will be called each time a keypad button is pressed
keypad.registerKeyPressHandler(printKey)

try:
    while(True):
        time.sleep(0.2)
except:
    keypad.cleanup()
