#!/bin/bash

#	RasACam Configuration Script for Raspberry Pi
#﻿  	Copyright (C) 2021 Josef Ladra <josef.ladra@gmail.com>
#	This script and RasACam are free software; you can redistribute it and
#	modify it under the terms of the GNU General Public

echo -e "\033[1;33mWelcome to instalation RasACam for Raspberry Pi\033[m" 

#if [ "$(whoami)" != "root" ]; then
#	echo "Please run this script with sudo.  Exiting now."
#	exit 1
#fi

read -p "Are you ready to proceed (y/n)? " proceed

if [ "$proceed" != "y" ]
then
	exit
fi

# Make dirs for ALS program
cd /home/astroberry && pwd
mkdir -m 777 -p RasACam/als/scan/
mkdir -m 777 RasACam/als/work/

# Set script and ALS to run mode
chmod +x foc.sh pichr.sh picraw.sh
chmod +x Downloads/als/als

# Install module guizero
sudo pip3 install guizero

# Move folder RasACam
mv /home/astroberry/Downloads/RasACam/*.* /home/astroberry/RasACam/

# Install ImageMagick
sudo apt-get install imagemagick

# Install DCRAW
git clone https://github.com/6by9/dcraw
cd /home/astroberry/dcraw && pwd
sudo apt-get install libjasper-dev libjpeg8-dev gettext liblcms2-dev
./buildme
mv /home/astroberry/dcraw/dcraw /home/astroberry/RasACam/

echo -e "\033[1;33mEnd of installation RasACam for Raspberry Pi\033[m"
