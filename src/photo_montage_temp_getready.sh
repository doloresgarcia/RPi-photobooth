#!/bin/bash
echo $1
name_file="/home/pi/photobooth_images/photo"
name_file+=${1}
name_file+=".jpg"
echo $name_file
convert $name_file -resize 307x260^ -gravity center -quality 90  -rotate '-90' "/home/pi/photobooth_images/photo_temp.jpg"
TEMPLATE_FILE="/home/pi/RPi-photobooth/images_wait/Nextphoto_out_temp.jpg"
FINAL_FILE="/home/pi/RPi-photobooth/images_wait/Nextphoto_out_temp_display.jpg"

TOP_LEFT_FILE="/home/pi/photobooth_images/photo_temp.jpg"
convert "$TEMPLATE_FILE" "$TOP_LEFT_FILE" -geometry +450+50 -composite "$FINAL_FILE"
rm /home/pi/photobooth_images/photo_temp.jpg





