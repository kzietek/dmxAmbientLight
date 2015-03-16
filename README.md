# dmxAmbientLight
This little tool picks average color from your Gnome 3 desktop and sets it on a dmx lamp in realtime.

## A few words from the author ##
I was trying to force my dmx lamp to act like... ekhm... some company's TV. You know, the glow-behind one ;-).

I know... I know... This tool is in a little bit raw form. This was my first contact with Python. 

The problem is that my USB dmx controller ( KWMATIK kw-d-01 ) is a little tricky to control under Linux due to driver conflicts. QLCPlus handles it in perfect way but it needs a human to operate.

## Requirements ##
 - a dmx device supported by Q Light Controller Plus
 - a running QLCPlus with websockets enabled (run with parameter: qlcplus -w )
 - some python dependences

## Usage ##
 - Ensure your dmx hardware is working properly with QLCPlus
 - Note dmx absolute channels for R, G, B
 - Edit "DmxWebSocket.py" and place above channels in sendColor method
 - Run QLCPlus with websocket support (qlcplus -w)
 - Run "dmx-ambient-light.py"
 - Done! Now go and watch a video :-)

## Areas that may be improved ##
 - Proper configuration
 - Better color detection. Currently it reads 100 pixels from entire screen and averages channels independently. (Classes responsible: ColorPickerExperimental / ColorPickerAvg, both may be used interchangably. Experimental version is better for anime ^_^ )
 - Lag. Right now i'm mixing old color with new color to prevent flickering. It results in slight delay.
