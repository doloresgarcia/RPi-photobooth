import RPi.GPIO as GPIO # Import Raspberry Pi GPIO library
from time import sleep 
import board
import neopixel
import time
import subprocess
import os
import sys
sys.path.insert(0, '../src')
from src.utils.neopixel import turn_leds_off
from src.utils.neopixel import leds_smooth_charger
pixels = neopixel.NeoPixel(board.D18, 120, pixel_order=neopixel.RGBW)

turn_leds_off(pixels)
leds_smooth_charger(pixels)