import colorsys
from Postprocessor import Postprocessor

class PostprocessOutputLimiter(Postprocessor):

	def __init__(self, previous, factor):
		Postprocessor.__init__(self)
		self.previousPostprocessor = previous
		self.factor = factor

	def __del__(self):
		pass

	def processColor(self, newColor):
		color = self.previousPostprocessor.processColor(newColor)
		return self.multiplyColor(color, self.factor)

	def multiplyColor(self, color, multiplier):
		return (int(color[0]*multiplier), int(color[1]*multiplier), int(color[2]*multiplier))