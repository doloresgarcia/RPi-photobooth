from time import sleep 
import time
import subprocess
import os

def kill_gphoto2_at_start():
    try: # if gphoto2 was already open kill it 
        output = subprocess.check_output("kill -9 $(ps aux | grep gphoto | grep -v grep | tr -s ' ' | cut -d' ' -f2)", 
                                                stderr=subprocess.STDOUT, shell=True)
    except subprocess.CalledProcessError as e:
        output = e.output

    
def remove_temp_photos_at_start():
    try: # remove images in the folder if there are any
        subprocess.check_output("rm /home/pi/photobooth_images/* ", stderr=subprocess.STDOUT, shell=True,)
    except subprocess.CalledProcessError as e:
        print('no photos to erase')

def kill_feh():
    try:  # kill feh if its running
        subprocess.check_output("sudo pkill feh", stderr=subprocess.STDOUT, shell=True,)
    except:
        print('first pic')

def remove_final_ifany():
    try:
        subprocess.check_output("rm /home/pi/RPi-photobooth/outputs_final/final_print/* ", stderr=subprocess.STDOUT,shell=True)
    except subprocess.CalledProcessError as e:
        output = e.output