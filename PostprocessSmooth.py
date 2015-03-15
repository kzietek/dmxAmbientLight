from Postprocessor import Postprocessor

class PostprocessSmooth(Postprocessor):

	def __init__(self, previous, initialColor, delayFactor):
		Postprocessor.__init__(self)
		self.previousPostprocessor = previous
		self.oldColor = initialColor
		self.newFactor = delayFactor

	def __del__(self):
		pass

	def processColor(self, newColor):
		newColor = self.previousPostprocessor.processColor(newColor)
		self.oldColor = self.mixColors(self.oldColor, newColor, self.newFactor)
		return self.oldColor

	def mixColors(self, oldColor, newColor, factor = 0.15):
		newFactor = factor
		return(	int((1 - newFactor)*oldColor[0] + (newFactor) * newColor[0]),
			int((1 - newFactor)*oldColor[1] + (newFactor) * newColor[1]),
			int((1 - newFactor)*oldColor[2] + (newFactor) * newColor[2]) )