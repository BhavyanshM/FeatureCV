#! /bin/bash

sudo apt-get -y update
sudo apt-get -y install python3-pip
sudo pip3 install opencv-python imutils
python3 game.py
