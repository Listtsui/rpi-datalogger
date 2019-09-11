#!/usr/bin/python
# -*- coding:utf-8 -*-


import time
import ADS1256
import RPi.GPIO as GPIO


try:
    ADC = ADS1256.ADS1256()
    ADC.ADS1256_init()

    while(1):

        print (ADC.ADS1256_GetChannalValue(0)*5.0/0x7fffff)
        print (ADC.ADS1256_GetChannalValue(1)*5.0/0x7fffff)

        print ("\33[1A")


except :
    GPIO.cleanup()
    print ("\r\nProgram end     ")
    exit()
