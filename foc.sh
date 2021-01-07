#!/bin/bash
if [ $# -eq 0 ]
then
	echo "Očekávám parametr rozlišení (0 nebo 1)" 1>&2
	exit 1
fi

zoom=$1

echo "nastaven zoom" $zoom
echo "Ostření spuštěno na max 120s"

if [ $zoom -eq 0 ]
then
	python3 Video_server.py | python3 Kamera_stream.py	
else 
	python3 Video_server.py | python3 Kamera_stream_zoom.py
fi
	
