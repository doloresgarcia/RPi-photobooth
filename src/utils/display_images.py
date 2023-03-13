from time import sleep 
import time
import subprocess
import os

def display_photo():
    gpout = subprocess.check_output("sudo convert -rotate '-90' /home/pi/RPi-photobooth/outputs_final/final_screen.jpg /home/pi/RPi-photobooth/outputs_final/final_screen_out.jpg",  shell=True)
    subprocess.call("sudo pkill feh", shell=True)
    gpout = subprocess.call("feh -F /home/pi/RPi-photobooth/outputs_final/final_screen_out.jpg &", shell=True)
    return gpout

def display_smile():
    subprocess.call("sudo pkill feh", shell=True)
    gpout = subprocess.call("feh -F /home/pi/RPi-photobooth/images_wait/GetReady_out.jpg  &", 
                                            stderr=subprocess.STDOUT, shell=True)
    return gpout

def display_loading():
    subprocess.call("sudo pkill feh", shell=True)
    gpout = subprocess.call("feh -F /home/pi/RPi-photobooth/images_wait/Print2_out.jpg &", 
                                            stderr=subprocess.STDOUT, shell=True)
    return gpout

def display_start():
    subprocess.call("feh -F /home/pi/RPi-photobooth/images_wait/StartHere_instructions_out.jpg &", shell=True)

def display_empty():
    subprocess.call("sudo pkill feh", shell=True)
    subprocess.call("feh -F /home/pi/RPi-photobooth/images_wait/Empty_out.jpg &", shell=True)



def remove_mouse():
    gpout = subprocess.check_output("unclutter -idle 0", 
                                                stderr=subprocess.STDOUT, shell=True)


def handler(signum, frame):
    print("Forever is over!")
    display_start()
    
