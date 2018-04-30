#!/usr/bin/env python

import signal
import sys
from time import sleep

from ColorPickerAvg import ColorPickerAvg
from ColorPickerExperimental import ColorPickerExperimental
from Postprocessor import Postprocessor
from PostprocessSmooth import PostprocessSmooth
from PostprocessSaturation import PostprocessSaturation
from PostprocessOutputLimiter import PostprocessOutputLimiter
from BulbOutput import BulbOutput

def signal_handler(signal, frame):
        global continueRunning
        continueRunning = False

def setupFilters(initialColor):
	postprocessor = Postprocessor()
	postprocessor = PostprocessSaturation(postprocessor, 3.0)
	# postprocessor = PostprocessSmooth(postprocessor, initialColor, 0.3)
	# postprocessor = PostprocessOutputLimiter(postprocessor, 0.3)
	return postprocessor

def runloop():
	signal.signal(signal.SIGINT, signal_handler)
	output = BulbOutput("192.168.0.200")
	output.save()
	nrOfSamplesToBeSquared = 5 #10
	newFactor = 0.2
	picker = ColorPickerAvg(nrOfSamplesToBeSquared)
	filters = setupFilters(picker.getColor())
	global continueRunning
	continueRunning = True
	while continueRunning:
		color = picker.getColor()
		color = filters.processColor(color)
		output.setColor(color)
		sleep(1.0/30.0)
	output.restore()

# 
# Main
# 

def main():
    runloop()

if __name__ == "__main__":
    main()


