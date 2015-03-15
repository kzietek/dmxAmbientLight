from ColorPickerGTK import ColorPickerGTK
import numpy

class ColorPickerAvg(ColorPickerGTK):

	def __init__(self, samples):
		ColorPickerGTK.__init__(self)
		self.numberOfSamples = samples

	def __del__(self):
		pass

	def getColor(self):
		colors = self.pickColors(self.numberOfSamples)
		color = self.avgColor(colors)
		return color

	def pickColors(self, numberOfSamples):
		offsetX = self.screenWidth() / (numberOfSamples + 1)
		offsetY = self.screenHeight() / (numberOfSamples + 1)

		colorList = []

		for y in xrange(1,numberOfSamples + 1):
			for x in xrange(1,numberOfSamples + 1):
				color = self.pixelAt(x*offsetX,y*offsetY)
				colorList.append(color)

		return colorList

	def avgColor(self, colors):
		rs, gs, bs = zip(*colors)
		r = numpy.mean(rs)
		g = numpy.mean(gs)
		b = numpy.mean(bs)
		return (r, g, b)