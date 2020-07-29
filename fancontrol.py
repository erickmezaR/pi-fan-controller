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
        if  temp >= 45:
            fan.on()
        elif temp <= 40:
            fan.off()
        time.sleep(1)

if __name__ == '__main__':
    main()
