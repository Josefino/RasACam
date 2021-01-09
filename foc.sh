#!/bin/bash
if [ $# -eq 0 ]
then
	echo "Awaiting parametr of resolution (0 or 1)" 1>&2
	exit 1
fi

zoom=$1

echo "setting zoom" $zoom
echo "Running for 120s"

if [ $zoom -eq 0 ]
then
	python3 Video_server.py | python3 Kamera_stream.py	
else 
	python3 Video_server.py | python3 Kamera_stream_zoom.py
fi
	
