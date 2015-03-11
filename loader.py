#!/usr/bin/python
# Example using a character LCD plate.
# import math
import time

import Adafruit_CharLCD as LCD


# Initialize the LCD using the pins 
lcd = LCD.Adafruit_CharLCDPlate()

lcd.clear()
lcd.message('Robot program loader')
time.sleep(3.0)


# Make list of button value, text, and backlight color.
buttons = ( (LCD.SELECT, 'Select', (1,1,1)),
            (LCD.LEFT,   'Left'  , (1,0,0)),
            (LCD.UP,     'Up'    , (0,0,1)),
            (LCD.DOWN,   'Down'  , (0,1,0)),
            (LCD.RIGHT,  'Right' , (1,0,1)) )

lcd.clear()
lcd.message('Use buttons to\nselect program')
print 'Press Ctrl-C to quit.'
while True:
	# Loop through each button and check if it is pressed.
	for button in buttons:
		if lcd.is_pressed(button[0]):
			# Button is pressed, change the message and backlight.
			lcd.clear()
			lcd.message(button[1])
			lcd.set_color(button[2][0], button[2][1], button[2][2])