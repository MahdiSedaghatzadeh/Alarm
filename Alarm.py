import tkinter as tk
from datetime import datetime
from pygame import mixer
import time
#import winsound **we could use winsound too but I used mixer for sound

#function for check remaining time
def remaining():
    h1 = datetime.now().hour
    m1 = datetime.now().minute
    s1 = datetime.now().second
    h2 = int(Hour.get())
    m2 = int(Minute.get())
    s2 = int(Second.get())
    if h2<h1:
        h2+=24
    if h2==h1 and m2<m1:
        h2+=24
    h1 *= 3600
    m1 *= 60
    s1 *= 1
    h2 *= 3600
    m2 *= 60
    s2 *= 1
    time1f = h1+m1+s1
    time2f = h2+m2+s2
    timefinal = time2f - time1f
    rem_h = timefinal/3600
    rem_ms = timefinal%3600
    rem_m = rem_ms/60
    rem_s = rem_ms%60
    hfinal = int(rem_h)
    mfinal = int(rem_m)
    sfinal = int(rem_s)
    if hfinal<10:
        hfinal = f"0{hfinal}"
    if mfinal<10:
        mfinal = f"0{mfinal}"
    if sfinal<10:
        sfinal = f"0{sfinal}"
    remain = f"{hfinal}:{mfinal}:{sfinal}"
    return remain

#function for stop ringing
def Break():
    mixer.Sound.stop(wakeup)

#function for convert given time to string
def target():
    time = f"{Hour.get()}:{Minute.get()}:{Second.get()}"
    return time

#function for check the time and ringing up
def Notice():
    while True:
        now = datetime.now()
        now = now.strftime("%H:%M:%S")
        target_time = target()
        remaining_time = remaining()
        time2.delete(0,tk.END)
        time2.insert(tk.END,remaining_time)
        if now == target_time:
            mixer.Sound.play(wakeup)
            #winsound.PlaySound("wakeup.wav",winsound.SND_FILENAME)
            break
        window.update()

#function for create labels
def labels(tex,posx,posy):
    label0 = tk.Label(window , text=tex , fg="black" , bg="#4477ff" , font="none 20 italic")
    label0.place(x=posx , y=posy)

#function for create box
def box(name,widt,posx,posy,bg0=None):
    name = tk.Entry(window , width=widt , fg="black" , bg=bg0 , font="none 20 italic")
    name.place(x=posx , y=posy)
    return name

#function for create button
def button(tex,widt,posx,posy,commmand):
    button0 = tk.Button(window , text=tex , width=widt , fg="white" , bg="black" , font="none 25 bold" , command=commmand)
    button0.place(x=posx , y=posy)

#initialize mixer
mixer.init()

#some variable
wakeup = mixer.Sound("wakeup.wav")
width = 350
height = 400
xpos = 10
ypos = 10

#create window
window = tk.Tk()
window.title("Mahdi's Alarm")
window.geometry(f"{width}x{height}+{xpos}+{ypos}")
window.configure(background = "#4477ff") 

#create some labels
labels("Hour" , 50 , 70)
labels("Min" , 150 , 70)
labels("Sec" , 250 , 70)
warning = tk.Label(window , text="Enter Your Time in 24 Hours" , bg="#4477aa" , borderwidth=5 , relief="groove" , font="none 17 italic")
warning.place(x=25 , y=20)

#create some boxes
Hour = box("Hour" , 3 , 54 , 110)
Minute = box("Min" , 3 , 154 , 110)
Second = box("Sec" , 3 , 254 , 110)
time2 = box("Sec" , 8 , 117 , 275 , bg0="#4477ff")

#create Button
button("SetAlarm" , 10 , 75 , 200 , Notice )
button("Stop" , 4 , 133 , 325 , Break)

#mainloop
window.mainloop()
