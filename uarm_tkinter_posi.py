#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import tkinter 
import os
import sys
from time import sleep
from uf.wrapper.swift_api import SwiftAPI
from uf.utils.log import *


swift = SwiftAPI() # {'hwid': 'USB VID:PID=2341:0042'}
sleep(2)
swift.set_position(150, 0, 150, speed = 20000, timeout = 20 ) 
swift.flush_cmd() 
sleep(1)


def destructor():
     print("[INFO] Beendet...")
     swift.flush_cmd()
     mainWin.destroy()

def parken():
    swift.set_position(120, 0, 40, speed = 20000 ) 
    uxx.set(120)
    uyy.set(0)
    uzz.set(40)
    uww.set(90)

    vlx.set('X=120')
    vly.set('Y=0')
    vlz.set('Z=40')
    vlw.set('W=90')
    swift.flush_cmd()

def gripper_ein():
    swift.set_gripper(True)

def gripper_aus():
    swift.set_gripper(False)

def sauger_ein():
    #swift.set_pump(True,timeout=2)
    swift.set_pump(True)
    #swift.flush_cmd()
            
def sauger_aus():
    swift.set_pump(False)

def goset():
    px = ex.get()
    py = ey.get()
    pz = ez.get()
    pw = ew.get()

    if px :
        swift.set_position(x = px, speed = 20000)
        uxx.set(px)
        vlx.set('X='+str(px))
    if py :
         swift.set_position(y = py, speed = 20000)
         uyy.set(py)
         vly.set('Y='+str(py))
    if pz :
         swift.set_position(z = pz, speed = 20000)
         uzz.set(pz)
         vlz.set('Z='+str(pz))
    if pw :
         swift.set_wrist(pw, wait = True)
         uww.set(pw)
         vlw.set('W='+str(pw))
    swift.flush_cmd() 


def get_slider(event):
    x = ux.get()
    y = uy.get()
    z = uz.get()
    w = uw.get()
    
    swift.set_wrist(w, wait = True)
    swift.set_position(x, y, z, speed = 20000) 

    vlx.set('X='+str(x))
    vly.set('Y='+str(y))
    vlz.set('Z='+str(z))
    vlw.set('W='+str(w))

    swift.flush_cmd() 



mainWin = tkinter.Tk() 
mainWin.title("RobotArm Positionen")   
mainWin.protocol('WM_DELETE_WINDOW', destructor)

mainFrame = tkinter.Frame(mainWin, height=500, width=500,borderwidth=0, relief='ridge', padx=10, pady=10)
mainFrame.grid(ipadx=5, ipady=5)

uxx = tkinter.IntVar()
uyy = tkinter.IntVar()
uzz = tkinter.IntVar()
uww = tkinter.IntVar()

vlx = tkinter.StringVar()
vly = tkinter.StringVar()
vlz = tkinter.StringVar()
vlw = tkinter.StringVar()

uxx.set(150)
uyy.set(0)
uzz.set(150)
uww.set(90)

vlx.set('X=150')
vly.set('Y=0')
vlz.set('Z=150')
vlw.set('W=90')


info = tkinter.Label(mainFrame, text = swift.get_device_info(),font=("Helvetica", 11),)
#info = tkinter.Label(mainFrame, text = 'xxxx xxxx xxxx xxxx xxxx',font=("Helvetica", 16),)
info.grid(column=2, row=20, columnspan=4)


ux = tkinter.Scale(mainFrame, orient=tkinter.VERTICAL,length=350, from_=110, to=350 ,variable = uxx,
                    command = get_slider, label='x Achse', resolution=0.5)
ux.grid(column=0, row=1, rowspan=40)


b1 = tkinter.Button(mainFrame, text = "Sauger", command = sauger_ein, width = 10)
b1.grid(column=2, row=35)
b2 = tkinter.Button(mainFrame, text = "aus", command = sauger_aus, width = 10)
b2.grid(column=3, row=35)
b3 = tkinter.Button(mainFrame, text = "...", width = 10)
b3.grid(column=4, row=35)
b4 = tkinter.Button(mainFrame, text = "...", width = 10)
b4.grid(column=5, row=35)
b5= tkinter.Button(mainFrame, text = "Gripper", command = gripper_ein, width = 10)
b5.grid(column=2, row=36)
b6 = tkinter.Button(mainFrame, text = "aus", command = sauger_aus, width = 10)
b6.grid(column=3, row=36)
b7 = tkinter.Button(mainFrame, text = "...", width = 10)
b7.grid(column=4, row=36)
b8 = tkinter.Button(mainFrame, text = "...", width = 10)
b8.grid(column=5, row=36)


lx = tkinter.Label(mainFrame, textvariable=vlx)
lx.grid(column=2, row=37)
ly = tkinter.Label(mainFrame, textvariable=vly)
ly.grid(column=3, row=37)
lz = tkinter.Label(mainFrame, textvariable=vlz)
lz.grid(column=4, row=37)
lw = tkinter.Label(mainFrame, textvariable=vlw)
lw.grid(column=5, row=37)

ex = tkinter.Entry(mainFrame, width=10)
ex.grid(column=2, row=38)
ey = tkinter.Entry(mainFrame, width=10)
ey.grid(column=3, row=38)
ez = tkinter.Entry(mainFrame, width=10)
ez.grid(column=4, row=38)
ew = tkinter.Entry(mainFrame, width=10)
ew.grid(column=5, row=38)

go = tkinter.Button(mainFrame, text = "Go", command = goset,width = 20)
go.grid(column=2, row=39, columnspan=2)

uw = tkinter.Scale(mainFrame, orient=tkinter.HORIZONTAL,length=200, from_=150, to=0,variable = uww,
                    command = get_slider, label='wrist', resolution=1)
uw.grid(column=4, row=39, columnspan=2)
uy = tkinter.Scale(mainFrame, orient=tkinter.HORIZONTAL,length=400, from_=-300, to=300,variable = uyy,
                    command = get_slider, label='y Achse', resolution=0.5)
uy.grid(column=2, row=40, columnspan=5)
uz= tkinter.Scale(mainFrame, orient=tkinter.VERTICAL,length=200, from_=180, to=0,variable = uzz,
                    command = get_slider, label='z Achse', resolution=0.5)
uz.grid(column=6, row=30,rowspan=10)

mBar = tkinter.Menu(mainFrame)
mSys = tkinter.Menu(mBar)
mSys.add_command(label="Parken", command = parken )
mSys.add_separator()
mSys.add_command(label="Beenden", command=destructor)
mBar.add_cascade(label="System", menu=mSys)
mainWin["menu"] = mBar

print("[INFO] Programmstart...")
mainWin.mainloop()


