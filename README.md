## **CircuitPython**
This repository will actually serve as an aid to help you get started with your own template.  You should copy the raw form of this readme into your own, and use this template to write your own.  If you want to draw inspiration from other classmates, feel free to check [this directory of all students!](https://github.com/chssigma/Class_Accounts).
## Table of Contents
* [Table of Contents](#TableOfContents)
* [Hello_CircuitPython](#Hello_CircuitPython)
* [CircuitPython_Servo](#CircuitPython_Servo)
* [CircuitPython_LCD](#CircuitPython_LCD)
* [NextAssignmentGoesHere](#NextAssignment)
---

## **CircuitPython_Servo**

### Description & Code Snippets
The goal of this assignment was to wire a servo to move with capacitive touch from two wires. The overall idea was vague, but it wasn't to hard to find and modify two pieces of code from adafruit to achieve our goal.

```python
Code goes here
# SPDX-FileCopyrightText: 2018 Kattni Rembor for Adafruit Industries
#
# SPDX-License-Identifier: MIT

"""CircuitPython Essentials Capacitive Touch on two pins example. Does not work on Trinket M0!"""
import time
import board
import touchio
import pwmio
from adafruit_motor import servo

# create a PWMOut object on Pin A2.
pwm = pwmio.PWMOut(board.A2, duty_cycle=2 ** 15, frequency=50)

# Create a servo object, my_servo.
my_servo = servo.ContinuousServo(pwm)

touch_A4 = touchio.TouchIn(board.A4)  # Not a touch pin on Trinket M0!
touch_A5 = touchio.TouchIn(board.A5)  # Not a touch pin on Trinket M0!

while True:
    my_servo.throttle = 0.0
    while touch_A4.value:
        my_servo.throttle = 1.0
        time.sleep(.5)
    while touch_A5.value:
        my_servo.throttle = -1.0
        time.sleep(.5)
```
### Evidence
https://github.com/aflores4838/engr3/assets/143545493/77100b45-e5fe-4438-9368-e325c8324f8c
### Credit to Cristofer


### Wiring  
![](https://raw.githubusercontent.com/SempronChip/engr3/v1/images/133495354-0ef9219e-2658-4c7b-bef3-01cff6986baf.png)
Credit to Joshua

### Reflection
It wasn't too challanging to complete this assignment, especially when I realized that all I needed to do was combine two pieces of code that were availible online.









## **CircuitPython_DistanceSensor**

### Description & Code Snippets
The goal of this assignment is to make the neopixel change color based on the distances reported by the ultrasonic sensor. This assignment was accomplished by modifying the previous code we had from the neopixel to include the if statements and distance sensor.


### Evidence


https://github.com/aflores4838/engr3/assets/143545493/69736f93-8297-4300-9f50-98c4fe8e3260
### Credit to cristofer

```python
This is the code

# SPDX-FileCopyrightText: 2021 ladyada for Adafruit Industries
# SPDX-License-Identifier: MIT

import time
import board
import adafruit_hcsr04
import neopixel

NUMPIXELS = 1  # Update this to match the number of LEDs.
SPEED = 0.05  # Increase to slow down the rainbow. Decrease to speed it up.
BRIGHTNESS = 1.0  # A number between 0.0 and 1.0, where 0.0 is off, and 1.0 is max.
PIN = board.NEOPIXEL
pixels = neopixel.NeoPixel(PIN, NUMPIXELS, brightness=BRIGHTNESS, auto_write=False)
sonar = adafruit_hcsr04.HCSR04(trigger_pin=board.D5, echo_pin=board.D6)

while True:
    try:
        print((sonar.distance,))
        if sonar.distance < 5:
            for pixel in range(len(pixels)):  # pylint: disable=consider-using-enumerate
                pixels[pixel] = (255, 0,0)
                pixels.show()
        if sonar.distance > 5 and sonar.distance < 20:
            for pixel in range(len(pixels)):  # pylint: disable=consider-using-enumerate
                pixels[pixel] = (255-(sonar.distance - 5 / 15 * 255), 0, (sonar.distance - 5 / 15 * 255))
                pixels.show()
             
        if sonar.distance > 20 and sonar.distance < 35:
            for pixel in range(len(pixels)):  # pylint: disable=consider-using-enumerate
                pixels[pixel] = ( 0, (sonar.distance - 5 / 15 * 255), 255-(sonar.distance - 5 / 15 * 255))
                pixels.show()
        if sonar.distance > 35:
            for pixel in range(len(pixels)):  # pylint: disable=consider-using-enumerate
                pixels[pixel] = ( 0, 255, 0)
                pixels.show()   
    except RuntimeError:
        print("Retrying!")
    time.sleep(0.1)



```

### Evidence

### Wiring
https://github.com/SempronChip/engr3/raw/v1/images/134725601-72db0fcb-0d50-486c-aff5-9e0ec1772057.png?raw=true

### Reflection
This assignment was diffiecult at first because I wasnt to sure what to do but then I used my recouses and classmates and got it done.


## **CircuitPython_Motor_Control**

### Description & Code Snippets
For this assignment we had to wire up a 6v battery pack to this circuit with a motor and then wrie a Python code to make the motor speed up and slow down, based on input from a potentiometer overall not to hard to accomplish.

  

```python
Code goes here
import board
import analogio

motor = analogio.AnalogOut(board.A0)
pot = analogio.AnalogIn(board.A1)
while True:
    speed = pot.value
    motor.value = speed  
```

### Evidence
https://mail.google.com/mail/u/0?ui=2&ik=bfc48763e3&attid=0.1&permmsgid=msg-f:1780575898331908353&th=18b5e0587bb20901&view=att&disp=inline&realattid=f_lo3ame0k0

Credit to Cristofer

### Wiring
![credit to Joshua](https://github.com/SempronChip/engr3/raw/v1/images/IRLB8721%20Motor%20Control.png?raw=true)

### Reflection
At first it was difficult to make it work because of the wirring was the problem for me so I tried re-wire it from the beginning. With some help of my table mates I was able to accomplish it. 

## Onshape hanger

### Description & Code Snippets
The goal of this assignment was to follow the design documents to make a hanger with a mass matching the specified mass when it is the specified material.
### part link
[https://cvilleschools.onshape.com/documents/14b2ce2aac42fef6773cf68a/w/072cfd2284c6a5c82ebc9c3d/e/b55676c6b81bcc5e9b4ea96b?renderMode=0&uiState=653811dca78729041873fff3](https://cvilleschools.onshape.com/documents/08f60c35aff8a0db8329e41f/w/34101d5075d19eb7ecf31521/e/e48e665908f08ebbe2e37712?renderMode=0&uiState=65381b0336ad40095cdc1b52)

### Evidence
![Part Studio 1](https://github.com/cflores90/engr3/assets/143544973/2bae1356-4a1f-4d73-9f36-d7d668c7f8eb)

### Reflection
This assignmeant was was sort of tricky at first sense I haven't touched On shape in month but then everythin else was straight forward and I was able to get it done.



### Onshape swingarm

### Description
The goal of this assignment was to recreate the part detailed in the design documents. The difference being this assignment had variables for certain values which would need to be changed in the second step. These variables would also change the mass of part for the second step.

### Evidence
![Part Studio 1 (2)](https://github.com/aflores4838/engr3/assets/143545493/27c9d1b9-cc5e-4955-8b7d-e391651f0791)

### Part link
https://cvilleschools.onshape.com/documents/f416cd57d3da4a3276ffc422/w/7c5a2cb81afc23cbc0f6f6bc/e/11ef1853fe24bd099f27b35a?renderMode=0&uiState=65381cef34efc47fdfe844cf
### Reflection
This assignmeant was way harder then the previous one and I had a hard time at first with the measuremeants. But then I Mr, Miller posted a VIDEO on how to do it and so I used it to give me a boost on starting and then after that I was able to complete it with effiecent time.
