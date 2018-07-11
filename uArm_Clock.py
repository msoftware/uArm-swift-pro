#!/usr/bin/env python3
# -*- coding: utf-8 -*-


import os
import sys
import time
from datetime import datetime
from uarm.wrapper import SwiftAPI
sys.path.append(os.path.join(os.path.dirname(__file__), '../../..'))

speed = 20000

swift2 = SwiftAPI(filters={'hwid': 'USB VID:PID=2341:0042'}) # Wischer
swift2.waiting_ready() 
swift1 = SwiftAPI(filters={'hwid': 'USB VID:PID=2341:0042'}) # Stift
swift1.waiting_ready() 

# Stift Setting
swift1.set_position(150, 0, 10, speed = speed, timeout = 20) 
swift1.set_wrist(90)
time.sleep(2)
swift1.set_gripper(True)
time.sleep(2)
swift1.set_position(150, 0, 20, speed = speed, timeout = 20) 
time.sleep(2) 

# Wischer Setting
swift2.set_position(150, 0, 0, speed = speed, timeout = 20) 
swift1.set_wrist(90)
time.sleep(2)
swift2.set_gripper(True)
swift2.set_position(110, 0, 20, speed = speed, timeout = 20) 
time.sleep(2)



def z1():
    swift1.set_position(z = -10, relative = True) 
    swift1.set_position(y = +9, relative = True) 
    swift1.set_position(x = +18, relative = True) 
    swift1.set_position(z = +10, relative = True) 
    swift1.set_position(y = -9,  relative = True) 
    swift1.set_position(z = -10, relative = True) 
    swift1.set_position(y = +18, relative = True) 
    swift1.set_position(z = +10, relative = True) 

def z2(): 
    swift1.set_position(z = -10, relative = True) 
    swift1.set_position(y = +18, relative = True) 
    swift1.set_position(x = +9, relative = True) 
    swift1.set_position(y = -18, relative = True) 
    swift1.set_position(x = +9, relative = True) 
    swift1.set_position(y = +18, relative = True) 
    swift1.set_position(z = +10, relative = True) 

def z3(): 
    swift1.set_position(z = -10, relative = True) 
    swift1.set_position(y = +18, relative = True) 
    swift1.set_position(x = +18, relative = True) 
    swift1.set_position(y = -18, relative = True) 
    swift1.set_position(z = +10, relative = True) 
    swift1.set_position(x = -9, relative = True) 
    swift1.set_position(z = -10, relative = True) 
    swift1.set_position(y = +18, relative = True) 
    swift1.set_position(z = +10, relative = True) 

def z4(): 
    swift1.set_position(z = -10, relative = True) 
    swift1.set_position(x = +9, relative = True) 
    swift1.set_position(y = +18, relative = True) 
    swift1.set_position(z = +10, relative = True) 
    swift1.set_position(x = -9, relative = True) 
    swift1.set_position(z = -10, relative = True) 
    swift1.set_position(x = +18, relative = True) 
    swift1.set_position(z = +10, relative = True) 

def z5(): 
    swift1.set_position(y = +18, relative = True) 
    swift1.set_position(z = -10, relative = True) 
    swift1.set_position(y = -18, relative = True) 
    swift1.set_position(x = +9, relative = True) 
    swift1.set_position(y = +18, relative = True) 
    swift1.set_position(x = +9, relative = True) 
    swift1.set_position(y = -18, relative = True) 
    swift1.set_position(z = +10, relative = True) 

def z6(): 
    swift1.set_position(y = +18, relative = True) 
    swift1.set_position(z = -10, relative = True) 
    swift1.set_position(y = -18, relative = True) 
    swift1.set_position(x = +18, relative = True) 
    swift1.set_position(y = +18, relative = True) 
    swift1.set_position(x = -9, relative = True) 
    swift1.set_position(y = -18, relative = True) 
    swift1.set_position(z = +10, relative = True) 

def z7(): 
    swift1.set_position(z = -10, relative = True) 
    swift1.set_position(y = +18, relative = True) 
    swift1.set_position(x = +18, relative = True) 
    swift1.set_position(z = +10, relative = True) 

