#!/usr/bin/env python

# 
# Color picker
# 

import gtk.gdk

def pixel_at(x, y):
    rw = gtk.gdk.get_default_root_window()
    pixbuf = gtk.gdk.Pixbuf(gtk.gdk.COLORSPACE_RGB, False, 8, 1, 1)
    pixbuf = pixbuf.get_from_drawable(rw, rw.get_colormap(), x, y, 0, 0, 1, 1)
    return tuple(pixbuf.pixel_array[0, 0])

import gtk, pygtk

def topBorderColor(topMargin, numberOfSamples):
	increment = screenWidth() / (numberOfSamples + 1)
	outputColors = []
	avgR = 0
	avgG = 0
	avgB = 0

	for i in xrange(1, numberOfSamples + 1):
		offset = i * increment
		rgb = pixel_at(offset, topMargin)
		avgR += rgb[0]
		avgG += rgb[1]
		avgB += rgb[2]
		outputColors.append(rgb)
		# print str(i) + ": " + str(offset) + " " + str(topMargin) + " -> " + str(rgb)

	avgR /= numberOfSamples
	avgG /= numberOfSamples
	avgB /= numberOfSamples

	return (avgR, avgG, avgB)

def fullScreenColor(numberOfSamples):
	increment = screenHeight() / (numberOfSamples + 1)
	outputColors = []
	avgR = 0
	avgG = 0
	avgB = 0

	for i in xrange(1, numberOfSamples + 1):
		offset = i * increment
		rgb = topBorderColor(offset, numberOfSamples)
		avgR += rgb[0]
		avgG += rgb[1]
		avgB += rgb[2]
		outputColors.append(rgb)
		# print str(i) + ": " + str(offset) + " " + str(topMargin) + " -> " + str(rgb)

	avgR /= numberOfSamples
	avgG /= numberOfSamples
	avgB /= numberOfSamples

	return (avgR, avgG, avgB)


def screenWidth():
	width = gtk.Window().get_screen().get_width()
	return width

def screenHeight():
	width = gtk.Window().get_screen().get_height()
	return width

def mixColors(oldColor, newColor):
	newFactor = 0.15
	# outputColor = (0,0,0)
	# for rgb in xrange(0,2):
		# outputColor[rgb] = (1 - newFactor)*oldColor[rgb] + (newFactor) * newColor[rgb]
	# return outputColor
	return(	int((1 - newFactor)*oldColor[0] + (newFactor) * newColor[0]),
		int((1 - newFactor)*oldColor[1] + (newFactor) * newColor[1]),
		int((1 - newFactor)*oldColor[2] + (newFactor) * newColor[2]) )

		

# 
# DMX WebSocket
# 

from websocket import create_connection

def sendColor(r, g, b):
	address = "ws://127.0.0.1:9999"
	ws = create_connection(address)

	ws.send("CH|2|" + str(r)) #R
	ws.send("CH|3|" + str(g)) #G
	ws.send("CH|4|" + str(b)) #B

	ws.close()

def connectToWebsocket():
	address = "ws://127.0.0.1:9999"
	ws = create_connection(address)
	return ws

def sendColorToWebsocket(ws, color):
	ws.send("CH|2|" + str(color[0])) #R
	ws.send("CH|3|" + str(color[1])) #G
	ws.send("CH|4|" + str(color[2])) #B

def disconnectFromWebSocket(ws):
	ws.close()

# 
# Run loop
# 

import signal
import sys
from time import sleep

global continueRunning

def signal_handler(signal, frame):
        print('You pressed Ctrl+C!')
        global continueRunning
        continueRunning = False
        # sys.exit(0)


def runloop():
	signal.signal(signal.SIGINT, signal_handler)
	
	socket = connectToWebsocket()

	global continueRunning
	continueRunning = True

	topSamples = 10
	oldColor = fullScreenColor(topSamples)
	while continueRunning:
		# topMargin = screenHeight()/2
		# topColor = topBorderColor(topMargin, topSamples)
		newColor = fullScreenColor(topSamples)
		oldColor = mixColors(oldColor, newColor)
		# print (oldColor)
		sendColorToWebsocket(socket, oldColor)
		sleep(1.0 / 30)
		
	blackColor = (0,0,0)
	sendColorToWebsocket(socket, blackColor)

	disconnectFromWebSocket(socket)
	print "Disconnected"

# 
# Main
# 

def main():
    runloop()

if __name__ == "__main__":
    main()


