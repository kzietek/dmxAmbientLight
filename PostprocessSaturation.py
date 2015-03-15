import colorsys
from Postprocessor import Postprocessor

class PostprocessSaturation(Postprocessor):

	def __init__(self, previous):
		Postprocessor.__init__(self)
		self.previousPostprocessor = previous

	def __del__(self):
		pass

	def processColor(self, newColor):
		color = self.previousPostprocessor.processColor(newColor)
		return self.increaseSaturation(color)

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