from tplight import LB130
import colorsys

class BulbOutput(object):

	def __init__(self, ip):
		self.bulb = LB130(ip)
		self.bulb.transition_period = 1 #1000/30
		self.lastHue = 0
		self.lastSaturation = 0
		self.lastBrightness = 0

	def __del__(self):
		pass

	def save(self):
		print("Device ID: " + self.bulb.device_id)
		print("Alias: " + self.bulb.alias)
		print("Wattage: " + str(self.bulb.wattage))
		pass

	def restore(self):
		pass

	def setColor(self, rgb):
		r = rgb[0] / 255.0
		g = rgb[1] / 255.0
		b = rgb[2] / 255.0
		hls = colorsys.rgb_to_hls(r, g, b)
		h = int(hls[0] * 360.0)
		l = int(hls[1] * 100.0)
		s = int(hls[2] * 100.0)
		print("H: %s, L: %s, S: %s" % (h,l,s))
		# if h != self.lastHue:
		# 	print(h)
		# 	self.bulb.hue = h
		# if s != self.lastSaturation:
		# 	self.bulb.saturation = s
		# if l != self.lastBrightness:
		# 	self.bulb.brightness = l
		self.bulb.setHSL(h,s,l)
		self.lastHue = h
		self.lastSaturation = s
		self.lastBrightness = l

	def intColor(self, color):
		return (int(color[0]*255),int(color[1]*255),int(color[2]*255))
