#!/usr/bin/env python3
import sys
from time import sleep
from uf.wrapper.swift_api import SwiftAPI
from uf.utils.log import *
    
zh = 60
x = 150
ya = -80
yb = 0
yc = 80

zspeed = 500
speed = 20000

swift = SwiftAPI() # {'hwid': 'USB VID:PID=2341:0042'}
sleep(2)
swift.set_position(x, ya, zh, speed = speed,  timeout = 20) 
swift.flush_cmd()
sleep(4)

def ab():
    a()
    heben()
    b()
    legen()
def ac():
    a()
    heben()
    c()
    legen()
def bc():
    b()
    heben()
    c()
    legen()
def ba():
    b()
    heben()
    a()
    legen()
def ca():
    c()
    heben()
    a()
    legen()
def cb():
    c()
    heben()
    b()
    legen()

def a():
    swift.set_position(x,ya, zh, speed = speed,  wait = True) 
def b():
    swift.set_position(x,yb, zh, speed = speed,  wait = True) 
def c():
    swift.set_position(x,yc, zh, speed = speed,  wait = True) 

def heben():
    r = zh
    while not swift.get_limit_switch():
        r = r - 1
        swift.set_position(z = r, speed = zspeed,timeout = 20)
    swift.set_pump(True)
    swift.set_position(z = zh, speed = speed)
    swift.flush_cmd()
def legen():
    r = zh
    while not swift.get_limit_switch():
        r = r - 1
        swift.set_position(z = r, speed = zspeed, wait = True)
    swift.set_pump(False)
    swift.set_position(z = zh, speed = speed, wait = True)
    swift.flush_cmd()
while True:
    ab()
    ac()
    bc()
    ab()
    ca()
    cb()
    ab()
    ac()
    bc()
    ba()
    ca()
    bc()
    ab()
    ac()
    bc()
    ab()
    ca()
    cb()
    ab()
    ca()
    bc()
    ba()
    ca()
    cb()
    ab()
    ac()
    bc()
    ab()
    ca()
    cb()
    ab()
    ac()
    bc()
    ba()
    ca()
    bc()
    ab()
    ac()
    bc()
    ba()
    cb()
    ca()
    ba()
    cb()
    ab()
    ac()
    bc()
    ba()
    cb()
    ca()
    ba()
    bc()
    ab()
    ac()
    bc()
    ab()
    ca()
    cb()
    ab()
    ac()
    bc()
    ba()
    ca()
    bc()
    ab()
    ac()
    bc()
    break
swift.set_position(x, yb, zh, speed = speed,  timeout = 20) 
