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

lcd.clear()
lcd.message('Use buttons to\nselect program')
time.sleep(1.0)

def update_display():
	line1 = programs[selected]
	if (selected == len(programs)-1):
		line2 = ''
	else:
		line2 = programs[selected+1]
	lcd.clear()	
	lcd.message(line1 + '\n' + line2)

def execute():
	lcd.clear()
	lcd.message('Executing\n'+programs[selected])

update_display()

print 'Press Ctrl-C to quit.'
while True:
	# Loop through each button and check if it is pressed.
	if lcd.is_pressed(LCD.UP):
		if (selected > 0):
			selected= selected-1
		update_display()
	if lcd.is_pressed(LCD.DOWN):
		if selected < len(programs)-1:
			selected+=1
		update_display()
	if lcd.is_pressed(LCD.SELECT):
		execute()
	time.sleep(0.1)