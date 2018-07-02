#!/usr/bin/env python3

import sys
from time import sleep
from uf.wrapper.swift_api import SwiftAPI
from uf.utils.log import *


swift = SwiftAPI() # {'hwid': 'USB VID:PID=2341:0042'}
sleep(2)
swift.set_position(150, 0, 150, speed = 20000,  wait = True) 
swift.flush_cmd()
sleep(2)
    

h = 150
zsp = 1500
ssp = 20000

def laden(x,y,w):
    swift.set_wrist(w, wait = True)
    swift.set_position(x,y, h, speed = ssp, wait = True) 
    r = h
    while not swift.get_limit_switch():
        r = r - 1
        swift.set_position(z = r, speed = zsp, wait = True)
        if r == 7:
           break
    swift.set_pump(True)
    swift.set_position(z = h, speed = ssp, wait = True)
    swift.flush_cmd()

def legen(x,y,w):
    swift.set_wrist(w, wait=True) # lang
    swift.set_position(x,y, h, speed = ssp, wait = True) 
    r = h
    while not swift.get_limit_switch():
        r = r - 1
        swift.set_position(z = r, speed = zsp, wait = True)
        if r == 7:
           break
    swift.set_pump(False)
    swift.set_position(z = h, speed = ssp, wait = True)
    swift.flush_cmd()


def ebene():
    laden(234,-180,50)
    legen(234,183,130)

    laden(234,-155,50)
    legen(234,133,116) 
      
    laden(234,-130,90)
    legen(256,160,60)

    laden(234,-109,90) 
    legen(206,160,60)  

for i in range(4):
    ebene()

swift.set_position(150, 0, 150, speed = 20000,  wait = True) 


