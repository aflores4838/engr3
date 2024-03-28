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
The goal of this assignment was to wire a servo to move with capacitive touch from two wires. The overall idea was incomplete, but it wasn't to hard to find and modify two pieces of code from adafruit to achieve our goal.

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
### Credit to Cristofer Flores Puentes


### Wiring  
![](https://raw.githubusercontent.com/SempronChip/engr3/v1/images/133495354-0ef9219e-2658-4c7b-bef3-01cff6986baf.png)
Credit to Joshua

### Reflection
This assignment wasn't too challenging to complete, especially when I realized I could just search it up and it ended up to be just two codes combined.









## **CircuitPython_DistanceSensor**

### Description & Code Snippets
The goal of this assignment is to make the neopixel change color based on the distances reported by the ultrasonic sensor. This assignment was accomplished by modifying the previous code we had from the neopixel to include the if statements and distance sensor.


### Evidence


https://github.com/aflores4838/engr3/assets/143545493/69736f93-8297-4300-9f50-98c4fe8e3260
### Credit to cristofer flores puentes

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

### Wiring
![](https://raw.githubusercontent.com/SempronChip/engr3/v1/images/134725601-72db0fcb-0d50-486c-aff5-9e0ec1772057.png)

### Reflection
This assignment was difficult at first because I wasnt to sure what to do but then I used my recourses and classmates to help me get abetter idea of what the main idea for this assinment was telling to do.


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

https://github.com/aflores4838/engr3/assets/143545493/d161df92-8076-488a-b1c3-02047411e97e



Credit to Cristofer

### Wiring
![credit to Joshua](https://raw.githubusercontent.com/SempronChip/engr3/v1/images/134725601-72db0fcb-0d50-486c-aff5-9e0ec1772057.png)

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
## Rotary Encoder & LCD
### Description and Code
For this assignment we had to use an rotary encoder and LCD to function, simillar to a traffic light. 
```python
Code goes here
# Rotary Encodare light thingksf;ja             # [lines 1-7] Import and set up neccesary libraries
import time
import rotaryio
import neopixel
import board
from lcd import LCD
from i2c_pcf8574_interface import I2CPCF8574Interface
from digitalio import DigitalInOut, Direction, Pull


encoder = rotaryio.IncrementalEncoder(board.D4, board.D3) # [lines 9-24] Start all Variables and define INs and OUTs
last_position = 0
btn = DigitalInOut(board.D2)
btn.direction = Direction.INPUT
btn.pull = Pull.UP
state = 0
Button = 1
led = neopixel.NeoPixel(board.NEOPIXEL, 1)
led.brightness = .3
i2c = board.I2C()
lcd = LCD(I2CPCF8574Interface(i2c, 0x27), num_rows=2, num_cols=16)





while True:                #[lines 27-38] Set up varible for encoder, limit it to >0 and <3
    position = encoder.position
    if position != last_position:
        state = position % 3
        if state == 0:     #[lines 39-47] Print to LCD based on Encoder Var
            lcd.clear()
            lcd.set_cursor_pos(0, 0) # [39
            lcd.print("Don't stop")
        elif state == 1:
            lcd.clear()
            lcd.set_cursor_pos(0, 0)
            lcd.print("Speed up")
        elif state == 2:
            lcd.clear()
            lcd.set_cursor_pos(0, 0)
            lcd.print("Slam on brakes")
    if btn.value == 0 and Button == 1: #[lines 48-63] If the button is pressed make the Encoder Var match the lights.
        print("buttion")
        if state == 0: 
            print('g')
            led[0] = (0, 255, 0)
        elif state == 1:
            print('y')
            led[0] = (255, 234, 0)
        elif state == 2:
            print('r')
            led[0] = (250, 0, 0)
        Button = 0       #[lines 64-68] Resets and delay
    if btn.value == 1:
        time.sleep(.1)
        Button = 1
    last_position = position
```
Credit to Joshua
### Evidence 
VIDEO SOOONNN
### Wirring 
![cd325ae495e7848aa78f0d50b4f0efc9345c3370_2_690x408](https://github.com/aflores4838/engr3/assets/143545493/5b9645d1-793d-4220-993b-116d5e235277)
### Reflection 
For this assignment I was a bit stuck at first it didn't want to turn on so I tried doing some reasearch on what I could. But, honestley I didn't find anything so, I asked one of my classmate if they could help me. We then figured out what was the issue one of my wire wasn't pluged in the right spot so, we then we attempted to started up again and then it started working and I got it done. 
## Stepper Motor and Limit Switch 
### Description and Code
For this assignmeant we had to make the motor hit the switch and once it hits, it will turn the other way.
``` python
import asyncio
import board
import keypad
import time
import digitalio
from adafruit_motor import stepper 

DELAY = 0.01
STEPS = 100

coils = (
    digitalio.DigitalInOut(board.D9),  # A1
    digitalio.DigitalInOut(board.D10), # A2
    digitalio.DigitalInOut(board.D11), # B1
    digitalio.DigitalInOut(board.D12), # B2
)

for coil in coils:
    coil.direction = digitalio.Direction.OUTPUT

motor = stepper.StepperMotor(coils[0], coils[1], coils[2], coils[3], microsteps=None)

async def catch_pin_transitions(pin):
    with keypad.Keys((pin,), value_when_pressed=False) as keys:
        while True:
            event = keys.events.get()
            if event:
                if event.pressed:
                    print("Limit Switch was pressed.")
                    for step in range(STEPS):
                        motor.onestep(direction=stepper.BACKWARD, style=stepper.DOUBLE)
                        time.sleep(DELAY)
                elif event.released:
                    print("Limit Switch was released.")
            await asyncio.sleep(0)

async def run_motor():
    while(True):
        for step in range(STEPS):
            motor.onestep(style=stepper.DOUBLE)
            time.sleep(DELAY)
        await asyncio.sleep(0)

async def main():
    interrupt_task = asyncio.create_task(catch_pin_transitions(board.D2))
    motor_task = asyncio.create_task(run_motor())
    await asyncio.gather(interrupt_task, motor_task)
asyncio.run(main())
```

### Evidence



![Stepper Motor and limit switch](https://github.com/aflores4838/engr3/assets/143545493/79b686dc-f9af-4426-9adc-1f616e817a98)

## Onshape_Assignment_Multi-Part_Cylinder

### Assignment Description

In this assignment I followed instructions to create multiple parts that will fit all together in a specific way. After that I had to change some parts of it to test if I had created the parts in a good presentable way.

### Evidence

![image](https://github.com/lwimber39/engr3/assets/143545399/a6c20807-ff55-435d-bf5b-df98b557ac43)

![image](https://github.com/lwimber39/engr3/assets/143545399/3bad8ec6-6ad7-4953-ba16-aca97f4a3ea0)

### Part Link 



### Reflection

This assignment was somewhat tricky because it has multiple parts however most of them were pretty much simple. One obstacle that seemed difficult was making the bolts always stick out from the top and bottom but then all it took was using an up to face extrude and two ofsets (Leo helped me figure it out) . One thing that I missed was at the end where the cylinder switched materials.
&nbsp;

## Onshape_Assignment_Single-Part_V-Block

### Assignment Description

In this assignment I had to create a V-block and edit some dimensions to see if I made it correct.

### Evidence

![image](https://github.com/lwimber39/engr3/assets/143545399/d36213ba-8a8b-41c2-8fca-ae3e6824c295)

![image](https://github.com/lwimber39/engr3/assets/143545399/7d5d241b-5438-4962-9ede-57fcee3804d2)

### Part Link 


### Reflection

This assignment was really not very hard considering I sort have already done this last year with Mr, Garcia. I did learn something from it thoguh, is that you can make versions for anything that has more than one question where you have to change variables, so you can easily go back if anything goes wrong.

&nbsp;

## Onshape_CAD_Challenge_Alignment_Plate

### Assignment Description

In this assignment I used the CAD challenges Onshape app to use a diagram to create an alignment plate. It was also timed so it put more pressure on me to things right with the lease aount of mistakes. To complete the part and the many features and compared to how others and they performed.

### Evidence

![image](https://github.com/lwimber39/engr3/assets/143545399/7c2b8b65-f264-4b2a-b6c9-c90187ed8f72)

![image](https://github.com/lwimber39/engr3/assets/143545399/65268799-301c-450d-9bc0-b37d5451b452)


### Part Link 


### Reflection

This assignment was pretty simple since it only took 3 features and I completed it in in like 10 minutes even while looking over my work. I didn't really learn much of it since I only used a sketch, extrude, and last but not least chamfer, but I don't use chamfers much so some practice could help me improve. 

&nbsp;

## Onshape_Assignment_Multi-Part_Mic_Stand

### Assignment Description

In this assignment we had to create a mic stand with multiple versions and an assembly to insert a screw.

### Evidence

![image](https://github.com/lwimber39/engr3/assets/143545399/446f3657-da8f-498c-8fe4-7cadae880deb)


![image](https://github.com/lwimber39/engr3/assets/143545399/ad2af5ce-b3e0-4aa4-9fb9-6a4970c7e3c7)


### Part Link 



### Reflection

This assignment was somewhat difficult because it contained multiple parts. I did come across some issues, when trying to make a curve in the mic holder at the same thickness all the way. To solve this I had to subtract the thickness you want and then from that the outer curve's radius to get the inner curve's radius. (Leo helped me with this)

&nbsp;

## Onshape_Assignment_Assemblies_Locking_Pliers

### Assignment Description

In this assignment we were told to put together pliers in an assemblies with multiple orientations to gather measurements.

### Evidence

![image](https://github.com/lwimber39/engr3/assets/143545399/d237dd6b-61ad-4c78-b25e-b59c906599ba)


![image](https://github.com/lwimber39/engr3/assets/143545399/ef0f0ddf-3eaf-4cc1-ac5b-eaed99507bb6)

### Part Link 


### Reflection

This assignment was pretty easy because it was only in an assembly thing. It was a little difficult because I am not super used to these types of mates and it was sort of difficult to get to understand. One issue was the parallel mate because some things can be parallel in multiple positions and basically at first it messed up my whole assembly and made it disonect so I had to figure it out but after some tests and switches I was able to get it done.

&nbsp;

## CircuitPython_Photointerrupter

### Description & Code Snippets
  The goal of this assignment was to get an LCD screen to display the number of times the photointerrupter has been interrupted and it recieves it every few seconds.

```python
    import time
import digitalio
from lcd.lcd import LCD
from lcd.i2c_pcf8574_interface import I2CPCF8574Interface
import board

photointerrupter = digitalio.DigitalInOut(board.D2)
photointerrupter.direction = digitalio.Direction.INPUT
photointerrupter.pull = digitalio.Pull.UP
photointerrupter_state = None
interrupt_counter = 0

lcd = LCD(I2CPCF8574Interface(board.I2C(), 0x27), num_rows=2, num_cols=16)
lcd.set_cursor_pos(0,0)
lcd.print("The number of interrupts is: ")
now = time.monotonic()

while True:
    if not photointerrupter.value and photointerrupter_state is None:
        photointerrupter_state = "interrupted"
    if photointerrupter.value and photointerrupter_state == "interrupted":
        photointerrupter_state = None
        interrupt_counter = interrupt_counter+1
    if (now + 4) < time.monotonic():
        lcd.set_cursor_pos(1,13)
        lcd.print(str(interrupt_counter))
        now = time.monotonic()

```



### Evidence!
![photointvid-ezgif com-video-to-gif-converter](https://github.com/lwimber39/engr3/assets/143545399/9bf5ee6c-b01d-4a7d-b8a6-8cb07a35d6a8)

Credit to Leo W

### Wiring
Here is a wiring diagram of my circuit.
![image](https://github.com/lwimber39/engr3/assets/143545399/cf3f8a93-0c8d-4979-9c3e-c341e1b0a052)

### Reflection
This assignment was sort of easy becuse I was able to find an exanmple of how to do it online. I didn't need much help for this but something to remember for next time is to always check that your LCD setup uses the correct code because it can be different for other LCDs.

## CircuitPython_Stepper_Motor

### Description & Code Snippets
  The goal of this assignment was to get a stepper motor to rotate continuously and rotate 180 degrees the other way. When a limit switch is pressed.

```python
import asyncio
import board
import keypad
import time
import digitalio
from adafruit_motor import stepper

DELAY = 0.01
STEPS = 100

coils = (
    digitalio.DigitalInOut(board.D9),  # A1
    digitalio.DigitalInOut(board.D10), # A2
    digitalio.DigitalInOut(board.D11), # B1
    digitalio.DigitalInOut(board.D12), # B2
)

for coil in coils:
    coil.direction = digitalio.Direction.OUTPUT

motor = stepper.StepperMotor(coils[0], coils[1], coils[2], coils[3], microsteps=None)

async def catch_pin_transitions(pin):
    with keypad.Keys((pin,), value_when_pressed=False) as keys:
        while True:
            event = keys.events.get()
            if event:
                if event.pressed:
                    print("Limit Switch was pressed.")
                    for step in range(STEPS):
                        motor.onestep(direction=stepper.BACKWARD, style=stepper.DOUBLE)
                        time.sleep(DELAY)
                elif event.released:
                    print("Limit Switch was released.")
            await asyncio.sleep(0)

async def run_motor():
    while(True):
        for step in range(STEPS):
            motor.onestep(style=stepper.DOUBLE)
            time.sleep(DELAY)
        await asyncio.sleep(0)

async def main():
    interrupt_task = asyncio.create_task(catch_pin_transitions(board.D2))
    motor_task = asyncio.create_task(run_motor())
    await asyncio.gather(interrupt_task, motor_task)
asyncio.run(main())

```

[](https://github.com/lwimber39/engr3/blob/main/StepperMotot.py)


### Evidence!
![ezgif com-video-to-gif-converter (1)](https://github.com/lwimber39/engr3/assets/143545399/a7f77728-8639-44a0-951f-edbff7e5a8e2)
Credit to Leo W
### Wiring

![image](https://github.com/lwimber39/engr3/assets/143545399/bae6c473-334d-4780-9a9d-6e72ac2bb94f)

### Reflection
This assignment was a litte tricky because I hadn't used a stepper motor. I used the slides and asked for some guidness and asked for help form my companions in my class when I needed it. The main thing I strugled with was figuring out how to make the motor move in different directions and continuously but everything else was pretty easy from there.

## CircuitPython_Infared_Sensor

### Description & Code Snippets
  The goal of this assignment was to get the neopixel to be either red or greem depending on whether the sensor is blocked or not respectively.


```python

ir_sensor = digitalio.DigitalInOut(board.D2)
ir_sensor.direction = digitalio.Direction.INPUT 
ir_sensor.pull = digitalio.Pull.UP 

led = neopixel.NeoPixel(board.NEOPIXEL, 1)
led.brightness = 0.3

while True:
    if ir_sensor.value:
        print("yes")
        led[0] = (0, 255, 0)
    if not ir_sensor.value:
        print("no")
        led[0] = (255, 0, 0))

```


### Evidence!
![ezgif com-video-to-gif-converter (2)](https://github.com/lwimber39/engr3/assets/143545399/c63ba1a3-61a3-4299-aa5d-97ac95190aae)
credit to Leo W


### Wiring
Here is a wiring diagram of my circuit.
![image](https://github.com/lwimber39/engr3/assets/143545399/7a4671f8-4cf6-4e1c-9d9d-8aa47dcd6ac6)


### Reflection
This assignment was really easy because it was just changing based on an input. I didn't need any help for this and the only troubling thing was accidentally switching what I from on and off.

## Onshape_Assignment_Robot_Gripper

### Assignment Description

In this assignment we had to create and assemble a functioning robot gripper.

### Evidence

![image](https://github.com/lwimber39/engr3/assets/143545399/82901f29-024f-4af2-8506-1b50342816f3)


![ezgif com-video-to-gif-converter (3)](https://github.com/lwimber39/engr3/assets/143545399/a638096a-7e9a-4a79-8efe-8290b33feef8)


### Part Link 



### Reflection

This assignment was somewhat tricky but still surprisingly pretty fun. I was able to use mt previouse knowledge to crsate this arm thingy and was pretty cool to see the results at the end. The sort of issue I ran too was when it was time to asemble it all but, I was able to figure it out and get it done.

&nbsp;

