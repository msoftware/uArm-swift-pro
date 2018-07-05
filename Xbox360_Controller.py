#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# https://github.com/zeth/inputs

import inputs 
import os
import sys
from time import sleep
from uf.wrapper.swift_api import SwiftAPI
from uf.utils.log import *

w = 90
swift = SwiftAPI() # {'hwid': 'USB VID:PID=2341:0042'}
sleep(2)
swift.set_position(150, 0, 150, speed = 20000, timeout = 20 ) 
swift.set_wrist(90, wait=True) # lang
swift.flush_cmd() 
sleep(1)

# print(inputs.devices.gamepads)

while True:
   
    events = inputs.get_gamepad()
    for event in events:

        if event.code == 'ABS_X' and event.state < -20000:
           swift.set_position(y = -1, speed = 20000, relative = True, wait = True) 
           print('links')
        if event.code == 'ABS_X' and event.state > 10000:
           swift.set_position(y = +1, speed = 20000, relative = True, wait = True) 
           print('rechts')
        if event.code == 'ABS_Y' and event.state < -20000:
           swift.set_position(x = +1, speed = 20000, relative = True, wait = True) 
           print('unten')
        if event.code == 'ABS_Y' and event.state > 10000:
           swift.set_position(x = -1, speed = 20000, relative = True, wait = True) 
           print('oben')


        if event.code == 'ABS_RX' and event.state < -20000:
           w += 1
           swift.set_wrist(w, wait=True) # lang
           print('R links')
        if event.code == 'ABS_RX' and event.state > 10000:
           w -= 1
           swift.set_wrist(w, wait=True) 
           print('R rechts')

        if event.code == 'ABS_RY' and event.state < -20000:
          swift.set_position(z = -1, speed = 20000, relative = True, wait = True) 
          print('R unten')

        if event.code == 'ABS_RY' and event.state > 10000:
          swift.set_position(z = +1, speed = 20000, relative = True, wait = True) 
          print('R oben')


        if event.code == 'BTN_SOUTH' and event.state == 1:
            swift.set_pump(False)
            print('A Button')
        if event.code == 'BTN_WEST' and event.state == 1:
           swift.set_gripper(True, timeout = 10)
           print('X Button - Start Position')
        if event.code == 'BTN_EAST' and event.state == 1:
           swift.set_gripper(False, timeout = 10)
           print('B Button')
        if event.code == 'BTN_NORTH' and event.state == 1:
           swift.set_pump(True)
           print('Y Button')


        if event.code == 'BTN_START' and event.state == 1:
            print('Back Button')
        if event.code == 'BTN_SELECT' and event.state == 1:
            swift.set_position(150, 0, 150, speed = 20000, timeout = 20 ) 
            swift.set_wrist(90, wait=True) # lang
            print('Start Button')
