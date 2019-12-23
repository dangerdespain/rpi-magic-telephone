from pad4pi import rpi_gpio
import RPi.GPIO as GPIO
import time
import os
import pyaudio
import wave
# p = pyaudio.PyAudio()

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

def callback(in_data, frame_count, time_info, status):
    data = wf.readframes(frame_count)
    return (data, pyaudio.paContinue)
# Try factory.create_4_by_3_keypad
# and factory.create_4_by_4_keypad for reasonable defaults
keypad = factory.create_keypad(keypad=KEYPAD, row_pins=ROW_PINS, col_pins=COL_PINS)

FILE = 'alphabet/' + str(key)
if key == '*' || key == '#':
    FILE = FILE = 'words/PLEASURE'


def printKey(key):
    FILENAME = os.path.dirname(os.path.abspath(__file__))  + '/audio/speak_and_spell/' + FILE + '.wav'
    print(FILENAME)
    os.system('aplay ' + FILENAME)
    # wf = wave.open(FILENAME, 'rb')

    # p = pyaudio.PyAudio()

    # stream = p.open(format=p.get_format_from_width(wf.getsampwidth()),
    #                 channels=wf.getnchannels(),
    #                 rate=wf.getframerate(),
    #                 output=True,
    #                 stream_callback=callback)

    # stream.start_stream()
    # data = wf.readframes(CHUNK)

# printKey will be called each time a keypad button is pressed
keypad.registerKeyPressHandler(printKey)

try:
    while(True):

        # if stream.is_active() == False:
        #     stream.stop_stream()
        #     stream.close()
        #     wf.close()

        time.sleep(0.1)
except:
    keypad.cleanup()
