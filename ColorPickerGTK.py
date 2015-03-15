import gtk.gdk

class ColorPickerGTK(object):

	def __init__(self):
		self.rw = gtk.gdk.get_default_root_window()
		self.pixbuf = gtk.gdk.Pixbuf(gtk.gdk.COLORSPACE_RGB, False, 8, 1, 1)
		pass

	def __del__(self):
		pass

	def screenWidth(self):
		width = gtk.Window().get_screen().get_width()
		return width

	def screenHeight(self):
		height = gtk.Window().get_screen().get_height()
		return height

	def pixelAt(self, x, y):
		pixbuf = self.pixbuf.get_from_drawable(self.rw, self.rw.get_colormap(), x, y, 0, 0, 1, 1)
		return tuple(pixbuf.pixel_array[0, 0])

	def getColor(self):
		raise NotImplementedError("Please overload this abstract method")