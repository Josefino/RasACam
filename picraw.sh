#!/bin/bash
if [ $# -eq 0 ]
then
	echo "Očekávám parametry - počet snímků a expozice v sekundách" 1>&2
	exit 1
fi

#python3 Ventilator.py #spuštění řízení ventilátoru, teplota 15 st.C
#zenity --warning --width=300 --height=150 --text="S T A R T  O F  S E Q U E N C E"

number=$1
exp=$2
echo "počet snímků" $number "expozice" $exp"s"
totalnumber=$(($number*$exp))
python3 progressbar.py 1 $totalnumber&
exp=$(($exp * 1000000))
i=0
while [ "$i" -ne "$number" ]; do
  echo -n "$(($i+1)) "
  raspistill -r -ss $exp -ISO 400 --mode 2 -w 2024 -h 1520 -o image.jpg
  ./dcraw -6 -T image.jpg && convert -flip -resize 2024 image.tiff image.fits
  mv image.fits /home/astroberry/RasACam/als_jobs/scan
  i=$(($i+1))
done
zenity --warning --width=300 --height=150 --text="E N D  O F  S E Q U E N C E"
