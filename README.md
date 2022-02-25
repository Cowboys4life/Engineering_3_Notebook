# Engineering_3_Notebook
My Engineering 3 stuff
# CircuitPython
This repository will actually serve as a aid to help you get started with your own template.  You should copy the raw form of this readme into your own, and use this template to write your own.  If you want to draw inspiration from other classmates, feel free to check [this directory of all students!](https://github.com/chssigma/Class_Accounts).
## Table of Contents
* [Table of Contents](#TableOfContents)
* [Hello_CircuitPython](#Hello_CircuitPython)
* [CircuitPython_Servo](#CircuitPython_Servo)
* [CircutPython_Distance_Sensor](#CircutPython_Distance_Sensor)
* [NextAssignmentGoesHere](#NextAssignment)
---

## Hello_CircuitPython

### Description & Code
Description goes here
It was a very easy assignment that didn't take long too do. It was a basic assignment. Mr. H told me I didnt have to make a wiring diagram, image and no evidence because the codes already in there.
```python
# made by Nick

import board
import neopixel
import time

dot = neopixel.NeoPixel(board.NEOPIXEL, 1)

while True:
    print("Make it blue!")
    dot.fill((0, 0, 255))
    time.sleep(.5)
    print("Make it yellow")
    dot.fill((255,255,0))
    time.sleep(.5)
    dot.brightness = 0.2

```


### Evidence
### Wiring

### Reflection
It was an easy assignment and it was not challenging at all.




## CircuitPython_Servo

### Description & Code
It was another basic assignment that was just tryna make a servo spin by coding.
```python
# made by Nick
"""CircuitPython Essentials Servo standard servo example"""
import time
import board
import pwmio
from adafruit_motor import servo

# create a PWMOut object on Pin A2.
pwm = pwmio.PWMOut(board.A2, duty_cycle=2 ** 15, frequency=50)

# Create a servo object, my_servo.
my_servo = servo.Servo(pwm)

while True:
    for angle in range(0, 180, 5):  # 0 - 180 degrees, 5 degrees at a time.
        my_servo.angle = angle
        time.sleep(0.05)
    for angle in range(180, 0, -5): # 180 - 0 degrees, 5 degrees at a time.
        my_servo.angle = angle
        time.sleep(0.05)

```

### Evidence
![image](https://github.com/nmckee78/CircuitPython/raw/main/Gif%20folder/ezgif.com-gif-maker%20(1).gif)

Image credit goes to [Nathanial McKee](https://github.com/nmckee78/CircuitPython)

### Wiring
![wiring](https://github.com/nmckee78/CircuitPython/raw/main/Pictures/Brilliant%20Vihelmo-Bigery.png)

Image credit goes to [Nathanial McKee](https://github.com/nmckee78/CircuitPython)

### Reflection
It was an basic assignment that was not challenging at all I think we did this last year but I can't really remember if we did or not.



## CircutPython_Distance_Sensor
It was a challenging assignment that took me some time to do. It was a struggle to get started but at the end I knew what I was doing.

```python
import time
import board
import adafruit_hcsr04
import neopixel
import simpleio

sonar = adafruit_hcsr04.HCSR04(trigger_pin=board.D5, echo_pin=board.D6)
dot = neopixel.NeoPixel(board.NEOPIXEL, 10, brightness=0.5)

r = 0
g = 0
b = 0


while True:


    try:
        distance = sonar.distance
        print((distance))

        if distance < 5:
            r = 255
            g = 0
            b = 0
        elif distance > 5 and distance < 20:
            r = simpleio.map_range(distance, 5, 20, 255, 0)
            b = simpleio.map_range(distance, 5, 20, 0, 255)
            g = 0
            r = int(r)
            g = int(g)
            b = int(b)
        elif distance > 20 and distance < 35:
            r = 0
            b = simpleio.map_range(distance, 20, 35, 255, 0)
            g = simpleio.map_range(distance, 20, 35, 0, 255)
            r = int(r)
            g = int(g)
            b = int(b)
        elif distance > 35:
            r = 0
            b = 0
            g = 255
            r = int(r)
            g = int(g)
            b = int(b)
        print(r, g, b)
        time.sleep(0.05)

    except RuntimeError:
        print("Retrying!")
        r = 0
        g = 0
        b = 255
        time.sleep(0.05)

    print(r, g, b)
    dot.fill((int(r), int(b), int(g)))
    time.sleep(0.05)

This code was made by Nathanial


```

### Evidence

![image](https://github.com/Cowboys4life/Engineering_3_Notebook/blob/main/Images/DistanceSensorGif.gif?raw=true)
It changes color based on how far the object is from the ultrasonic. There is a sensor that senses and changes the color based on how far the object is.
### Wiring

![image](https://github.com/Cowboys4life/Engineering_3_Notebook/blob/main/Images/DistanceSensor.png?raw=true)
 
### Reflection
It was a struggle at first to get started then i got the hang of it. I got confusing of the wiring on the metro because I didn't know where they went at first but Luka helped me and I appericate Lukas help.

## Robot arm


### Description
This project was supposed to be a nerf gun strapped onto two servos that made it a turret. The servos would allow the blaster to move vertically and horizontally. As for the blaster, our goal was to have the dart go at least 15 MPH. We had a base that had two servos on it, it was supposed to hold the blaster as it fires with a servo pulling the trigger. We tried to build a holster for the blaster that would attach to the servo so it could move.


### Code
  SPDX-FileCopyrightText: 2018 Mikey Sklar for Adafruit Industries

SPDX-License-Identifier: MIT

 Trinket Gemma Servo Control
 for Adafruit M0 boards

import board
import time
import pwmio
import simpleio
from adafruit_motor import servo
from analogio import AnalogIn

 servo pin for the M0 boards:
pwm = pwmio.PWMOut(board.A2, duty_cycle=2 ** 15, frequency=50)
pwm2 = pwmio.PWMOut(board.A3, duty_cycle=2 ** 15, frequency=50)

my_servo = servo.Servo(pwm)
my_servo2 = servo.Servo(pwm2)

angle = 0
angle2 = 0

potentiometer
trimpot = AnalogIn(board.A1)  # pot pin for servo control
trimpot2 = AnalogIn(board.A0)  # pot pin for servo control


while True:

    angle = simpleio.map_range(trimpot.value, 0, 65535, 0, 180)
    my_servo.angle = angle
    time.sleep(0.05)

    angle2 = simpleio.map_range(trimpot2.value, 0, 65535, 0, 180)
    my_servo2.angle = angle2
    print("Servo1 =", angle, "Servo2 =", angle2)
    time.sleep(0.05)
    
 ### Images 
https://docs.google.com/document/d/12MXsCBQTy6oUYVpjbeF3IZtGf592FxAnarE-sQJ-BMw/edit



### Reflection
We did not finish our project. We had a lot of obstacles that me and Luka had to face. We had no way of getting a blaster so Mr. H had to give us one a week before the project was due. Me and Luka also spent a lot of time doing the cad and the coding because it was challeging. Since we only had about 1 week with the blaster, it made the CAD much harder. We didn't have the exact measurements that we needed so we had to work on estimations. The coding part was really easy however and that was one of the first things we got done compleatley.
