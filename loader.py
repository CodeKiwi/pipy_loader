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

programs = ['test.py', 'test2.py', 'myprogram.py']
selected = 0
# Make list of button value, text, and backlight color.
buttons = ( (LCD.SELECT, 'Select', (1,1,1)),
            (LCD.LEFT,   'Left'  , (1,0,0)),
            (LCD.UP,     'Up'    , (0,0,1)),
            (LCD.DOWN,   'Down'  , (0,1,0)),
            (LCD.RIGHT,  'Right' , (1,0,1)) )

lcd.clear()
lcd.message('Use buttons to\nselect program')

def update_display():
	line1 = programs[selected]
	if (selected == len(programs)):
		line2 = ''
	else:
		line2 = programs[selected+1]
	lcd.clear()	
	lcd.message(line1 + '\n' + line2)


print 'Press Ctrl-C to quit.'
while True:
	# Loop through each button and check if it is pressed.
	for button in buttons:
		if lcd.is_pressed(LCD.UP):
			if (selected > 0):
				selected=-1
		if lcd.is_pressed(LCD.DOWN):
			if selected < len(programs):
				selected=+1
		update_display()