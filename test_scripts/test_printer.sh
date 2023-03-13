#!/bin/bash
lp -d Canon_SELPHY_CP1300_HTTP /home/pi/RPi-photobooth/outputs_final/final_1.jpg
sleep 50
cancel -a Canon_SELPHY_CP1300_HTTP
cupsenable Canon_SELPHY_CP1300_HTTP
sudo service cups restart
sleep 6