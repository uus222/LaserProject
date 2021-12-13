# -*- coding: utf-8 -*-
import time
import RPi.GPIO as GPIO
TRIG=23
ECHO=24
# 超音波センサー(HC-SR04)
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(TRIG,GPIO.OUT) # Trig
GPIO.setup(ECHO,GPIO.IN) # Echo
def getDistance():
    GPIO.output(TRIG, GPIO.LOW)
    GPIO.output(TRIG, GPIO.HIGH)
    time.sleep(0.00001)
    GPIO.output(TRIG, GPIO.LOW)
    while GPIO.input(ECHO) == 0:
        signaloff = time.time()
    while GPIO.input(ECHO) == 1:
        signalon = time.time()
    timepassed = signalon - signaloff
    return timepassed * 332 * 50 # cmに直す

"""
def main():
    while True:
        # 距離の測定
        distanceA = getDistance()
        print("{:.1f} cm".format(distanceA))
        time.sleep(1.0)
if __name__ == '__main__':
    main()

"""
