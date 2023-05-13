import RPi.GPIO as GPIO # Import Raspberry Pi GPIO library
from time import sleep 
import board
import neopixel
import time
import subprocess
import os


os.environ['DISPLAY']=':0'

gpout = subprocess.check_output("sudo convert -rotate '-90' /home/pi/RPi-photobooth/images_wait/photoalmostready.jpg /home/pi/RPi-photobooth/images_wait/photoalmostready_out.jpg", 
                                            stderr=subprocess.STDOUT, shell=True)
subprocess.call("feh -F /home/pi/RPi-photobooth/images_wait/photoalmostready_out.jpg  &", shell=True)
#gpout = subprocess.check_output("unclutter -idle 0", 
#                                            stderr=subprocess.STDOUT, shell=True)
sleep(60)
subprocess.call("sudo pkill feh", shell=True)
