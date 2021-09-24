# Engineering_3_Notebook
My Engineering 3 stuff
# CircuitPython
This repository will actually serve as a aid to help you get started with your own template.  You should copy the raw form of this readme into your own, and use this template to write your own.  If you want to draw inspiration from other classmates, feel free to check [this directory of all students!](https://github.com/chssigma/Class_Accounts).
## Table of Contents
* [Table of Contents](#TableOfContents)
* [Hello_CircuitPython](#Hello_CircuitPython)
* [CircuitPython_Servo](#CircuitPython_Servo)
* [CircuitPython_LCD](#CircuitPython_LCD)
* [NextAssignmentGoesHere](#NextAssignment)
---

## Hello_CircuitPython

### Description & Code
Description goes here
It was a very easy assignment that didn't take long too do. It was a basic assignment.
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

### Wiring
![image](https://cdn-learn.adafruit.com/assets/assets/000/053/104/medium640/circuitpython_MetroM4ExpressServo_bb.jpg?1524167660)

### Reflection
It was an basic assignment that was not challenging at all I think we did this last year but I can't really remember if we did or not.



## CircutPython Distance Sensor
It was a challenging assignment that took me some time to do. It was a struggle to get started but at the end I knew what I was doing.

```python
Code goes here

```

### Evidence

![image](https://github.com/Cowboys4life/Engineering_3_Notebook/blob/main/Images/DistanceSensorGif.gif?raw=true)

### Wiring

### Reflection





## NextAssignment

### Description & Code

```python
Code goes here

```

### Evidence

### Wiring

### Reflection
