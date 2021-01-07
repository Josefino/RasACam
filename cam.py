from guizero import App, Text, PushButton, Slider, TextBox, Box, ButtonGroup, info, Drawing, Picture, CheckBox
import subprocess, os, signal
import socket


app = App("RasACam", width=380, height=380, layout="grid")

empty_text=Text(app, text="", grid=[0,1])

# Nastavení sliderů pro expozici a její čas
Text(app, "Number of exposure", grid=[0,4])
number_slider = Slider(app, start=1, end=100, grid=[0,6])
Text(app, "Time of exposure", grid=[1,4])
time_slider = Slider(app, start=1, end=100, grid=[1,6])
empty_text=Text(app, text="", grid=[0,8])

# Spuštění programu ALS pro aligment a zobrazení snímků
cmd = ("~/./Downloads/als/als")
run_bash = subprocess.Popen(cmd, stdout=subprocess.PIPE, shell = True)

# Stiskem tl. Make picture se načtou hodny sliderů a zavolá bash pro vytvoření snímků
def make_picture():
    if choice_format.value == 'RAW':
        run_bash = subprocess.Popen(["./picraw.sh", str(number_slider.value), str(time_slider.value)], stdout=subprocess.PIPE, stdin=subprocess.PIPE)
    if choice_format.value =='JPEG':
        run_bash = subprocess.Popen(["./pichr.sh", str(number_slider.value), str(time_slider.value)], stdout=subprocess.PIPE, stdin=subprocess.PIPE)

# Tl. pro spuštění foto sekvence
make_text = PushButton(app, command=make_picture, text="Make picture", grid=[0,12])


# Stiskem tl. Cocus picture se zobrazí ve VLC obraz z kamery 640x480, případně po volbě Zoom výřez 1/4
def focus_picture():
    run_bash = subprocess.Popen(["./foc.sh", str(checkbox.value)], stdout=subprocess.PIPE, stdin=subprocess.PIPE)    

# Tl. spuštění videa pro zaostření obrázku
focus_text = PushButton(app, command=focus_picture, text="Focus picture", grid=[1,12])

# Volba zoom udělá výřez 1/4 prostřední části obrazu
def zoom():
    zoom_value=checkbox.value

# Check box pro Zoom volbu
checkbox = CheckBox(app, text="Zoom", command=zoom, grid=[1,15])

# Volba formátu výstupu z kamery (16 bit FITS, 8 bit JPEG)    
def pic_format():
    pic_format_value = choice_format.value

# Přepínač volby nastavení formátu výstup z kamery
choice_format = ButtonGroup(app, command=pic_format, options=["RAW", "JPEG"], selected="RAW", grid=[0,18])

# Nouzové končení programu 
def stop_capture():
    terminate = os.getpid()
    os.kill(terminate, 9)
    
# Tl. ukončení programu    
empty_text=Text(app, text="", grid=[0,21])    
stop_text = PushButton(app, command=stop_capture, text="Terminate", grid=[0,22])

# Info text a logo
empty_text=Text(app, text="", grid=[0,23])
info_message = Text(app, text="Raspberry Astronomy Cam v.1.01 © 2021", size=8, grid=[0,32])
pic = Picture(app, image="RasACam_logo.gif", grid=[1,22])


app.display()
