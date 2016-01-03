#!/usr/bin/env python

import usb.core
import usb.util
import time
import RPi.GPIO as GPIO


USB_VENDOR  = 0x0c40 # Rii
USB_PRODUCT = 0x7a11 # Mini Wireless Keyboard

USB_IF      = 0 # Interface
USB_TIMEOUT = 5 # Timeout in MS

BTN_LEFT  = 80
BTN_RIGHT = 79
BTN_DOWN  = 81
BTN_UP    = 82    
BTN_STOP  = 44 # Space 
BTN_EXIT  = 41 # ESC

LEFT  = 24
RIGHT = 25

GPIO.setmode(GPIO.BCM) 

GPIO.setup(LEFT, GPIO.OUT)
GPIO.setup(RIGHT, GPIO.OUT)

dev = usb.core.find(idVendor=USB_VENDOR, idProduct=USB_PRODUCT)
endpoint = dev[0][(0,0)][0]

if dev.is_kernel_driver_active(USB_IF) is True:
  dev.detach_kernel_driver(USB_IF)

usb.util.claim_interface(dev, USB_IF) 

while True:
    control = None
    try:    
        control = dev.read(endpoint.bEndpointAddress, endpoint.wMaxPacketSize, USB_TIMEOUT)
    except: 
        pass    

    if control != None:
        if BTN_DOWN in control:
            pass    

        elif BTN_UP in control:
            GPIO.output(LEFT, True)
            GPIO.output(RIGHT, True)

        elif BTN_LEFT in control:
          GPIO.output(LEFT, True)
          GPIO.output(RIGHT, False)

        elif BTN_RIGHT in control:
            GPIO.output(RIGHT, True)
            GPIO.output(LEFT, False)

        else:
            GPIO.output(LEFT, False)
            GPIO.output(RIGHT, False)

    time.sleep(0.02)
