#!/bin/bash
if [ $# -eq 0 ]
then
	echo "Očekávám parametry - počet snímků a expozice v sekundách" 1>&2
	exit 1
fi

#python3 Ventilator.py #spuštění řízení ventilátoru, teplota 15 st.C

number=$1
exp=$2
echo "počet snímků" $number "expozice" $exp"s"

exp=$(($exp * 1000000))
i=0
while [ "$i" -ne "$number" ]; do
  echo -n "$(($i+1)) "
  raspistill -ss $exp -ISO 100 --mode 2 -w 2024 -h 1520 -o image2.jpg
  convert -flip image2.jpg image2.fits
  mv image2.fits /home/astroberry/RasACam/als_jobs/scan
  i=$(($i+1))
done
zenity --warning --width=300 --height=150 --text="E N D  O F  S E Q U E N C E"
