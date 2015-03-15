import colorsys

class ColorPostprocessor(object):

	def __init__(self, initialColor, delayFactor):
		self.oldColor = initialColor
		self.newFactor = delayFactor

	def __del__(self):
		pass

	def processColor(self, newColor):
		self.oldColor = self.mixColors(self.oldColor, newColor, self.newFactor)
		return self.increaseSaturation(self.oldColor)

	def mixColors(self, oldColor, newColor, factor = 0.15):
		newFactor = factor
		return(	int((1 - newFactor)*oldColor[0] + (newFactor) * newColor[0]),
			int((1 - newFactor)*oldColor[1] + (newFactor) * newColor[1]),
			int((1 - newFactor)*oldColor[2] + (newFactor) * newColor[2]) )

	def increaseSaturation(self, color):
		floatColor = self.floatColor(color)
		hsv = colorsys.rgb_to_hsv(*floatColor)
		newValue = min(1, hsv[1]*2)
		newHsv = (hsv[0], newValue, hsv[2])
		rgb = colorsys.hsv_to_rgb(*newHsv)
		return self.intColor(rgb)

	def floatColor(self, color):
		multiplier = 1.0/255
		return (color[0]*multiplier, color[1]*multiplier, color[2]*multiplier)

	def intColor(self, color):
		return (int(color[0]*255),int(color[1]*255),int(color[2]*255))