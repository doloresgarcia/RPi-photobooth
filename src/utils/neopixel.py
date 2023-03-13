from time import sleep 
import time
import subprocess
import os


#def leds_red_charger(pixels):
#    for i in range(0,120):
#        pixels[i]=(0,255, 0, 0)
#        if i >= 7:
#            pixels[i-7]=(0,0, 0, 0)

def leds_blue_charger(pixels):
    pixels.fill((0, 0, 255, 0))
    list1 = list(range(0,55))[::-1]
    list2 = list(range(55,74))[::-1]
    all_pixels_ordered = list1 + list2 

    for i in all_pixels_ordered:
        pixels[i]=(0,0, 0, 0)
        sleep(10.0/72.0)

def leds_purple_loading(pixels):
    pixels.fill((0, 255, 255, 0))


def turn_leds_off(pixels):
    pixels.fill((0, 0, 0, 0))

def make_led_flash(pixels):
    pixels.fill((0, 0, 0, 255))

def upper_button_purple(pixels):
    # 72,73,0
    list_of_pixels = [72,73]

    for index,el in enumerate(list_of_pixels):
        pixels[el]=(0,150, 150, 0)

def lower_button_blue(pixels):
    list_of_pixels = [2,3]
    for index,el in enumerate(list_of_pixels):
        pixels[el]=(0,0, 150, 0)
           

def leds_purple_charger(pixels):
    pixels.fill((0, 255, 255, 0))
    list1 = list(range(0,55))[::-1]
    list2 = list(range(55,74))[::-1]
    all_pixels_ordered = list1 + list2 

    for i in all_pixels_ordered:
        pixels[i]=(0,0, 0, 0)
        sleep(22.0/72.0)
