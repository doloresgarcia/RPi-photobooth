import RPi.GPIO as GPIO # Import Raspberry Pi GPIO library
from time import sleep 
import board
import neopixel
import time
import subprocess
import os
from src.utils.neopixel import leds_red_charger, make_led_flash,turn_leds_off, leds_purple_loading, turn_leds_off
from src.utils.display_images import display_photo, display_smile, display_loading

os.environ['DISPLAY']=':0'

gpout = subprocess.check_output("sudo convert -rotate '-90' /home/pi/RPi-photobooth/images_wait/StartHere.jpg /home/pi/RPi-photobooth/images_wait/StartHere_out.jpg", 
                                            stderr=subprocess.STDOUT, shell=True)
subprocess.call("feh -F /home/pi/RPi-photobooth/images_wait/StartHere_out.jpg  &", shell=True)
#gpout = subprocess.check_output("unclutter -idle 0", 
#                                            stderr=subprocess.STDOUT, shell=True)
sleep(60)
subprocess.call("sudo pkill feh", shell=True)
