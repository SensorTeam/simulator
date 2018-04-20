import math
import cv2 as cv
import numpy as np
import colorsys as cs

class Simulator:
	def __init__(self):
		# Initialises the Simulator object
		self.__image_filename = None
		self.__image_margin = None
		self.__image_height = None
		self.__image_width = None

		self.__pupil_distance_inter = None
		self.__pupil_distance = None
		self.__pupil_size = None

		self.__coord_right = None
		self.__coord_left = None

		self.__spectrum = None

		self.__output = None
		self.__image = None

	def render(self, parameters):
		# Main render method
		self.__set_params(parameters)

		self.__image = np.zeros((
			self.__image_height,
			self.__image_width,
			3
		), np.uint8)

		self.__coord_left = (
			(self.__image_width // 2) - (self.__pupil_distance_inter // 2),
			self.__image_height - self.__pupil_size - self.__image_margin
		)
		self.__coord_right = (
			(self.__image_width // 2) + (self.__pupil_distance_inter // 2),
			self.__image_height - self.__pupil_size - self.__image_margin
		)

		self.__render_spectra()
		self.__render_eyes()
		self.__export()

	def __set_params(self, parameters):
		# Sets simulation parameters
		self.__image_filename = parameters['image-filename']
		self.__image_margin = parameters['image-margin']
		self.__image_height = parameters['image-height']
		self.__image_width = parameters['image-width']

		self.__pupil_distance_inter = parameters['pupil-distance-inter']
		self.__pupil_distance = parameters['pupil-distance']
		self.__pupil_size = parameters['pupil-size']

		self.__spectrum = parameters['spectrum']

	def __render_spectra(self):
		# Draws the spectrum
		start = self.__image_margin
		end = self.__image_height - (2 * self.__image_margin) - (2 * self.__pupil_size)
		length = (end - start)

		# Draw rainbow according to input spectrum
		for i in range(start, end):
			count = i - start
			fraction = count/length
			index = int(len(self.__spectrum.data) * fraction)
			value = self.__spectrum.data[index][1]
			hue = -(fraction * (270/360)) + (270/360)
			rgb = cs.hsv_to_rgb(hue, 1, value)
			bgr = (
				int(rgb[2] * 255),
				int(rgb[1] * 255),
				int(rgb[0] * 255),
			)
			cv.line(
				self.__image,
				(self.__coord_left[0] - self.__pupil_size, i),
				(self.__coord_left[0] + self.__pupil_size, i),
				bgr,
				1
			)
			cv.line(
				self.__image,
				(self.__coord_right[0] - self.__pupil_size, i),
				(self.__coord_right[0] + self.__pupil_size, i),
				bgr,
				1
			)

	def __render_eyes(self):
		# Draws eyes
		color = self.__spectrum.rgb
		for i in range(self.__pupil_size, 1, -1):
			# Find light intensity
			s = self.__intensity(i/self.__pupil_size)
			hsv = cs.rgb_to_hsv(color[0], color[1], color[2])
			rgb = cs.hsv_to_rgb(hsv[0], 1 - s, hsv[2])
			bgr = (
				int(rgb[2] * 255),
				int(rgb[1] * 255),
				int(rgb[0] * 255),
			)

			# Draw left eye
			cv.circle(
				self.__image,
				self.__coord_left,
				i,
				bgr,
				thickness=-1
			)

			# Draw right eye
			cv.circle(
				self.__image,
				self.__coord_right,
				i,
				bgr,
				thickness=-1
			)

	def __intensity(self, x):
		# Simplified Gaussian function for color intensity
		exponent = -(x ** 2)
		return math.exp(exponent)

	def __export(self):
		# Writes output to an image file
		cv.imwrite(self.__image_filename, self.__image)