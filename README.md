# RasACam
EAA Astronomy Camera
Instructions for running SW for RasACam (Raspberry Astronomy Camera)

Version history:

Version 1.01
Completed progress bar for displaying in what time phase is sky capturing
(exposure time x number of exposures)

Version 1.0
The first functional application

---------------------------------
Installation:
1. Unzip the downloaded RasACam.zip file in the Downloads folder. You can run the script
"./rasacam.sh" (if it is not possible to run, set the rights with the command "chmod + x rasacam.sh"),
which creates the RasACam, als, scan and work directories and copies them all
unzipped files to the RasACam directory. In second step installs DCRAW
with the necessary libraries and it installs ImageMagick.

2. Download software ALS to RasACam folder, unzip and rename folder to "als" and also
executive program to "als". You can download it fro github: https://github.com/gehelem/als

--------------------------
Running RsACam:
Switch to the RasACam directory and run the command in the terminal
"python3 cam.py", which launches the RasACam GUI and the ALS program. In the ALS program
set the path to the working folder als_jobs / scan and / work.

----------------------------
Use the following scripts for manual control:

1. To focus on a given object or adjust the composition, run a script
./foc.sh x, where x is equal to 0 at full resolution, or 1, for ROI 0.25x.

Example:
./foc.sh 0 is a standard FOV resolution of 640x480 pix
./foc.sh 1 is a 1/4 standard FOV of the camera from the center of the field.

2. To take pictures of the sky, first start the program ./als (found in
folder als-xxx), where we set the necessary parameters and start alignment

3. Now run the script ./pichr x y for JPEG, or ./picraw.sh x y for RAW, where
x is the number of exposures and y is the duration of the exposure in seconds.

Example:
./pichr.sh 10 10 means resolution 2028x1520 pix, number of frames 10, exposure 10s
./picraw.sh 10 10 means resolution 4056x3040 pix, number of pictures 10, exposure 10s

4. After starting, the individual images in the als program and the resulting ones will start to compose
we can save the image (work directory).
