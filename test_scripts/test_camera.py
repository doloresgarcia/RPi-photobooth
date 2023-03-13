import RPi.GPIO as GPIO # Import Raspberry Pi GPIO library
from time import sleep 
import board
import neopixel
import time
import subprocess
import os
from functions import leds_red_charger, make_led_flash, display_photo, turn_leds_off, display_smile, display_loading
from functions import leds_purple_loading, display_ready

output = None
try:
    output = subprocess.check_output("kill -9 $(ps aux | grep gphoto | grep -v grep | tr -s ' ' | cut -d' ' -f2)", 
                                            stderr=subprocess.STDOUT, shell=True)
except subprocess.CalledProcessError as e:
    output = e.output
    
gpout = subprocess.check_output("gphoto2 --capture-image-and-download --filename /home/pi/test_images/testphoto.jpg", 
                                            stderr=subprocess.STDOUT, shell=True)