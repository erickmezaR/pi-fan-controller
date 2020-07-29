#!/usr/bin/env python3

import sys
import os
import time
from gpiozero import PWMLED
from vcgencmd import Vcgencmd

def main():
    fan = PWMLED(18)
    while True:
        vcgm = Vcgencmd()
        temp = vcgm.measure_temp()
        print(temp)
        if  temp >= 45:
            fan.on()
            print("fan.on()")
        elif temp <= 40:
            fan.off()
            print("fan.off()")
        time.sleep(1)

if __name__ == '__main__':
    main()
    
