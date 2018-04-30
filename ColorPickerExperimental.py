from ColorPickerGTK import ColorPickerGTK
import numpy
import struct
import scipy
import scipy.misc
import scipy.cluster

from PIL import Image

class ColorPickerExperimental(ColorPickerGTK):

	def __init__(self, samples):
		ColorPickerGTK.__init__(self)
		self.numberOfSamples = samples

	def __del__(self):
		pass

	def getColor(self):
		colors = self.pickColors(self.numberOfSamples)
		color = self.medianColor(colors)
		return color

	def medianColor(self, colors):
		rs, gs, bs = zip(*colors)
		r = numpy.median(rs)
		g = numpy.median(gs)
		b = numpy.median(bs)
		return (r, g, b)

	def getByClustering(self, colors):
		ar = numpy.array(colors)
		NUM_CLUSTERS = 3
		codes, dist = scipy.cluster.vq.kmeans(ar, NUM_CLUSTERS)
		vecs, dist = scipy.cluster.vq.vq(ar, codes)         # assign codes
		counts, bins = scipy.histogram(vecs, len(codes))    # count occurrences
		index_max = scipy.argmax(counts)                    # find most frequent
		peak = codes[index_max]
		colour = ''.join(chr(c) for c in peak).encode('hex')
		print 'most frequent is %s (#%s)' % (peak, colour)
		return (int(peak[0]),int(peak[1]),int(peak[2]))

	# def most_frequent_colour(self, image):
	#     w, h = (self.numberOfSamples, self.numberOfSamples)
	#     pixels = image.getcolors(w * h)

	#     most_frequent_pixel = pixels[0]

	#     for count, colour in pixels:
	#         if count > most_frequent_pixel[0]:
	#             most_frequent_pixel = (count, colour)

	#     compare("Most Common", image, most_frequent_pixel[1])

	#     return most_frequent_pixel

	def pickColors(self, numberOfSamples):
		offsetX = self.screenWidth() / (numberOfSamples + 1)
		offsetY = self.screenHeight() / (numberOfSamples + 1)

		colorList = []

		for y in xrange(1,numberOfSamples + 1):
			for x in xrange(1,numberOfSamples + 1):
				color = self.pixelAt(x*offsetX,y*offsetY)
				colorList.append(list(color))

		return colorList

	def avgColor(self, colors):
		rs, gs, bs = zip(*colors)
		r = numpy.mean(rs)
		g = numpy.mean(gs)
		b = numpy.mean(bs)
		return (r, g, b)