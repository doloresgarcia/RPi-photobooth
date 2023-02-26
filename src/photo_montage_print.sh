#!/bin/bash
#mogrify -resize 535x660 /home/pi/photobooth_images/*.jpg
convert "/home/pi/photobooth_images/photo0.jpg" -resize 555x440^ -gravity center -extent 555x440 -quality 90 "/home/pi/photobooth_images/photo0.jpg"
convert "/home/pi/photobooth_images/photo1.jpg" -resize 555x440^ -gravity center -extent 555x440 -quality 90 "/home/pi/photobooth_images/photo1.jpg"
convert "/home/pi/photobooth_images/photo2.jpg" -resize 555x440^ -gravity center -extent 555x440 -quality 90 "/home/pi/photobooth_images/photo2.jpg"
TEMPLATE_FILE="/home/pi/4x6.jpg"
FINAL_FILE="/home/pi/final.jpg"

TOP_LEFT_FILE="/home/pi/photobooth_images/photo0.jpg"
convert "$TEMPLATE_FILE" "$TOP_LEFT_FILE" -geometry +20+20 -composite "$FINAL_FILE"
convert "$FINAL_FILE" "$TOP_LEFT_FILE" -geometry +615+20  -composite "$FINAL_FILE"

TOP_RIGHT_FILE="/home/pi/photobooth_images/photo1.jpg"
convert "$FINAL_FILE" "$TOP_RIGHT_FILE" -geometry +20+480  -composite "$FINAL_FILE"
convert "$FINAL_FILE" "$TOP_RIGHT_FILE" -geometry +615+480 -composite "$FINAL_FILE"

BOT_LEFT_FILE="/home/pi/photobooth_images/photo2.jpg"
convert "$FINAL_FILE" "$BOT_LEFT_FILE" -geometry +20+940 -composite "$FINAL_FILE"
convert "$FINAL_FILE" "$BOT_LEFT_FILE" -geometry +615+940 -composite "$FINAL_FILE"




