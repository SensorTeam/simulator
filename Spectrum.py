import numpy as np

class Spectrum:
	def __init__(self, data=None):
		# Initialise public attributes
		self.data = data
		self.rgb = None

		# Initialise private attributes
		self.__matrix_rgb_from_xyz = None
		self.__matrix_xyz_from_rgb = None
		self.__matrix_xyz_colors = None
		self.__matrix_xyz_deltas = None
		self.__tristimulus_table = None
		self.__wavelength_start = None
		self.__wavelength_end = None

		# Initialisation methods
		self.__init__private()
		self.__init__public()

	def __init__private(self):
		# Initialise private attributes
		pass

	def __init__public(self):
		# Initialise public attributes
		if self.data is None:
			self.data = self.__render__empty_spectrum()
		self.rgb = self.__render__color()

	def __util__normalise(self, xyz):
		# Normalise XYZ color
		pass

	def __util__xyz(self, x, y, z=None):
		# Generate new XYZ color tuple
		pass

	def __util__wavelength_to_xyz(self, wavelength):
		# Converts wavelength to XYZ color
		pass

	def __render__empty_spectrum(self):
		# Renders an empty 2D array of wavelength vs intensity
		pass

	def __render__color(self):
		# Converts current spectrum into an RGB color
		pass