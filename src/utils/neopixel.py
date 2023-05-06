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
        sleep(8.0/72.0) # this happens during 8 seconds

def leds_purple_loading(pixels):
    pixels.auto_write=True
    pixels.fill((0, 255, 255, 0))


def turn_leds_off(pixels):
    pixels.auto_write=True
    pixels.fill((0, 0, 0, 0))

def make_led_flash(pixels):
    pixels.fill((0, 0, 0, 255))

def upper_button_purple(pixels):
    # 72,73,0
    pixels.auto_write=True
    list_of_pixels = [72,73]

    for index,el in enumerate(list_of_pixels):
        pixels[el]=(0,150, 150, 0)

def lower_button_blue(pixels):
    pixels.auto_write=True
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

def leds_smooth_charger(pixels):
    tail_length = 20
    nb_leds = 74
    max_brightness = 200
    head = 30

    brightness = [0]*nb_leds

    for j in range(1, tail_length):
        brightness[j] = 1-j/tail_length

    # pixels.fill((0, 255, 255, 0))
    list1 = list(range(0,55))[::-1]
    list2 = list(range(55,74))[::-1]
    all_pixels_ordered = list1 + list2 
    pixels.auto_write=False

    for x in range(1,10):
        for t in range(1, 100):
            for i in all_pixels_ordered:
                pixels[(i + head) % nb_leds] = (0, max_brightness*brightness[i], max_brightness*brightness[i], 0)
            pixels.show()
            head -= 1
            sleep(2.2/72.0)

    pixels.auto_write=True
    for i in all_pixels_ordered:
        pixels[i]=(0,0, 0, 0)
        # sleep(22.0/72.0)



def leds_blue_charger_smooth(pixels):

    
    pixels.fill((0, 0, 255, 0))
    pixels.auto_write=False
    list1 = list(range(0,55))[::-1]
    list2 = list(range(55,74))[::-1]
    all_pixels_ordered = list1 + list2 

    for i in all_pixels_ordered:
        for p in range(1, 10):
            pixels[i]=(0,0, 255*(1-p/9), 0)
            pixels.show()
            sleep(1.0/72.0)
        #sleep(10.0/72.0)

    pixels.auto_write=True

