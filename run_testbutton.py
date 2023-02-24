import RPi.GPIO as GPIO # Import Raspberry Pi GPIO library
from time import sleep 
import board
import neopixel
import time
import subprocess
import os
from src.utils.display_images import display_photo, display_smile, display_loading, display_start
from src.utils.neopixel import leds_purple_loading,upper_button_green,leds_red_charger, make_led_flash, turn_leds_off
from src.utils.photos import kill_gphoto2_at_start, remove_temp_photos_at_start, kill_feh

#set up board and display 
pixels = neopixel.NeoPixel(board.D18, 120, pixel_order=neopixel.RGBW)
GPIO.setmode(GPIO.BCM) # Use physical pin numbering
GPIO.setup(4, GPIO.IN, pull_up_down=GPIO.PUD_UP)
output = None
os.environ['DISPLAY']=':0'  

#checks at start
kill_gphoto2_at_start()
remove_temp_photos_at_start()
turn_leds_off(pixels)
kill_feh()
display_start()
upper_button_green(pixels)


while True: # Run forever
    if GPIO.input(4) ==  GPIO.LOW:
        print('the button has been clicked and the sequence of 3 photos starts')
        # take 3 photos 
        #tick = 0
        time_now = time.strftime("%d-%H:%M:%S:")
        display_smile()
        flag_all_photos = True 
        number_of_photos_in_folder = 0 
        number_of_photos_in_folder_old = 0
        while number_of_photos_in_folder < 3:
            name_photo = "photo"+ str(number_of_photos_in_folder)
            leds_red_charger(pixels) # leds do loop 
            # take photo
            print("CLICK!")
            make_led_flash(pixels)

          
            subprocess.check_output("gphoto2  --capture-image-and-download --filename /home/pi/photobooth_images/"+name_photo+".jpg", 
                                                stderr=subprocess.STDOUT, shell=True)
            
            number_of_photos_in_folder = len(os.listdir('/home/pi/photobooth_images/'))

            turn_leds_off(pixels) 
            if number_of_photos_in_folder>number_of_photos_in_folder_old:
            #save full res photo 
                number_of_photos_in_folder_old += 1
                gpout = subprocess.check_output("scp  /home/pi/photobooth_images/"+name_photo+".jpg"+" " +"/home/pi/copies_full_res/"+time_now+name_photo+".jpg", 
                                            stderr=subprocess.STDOUT, shell=True)
                #print(gpout)
                #tick += 1

        
        print("about to call make_collage script...")

        display_loading()
        print('done display')
        leds_purple_loading(pixels)
        subprocess.call("sudo bash /home/pi/RPi-photobooth/photo_montage33.sh", shell=True)
        print("diplay photo...")
        time.sleep(1)
        subprocess.call("sudo bash /home/pi/RPi-photobooth/photo_montage_screen.sh", shell=True)
        gpout = display_photo()
        print(gpout)
        print("Errase photos to clean folder...")
        subprocess.call("rm /home/pi/photobooth_images/* ", shell=True)
        leds_purple_loading(pixels)
        time.sleep(60)

        try: 
            subprocess.call("sudo pkill feh", shell=True)
        except:
            print('end of program')
        print('ready to go again')
        subprocess.call("feh -F /home/pi/RPi-photobooth/images_wait/Start2_out.jpg &", shell=True)
        turn_leds_off(pixels)
        upper_button_green(pixels)


