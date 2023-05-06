import RPi.GPIO as GPIO # Import Raspberry Pi GPIO library
from time import sleep 
import board
import neopixel
import time
import subprocess
import os
import signal
from src.utils.display_images import display_photo, display_smile, display_loading, display_start, display_empty
from src.utils.display_images import handler
from src.utils.neopixel import leds_purple_loading,upper_button_purple,leds_blue_charger, make_led_flash, turn_leds_off, leds_smooth_charger, leds_blue_charger_smooth
from src.utils.neopixel import leds_purple_charger, lower_button_blue
from src.utils.photos import kill_gphoto2_at_start, remove_temp_photos_at_start, kill_feh, remove_final_ifany

#set up board and display 
INPUT_TAKE_PHOTO = 4
INPUT_PRINT = 22
pixels = neopixel.NeoPixel(board.D18, 120, pixel_order=neopixel.RGBW)
GPIO.setmode(GPIO.BCM) # Use physical pin numbering
GPIO.setup(INPUT_TAKE_PHOTO, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(INPUT_PRINT, GPIO.IN, pull_up_down=GPIO.PUD_UP)
output = None
os.environ['DISPLAY']=':0'  

#checks at start
kill_gphoto2_at_start()
remove_temp_photos_at_start()
print('turning leds off')
turn_leds_off(pixels)
kill_feh()
display_start()
upper_button_purple(pixels)

while True: # Run forever
    if GPIO.input(INPUT_TAKE_PHOTO) ==  GPIO.LOW:
        signal.alarm(0)
        print('the button has been clicked and the sequence of 3 photos starts')
        remove_final_ifany() # remove the final in case there is one in the folder
        time_now = time.strftime("%d-%H:%M:%S:")
        number_of_photos_in_folder = 0 
        number_of_photos_in_folder_old = 0
        while number_of_photos_in_folder < 3:
            name_photo = "photo"+ str(number_of_photos_in_folder)
            display_smile()
            leds_blue_charger_smooth(pixels) 
            print("CLICK!")
            make_led_flash(pixels)
            display_empty()
            kill_gphoto2_at_start()
            subprocess.check_output("sudo gphoto2  --capture-image-and-download --filename /home/pi/photobooth_images/"+name_photo+".jpg", 
                                                stderr=subprocess.STDOUT, shell=True)
            number_of_photos_in_folder = len(os.listdir('/home/pi/photobooth_images/'))
            turn_leds_off(pixels) 
            if number_of_photos_in_folder>number_of_photos_in_folder_old:
                number_of_photos_in_folder_old += 1
                gpout = subprocess.check_output("scp  /home/pi/photobooth_images/"+name_photo+".jpg"+" " +"/home/pi/copies_full_res/"+time_now+name_photo+".jpg",  #save full res photo 
                                            stderr=subprocess.STDOUT, shell=True)

        print("about to call make_collage script...")
        display_empty()
        subprocess.Popen("sudo bash /home/pi/RPi-photobooth/src/photo_montage_print.sh", shell=True)
        #subprocess.Popen("sudo bash /home/pi/RPi-photobooth/src/photo_montage_screen.sh", shell=True)
        leds_smooth_charger(pixels)
        gpout = display_photo()
        print("Erase photos to clean folder...")
        subprocess.call("rm /home/pi/photobooth_images/* ", shell=True)
        # do you want to print? 
        # at this point the screen is showing the last photo with the new print buttons and the leds are off
        upper_button_purple(pixels)
        lower_button_blue(pixels)
        signal.signal(signal.SIGALRM, handler)
        signal.alarm(60)
        


    if GPIO.input(INPUT_PRINT) ==  GPIO.LOW:
        signal.alarm(0)
        #print the last photo stored in the final
        #check if the final exists 
        if len(os.listdir('/home/pi/RPi-photobooth/outputs_final/final_print'))>0:
            subprocess.Popen("sudo bash /home/pi/RPi-photobooth/src/print_photo.sh", shell=True)
            time.sleep(5)
            kill_feh()
            display_start()
            turn_leds_off(pixels)
            upper_button_purple(pixels)
        else:

            print('no photo to print')
            kill_feh()
            display_start()
            turn_leds_off(pixels)
            upper_button_purple(pixels)


