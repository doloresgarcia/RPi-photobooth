import RPi.GPIO as GPIO # Import Raspberry Pi GPIO library
from time import sleep 
import board
import neopixel
import time
import subprocess
import os
from functions import leds_red_charger, make_led_flash, display_photo, turn_leds_off, display_smile, display_loading
from functions import leds_purple_loading, display_ready
pixels = neopixel.NeoPixel(board.D18, 120, pixel_order=neopixel.RGBW)

turn_leds_off(pixels)