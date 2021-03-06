#!/usr/bin/env python

import signal
import sys
from time import sleep

from ColorPickerAvg import ColorPickerAvg
from ColorPickerExperimental import ColorPickerExperimental
from DmxWebSocket import DmxWebSocket
from Postprocessor import Postprocessor
from PostprocessSmooth import PostprocessSmooth
from PostprocessSaturation import PostprocessSaturation
from PostprocessOutputLimiter import PostprocessOutputLimiter

def signal_handler(signal, frame):
        global continueRunning
        continueRunning = False

def setupFilters(initialColor):
	postprocessor = Postprocessor()
	postprocessor = PostprocessSaturation(postprocessor, 1.0)
	# postprocessor = PostprocessSmooth(postprocessor, initialColor, 0.3)
	# postprocessor = PostprocessOutputLimiter(postprocessor, 0.3)
	return postprocessor

def runloop():
	signal.signal(signal.SIGINT, signal_handler)
	socket = DmxWebSocket()
	nrOfSamplesToBeSquared = 10
	newFactor = 0.2
	picker = ColorPickerExperimental(nrOfSamplesToBeSquared)
	filters = setupFilters(picker.getColor())
	global continueRunning
	continueRunning = True
	while continueRunning:
		color = picker.getColor()
		color = filters.processColor(color)
		socket.sendColor(color)
		sleep(1.0 / 30)
	blackColor = (0,0,0)
	socket.sendColor(blackColor)

# 
# Main
# 

def main():
    runloop()

if __name__ == "__main__":
    main()


