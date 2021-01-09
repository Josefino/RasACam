from guizero import App, Text, PushButton, Slider, TextBox, Box, ButtonGroup, info, Drawing, Picture, CheckBox
import subprocess, os, signal
import socket

# Main utility for a capturing pictures
#######################################


app = App("RasACam", width=380, height=380, layout="grid")

empty_text=Text(app, text="", grid=[0,1])

# Setting sliders for number of pictures and time of exposure 
Text(app, "Number of exposure", grid=[0,4])
number_slider = Slider(app, start=1, end=100, grid=[0,6])
Text(app, "Time of exposure", grid=[1,4])
time_slider = Slider(app, start=1, end=100, grid=[1,6])
empty_text=Text(app, text="", grid=[0,8])

# Run software ALS for alignment and display pictures
cmd = ("~/./Downloads/als/als")
run_bash = subprocess.Popen(cmd, stdout=subprocess.PIPE, shell = True)

# After pushing button "Make picture" are read parameters from sliders and call bash for Makinng pictures.
def make_picture():
    if choice_format.value == 'RAW':
        run_bash = subprocess.Popen(["./picraw.sh", str(number_slider.value), str(time_slider.value)], stdout=subprocess.PIPE, stdin=subprocess.PIPE)
    if choice_format.value =='JPEG':
        run_bash = subprocess.Popen(["./pichr.sh", str(number_slider.value), str(time_slider.value)], stdout=subprocess.PIPE, stdin=subprocess.PIPE)

# Button for running capture
make_text = PushButton(app, command=make_picture, text="Make picture", grid=[0,12])


# Pushing button "Focus picture" display in VLC software picture from camera 640x480 pix normal resolution or ROI
def focus_picture():
    run_bash = subprocess.Popen(["./foc.sh", str(checkbox.value)], stdout=subprocess.PIPE, stdin=subprocess.PIPE)    

# Botton for focusing
focus_text = PushButton(app, command=focus_picture, text="Focus picture", grid=[1,12])

# Setting zoom - ROI 25%x25% in the middle of the picture
def zoom():
    zoom_value=checkbox.value

# Check box for Zoom choice
checkbox = CheckBox(app, text="Zoom", command=zoom, grid=[1,15])

# Choice format from camera (16 bit FITS, 8 bit JPEG)    
def pic_format():
    pic_format_value = choice_format.value

# Switch choice setting RAW or JPEG
choice_format = ButtonGroup(app, command=pic_format, options=["RAW", "JPEG"], selected="RAW", grid=[0,18])

# Terminate program 
def stop_capture():
    terminate = os.getpid()
    os.kill(terminate, 9)
    
# Button terminate program    
empty_text=Text(app, text="", grid=[0,21])    
stop_text = PushButton(app, command=stop_capture, text="Terminate", grid=[0,22])

# Name of software and logo
empty_text=Text(app, text="", grid=[0,23])
info_message = Text(app, text="Raspberry Astronomy Cam v.1.01 © 2021", size=8, grid=[0,32])
pic = Picture(app, image="RasACam_logo.gif", grid=[1,22])


app.display()
