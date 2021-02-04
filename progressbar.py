from tkinter import *
from tkinter.ttk import *
from guizero import App, Text, PushButton
import sys, os
from guizero import PushButton

# Progress bar for capturing
############################

# Find CPU model of Raspberry
def getrevision():
  # Extract board revision from cpuinfo file
  myrevision = "0000"
  try:
    with open('/proc/cpuinfo','r', encoding='utf-8') as f:
        for line in f.readlines():
            if "Revision" in line[0:50]:
                length=len(line)
                myrevision = line[11:length-1]
    f.close()
  except:
    myrevision = "0000"
    
  return myrevision
 
b=getrevision() # call function model of RPi

if b == "a22023": #RPi 3
    c = 430
elif b == "a020d3": # RPi3
    c = 430
elif b == "b03111": #RPi 4
    c = 380
elif b == "b03112": #RPi 4
    c = 380
elif b == "b03114": #RPi 4
    c = 380


a = str(sys.argv[2])
a = c * int(a) # set interval of the bar

def bar():
    # progress['value'] is from ttk
    if progress['value'] < 100:
        progress['value'] += 5
        app.after(a, bar)

app = App("RasACam", width=300, height=100)

gz_text = Text(app, "Progress")

# This bit comes from ttk
# --------------------------------------------------------------------------------
progress = Progressbar(app.tk,orient=HORIZONTAL,length=200)
progress.pack()
# --------------------------------------------------------------------------------

bar()

def close_win():
    sys.exit()
    
    
close = PushButton(app, command=close_win, text="Close")

app.display()





