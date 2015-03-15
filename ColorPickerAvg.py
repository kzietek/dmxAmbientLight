from ColorPickerGTK import ColorPickerGTK

class ColorPickerAvg(ColorPickerGTK):

	def __init__(self, samples):
		ColorPickerGTK.__init__(self)
		self.numberOfSamples = samples

	def __del__(self):
		pass

	def getColor(self):
		return self.avgGridColor(self.numberOfSamples)

	def avgLineColor(self, posY, numberOfSamples):
		increment = self.screenWidth() / (numberOfSamples + 1)
		outputColors = []
		avgR = 0
		avgG = 0
		avgB = 0

		for i in xrange(1, numberOfSamples + 1):
			offsetX = i * increment
			rgb = self.pixelAt(offsetX, posY)
			avgR += rgb[0]
			avgG += rgb[1]
			avgB += rgb[2]
			outputColors.append(rgb)
			# print str(i) + ": " + str(offsetX) + " " + str(posY) + " -> " + str(rgb)

		avgR /= numberOfSamples
		avgG /= numberOfSamples
		avgB /= numberOfSamples

		return (avgR, avgG, avgB)

	def avgGridColor(self, numberOfSamples):
		increment = self.screenHeight() / (numberOfSamples + 1)
		outputColors = []
		avgR = 0
		avgG = 0
		avgB = 0

		for i in xrange(1, numberOfSamples + 1):
			offset = i * increment
			rgb = self.avgLineColor(offset, numberOfSamples)
			avgR += rgb[0]
			avgG += rgb[1]
			avgB += rgb[2]
			outputColors.append(rgb)
			# print str(i) + ": " + str(offset) + " " + str(topMargin) + " -> " + str(rgb)

		avgR /= numberOfSamples
		avgG /= numberOfSamples
		avgB /= numberOfSamples

		return (avgR, avgG, avgB)