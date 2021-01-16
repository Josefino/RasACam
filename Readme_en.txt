Manual for software RasACam (Raspberry Astronomy Camera)
--------------------------------------------------------------

History:

Version 1.01
Add progress bar for state of capturing 
(Exposure time x Number of the exposure)

Verze 1.0
First version of software

------------------------

Installation:
1. Download zip file RasACam.zip in Downloads folder. Run script  "./rasacam.sh",  it makes folders RasACam, als, scan a work a  Copy all unzip files to RasACam folder. Then install software DCRAW with libraries and install ImageMagick. You need also manual install VLC software.

2. Download software ALS to folder RasACam, unzip it and rename folder "als-xxxx" to "als" and rename program "als-xxxx" to "als". Program you can download from github: https://github.com/gehelem/als

Running:
3. Go to folder RasACam and run ./rasacam.sh in terminal, which run GUI RasACam  and program ALS. In programu ALS set path to working folders als_jobs/scan and /work.

--------------------------

For manual control use these scripts:

1. For focusing the object or set composition run script  ./foc.sh x, where x is equal 0 for full resolution, or 1, for ROI 0,25x.

Example:
./foc.sh 0 is resolution 640x480 pix video in VLC software
./foc.sh 1 is ROI 0,25 od FOV in the center of the picture video in VLC software

2. For alignment run software ALS ./als (it find in folder als), where set a parameters and run the capturing.

3. Now run script ./pichr x y for JPEG format (or ./picraw x y for RAW format), where  "x" is number of exposure and "y" is exposure in seconds.

Example:
./pichr.sh 10 10 is resolution 2028x1520 pix, number of pictures 10, exposure 10s
./picraw.sh 10 10 is resolution 4056x3040 pix, number of pictures 10, exposure 10s

4. After running script you can see picture in ALS app after alignment (it is in folder "work") or we can save it in the every moment.
