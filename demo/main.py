#!/usr/bin/python
# -*- coding:utf-8 -*-


import time
import ADS1256
import RPi.GPIO as GPIO


try:
    ADC = ADS1256.ADS1256()
    ADC.ADS1256_init()

    while(1):

        print (ADS1256_GetChannalValue(0))


        print ("\33[9A")


except :
    GPIO.cleanup()
    print ("\r\nProgram end     ")
    exit()
