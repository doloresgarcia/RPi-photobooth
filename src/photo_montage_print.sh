#!/bin/bash
#mogrify -resize 535x660 /home/pi/photobooth_images/*.jpg
convert "/home/pi/photobooth_images/photo0.jpg" -resize 555x440^ -gravity center -extent 555x440 -quality 90 "/home/pi/photobooth_images/photo0.jpg"
convert "/home/pi/photobooth_images/photo1.jpg" -resize 555x440^ -gravity center -extent 555x440 -quality 90 "/home/pi/photobooth_images/photo1.jpg"
convert "/home/pi/photobooth_images/photo2.jpg" -resize 555x440^ -gravity center -extent 555x440 -quality 90 "/home/pi/photobooth_images/photo2.jpg"
TEMPLATE_FILE="/home/pi/RPi-photobooth/templates/4x6.jpg"
FINAL_FILE="/home/pi/RPi-photobooth/outputs_final/final_print/final.jpg"

TOP_LEFT_FILE="/home/pi/photobooth_images/photo0.jpg"
convert "$TEMPLATE_FILE" "$TOP_LEFT_FILE" -geometry +20+20 -composite "$FINAL_FILE"
convert "$FINAL_FILE" "$TOP_LEFT_FILE" -geometry +615+20  -composite "$FINAL_FILE"

TOP_RIGHT_FILE="/home/pi/photobooth_images/photo1.jpg"
convert "$FINAL_FILE" "$TOP_RIGHT_FILE" -geometry +20+480  -composite "$FINAL_FILE"
convert "$FINAL_FILE" "$TOP_RIGHT_FILE" -geometry +615+480 -composite "$FINAL_FILE"

BOT_LEFT_FILE="/home/pi/photobooth_images/photo2.jpg"
convert "$FINAL_FILE" "$BOT_LEFT_FILE" -geometry +20+940 -composite "$FINAL_FILE"
convert "$FINAL_FILE" "$BOT_LEFT_FILE" -geometry +615+940 -composite "$FINAL_FILE"

convert "/home/pi/photobooth_images/photo0.jpg" -resize 237x190^ -gravity center -quality 90 "/home/pi/photobooth_images/photo0.jpg"
convert "/home/pi/photobooth_images/photo1.jpg" -resize 237x190^ -gravity center -quality 90 "/home/pi/photobooth_images/photo1.jpg"
convert "/home/pi/photobooth_images/photo2.jpg" -resize 237x190^ -gravity center -quality 90 "/home/pi/photobooth_images/photo2.jpg"
TEMPLATE_FILE="/home/pi/RPi-photobooth/images_wait/Print2.jpg"
FINAL_FILE="/home/pi/RPi-photobooth/outputs_final/final_screen.jpg"

TOP_LEFT_FILE="/home/pi/photobooth_images/photo0.jpg"
convert "$TEMPLATE_FILE" "$TOP_LEFT_FILE" -geometry +15+75 -composite "$FINAL_FILE"

TOP_RIGHT_FILE="/home/pi/photobooth_images/photo1.jpg"
convert "$FINAL_FILE" "$TOP_RIGHT_FILE" -geometry +15+280  -composite "$FINAL_FILE"

BOT_LEFT_FILE="/home/pi/photobooth_images/photo2.jpg"
convert "$FINAL_FILE" "$BOT_LEFT_FILE" -geometry +15+485 -composite "$FINAL_FILE"




