from time import sleep 
import time
import subprocess
import os


def leds_red_charger(pixels):
    for i in range(0,120):
        pixels[i]=(0,255, 0, 0)
        if i >= 7:
            pixels[i-7]=(0,0, 0, 0)

def leds_purple_loading(pixels):
    pixels.fill((0, 255, 255, 0))


def turn_leds_off(pixels):
    pixels.fill((0, 0, 0, 0))

def make_led_flash(pixels):
    pixels.fill((255, 255, 255, 255))

def upper_button_green(pixels):
    # 72,73,0
    list_of_pixels = [72,73,0]

    for index,el in enumerate(list_of_pixels):
        pixels[el]=(255,0, 0, 0)
           