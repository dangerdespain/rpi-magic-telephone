from pad4pi import rpi_gpio
import RPi.GPIO as GPIO
import time
import os
import pygame

KEYPAD = [
    [6,4,5], # [1, 2, 3], 
    [1,2,3], # [4, 5, 6], 
    [0,"#","*"], # [7, 8, 9], 
    [7,8,9] # ["*", 0, "#"] 
]

ROW_PINS = [4, 8, 7, 17] # BCM numbering
COL_PINS = [23, 24, 25] # BCM numbering

factory = rpi_gpio.KeypadFactory()
keypad = factory.create_keypad(keypad=KEYPAD, row_pins=ROW_PINS, col_pins=COL_PINS)

PATH = os.path.dirname(os.path.abspath(__file__))
pygame.mixer.init()

def printKey(key):
    
    FILE = 'alphabet/' + str(key)
    if key == '*' or key == '#':
        FILE = 'words/PLEASURE'

    FILENAME = PATH  + '/audio/speak_and_spell/' + FILE + '.wav'

    if pygame.mixer.music.get_busy() != True:
        pygame.mixer.music.stop()
    pygame.mixer.music.load(FILENAME)
    pygame.mixer.music.play()

keypad.registerKeyPressHandler(printKey)

try:
    while(True):
        time.sleep(0.1)
except:
    keypad.cleanup()