def z8(): 
    swift1.set_position(z = -10, relative = True) 
    swift1.set_position(y = +18, relative = True) 
    swift1.set_position(x = +18, relative = True) 
    swift1.set_position(y = -18, relative = True) 
    swift1.set_position(x = -18, relative = True) 
    swift1.set_position(z = +10, relative = True) 
    swift1.set_position(x = +9, relative = True) 
    swift1.set_position(z = -10, relative = True) 
    swift1.set_position(y = +18, relative = True) 
    swift1.set_position(z = +10, relative = True) 

def z9(): 
    swift1.set_position(x = +9, relative = True) 
    swift1.set_position(y = +18, relative = True) 
    swift1.set_position(z = -10, relative = True) 
    swift1.set_position(y = -18, relative = True) 
    swift1.set_position(x = -9, relative = True) 
    swift1.set_position(y = +18, relative = True) 
    swift1.set_position(x = +18, relative = True) 
    swift1.set_position(y = -18, relative = True) 
    swift1.set_position(z = +10, relative = True) 

def z0(): 
    swift1.set_position(z = -10, relative = True) 
    swift1.set_position(y = +18, relative = True) 
    swift1.set_position(x = 18, relative = True) 
    swift1.set_position(y = -18, relative = True) 
    swift1.set_position(x = -18, relative = True) 
    swift1.set_position(z = +10, relative = True) 

def zpk():
    swift1.set_position(y = +9, relative = True) 
    swift1.set_position(x = +3, relative = True) 
    swift1.set_position(z = -10, relative = True) 
    swift1.set_position(x = +3, relative = True) 
    swift1.set_position(z = +10, relative = True) 
    swift1.set_position(x = +3, relative = True) 
    swift1.set_position(z = -10, relative = True) 
    swift1.set_position(x = +3, relative = True) 
    swift1.set_position(z = +10, relative = True) 




while True:
    now = datetime.now()
    zeit = now.strftime("%H:%M")
    swift1.set_position(150, 0, 20 ) 

    if zeit[0] == '1' :
        z1()
    elif zeit[0] == '2' :
        z2()
    elif zeit[0] == '3' :
        z3()
    elif zeit[0] == '4' :
        z4()
    elif zeit[0] == '5' :
        z5()
    elif zeit[0] == '6' :
        z6()
    elif zeit[0] == '7' :
        z7()
    elif zeit[0] == '8' :
        z8()
    elif zeit[0] == '9' :
        z9()
    swift1.set_position(150, 30, 20 ) 
        
    #
    if zeit[1] == '0' :
        z0()
    elif zeit[1] == '1' :
        z1()
    elif zeit[1] == '2' :
        z2()
    elif zeit[1] == '3' :
        z3()
    elif zeit[1] == '4' :
        z4()
    elif zeit[1] == '5' :
        z5()
    elif zeit[1] == '6' :
        z6()
    elif zeit[1] == '7' :
        z7()
    elif zeit[1] == '8' :
        z8()
    elif zeit[1] == '9' :
        z9()
    swift1.set_position(150, 50, 20 )     
    zpk()
    swift1.set_position(150, 70, 20 )    

    #
    if zeit[3] == '0' :
        z0()
    elif zeit[3] == '1' :
        z1()
    elif zeit[3] == '2' :
        z2()
    elif zeit[3] == '3' :
        z3()
    elif zeit[3] == '4' :
        z4()
    elif zeit[3] == '5' :
        z5()
    elif zeit[3] == '6' :
        z6()
    elif zeit[3] == '7' :
        z7()
    elif zeit[3] == '8' :
        z8()
    elif zeit[3] == '9' :
        z9()
    swift1.set_position(150, 100, 20 )    

    #
    if zeit[4] == '0' :
        z0()
    elif zeit[4] == '1' :
        z1()
    elif zeit[4] == '2' :
        z2()
    elif zeit[4] == '3' :
        z3()
    elif zeit[4] == '4' :
        z4()
    elif zeit[4] == '5' :
        z5()
    elif zeit[4] == '6' :
        z6()
    elif zeit[4] == '7' :
        z7()
    elif zeit[4] == '8' :
        z8()
    elif zeit[4] == '9':
        z9()
    swift1.set_position(150, 150, 40 ) 
   
    
    time.sleep(40)
    swift2.set_position(180, 0, 20, speed = speed, wait=True) 
    swift2.set_position(180, 0, 0, speed = 400, wait=True) 
    swift2.set_position(330, 0, 0, speed = 400, wait=True) 

    swift2.set_position(110, 0, 20, speed = speed, wait=True) 
    time.sleep(5)

