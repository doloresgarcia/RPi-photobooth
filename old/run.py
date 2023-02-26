import time
import subprocess
import os


# take 3 photos 
tick = 0
time_now = time.strftime("%d-%H:%M:%S:")
while tick < 3:
    name_photo = "photo"+ str(tick)
    print("CLICK!")
    gpout = subprocess.check_output("gphoto2 --capture-image-and-download --filename /home/pi/photobooth_images/"+name_photo+".jpg", 
                                    stderr=subprocess.STDOUT, shell=True)

    print(gpout)
    #save full res photo 
    gpout = subprocess.check_output("scp  /home/pi/photobooth_images/"+name_photo+".jpg" /home/pi/copies_full_res/+time_now+name_photo+".jpg", 
                                    stderr=subprocess.STDOUT, shell=True)
    print(gpout)
    time.sleep(0.5)

print("about to call print_photo script...")
subprocess.call("sudo /home/pi/photobooth/print_photo", shell=True)

