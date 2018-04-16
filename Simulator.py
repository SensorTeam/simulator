import cv2 as cv
import numpy as np
import colorsys as cs

class Simulator:
	def __init__(self, width, height, margin):
		self.width = width
		self.height = height
		self.margin = margin
		self.image = np.zeros((
			height,
			width,
			3
		), np.uint8)

		self.eye_size = None
		self.eye_span = None
		self.eye_coord_left = None
		self.eye_coord_right = None

	def _eyes(self, size, span, color):
		self.eye_size = size
		self.eye_span = span
		self.eye_coord_left = (
			(self.width // 2) - (span // 2),
			self.height - size - self.margin
		)
		self.eye_coord_right = (
			(self.width // 2) + (span // 2),
			self.height - size - self.margin
		)

		cv.circle(
			self.image,
			self.eye_coord_left,
			size,
			color,
			thickness=-1
		)

		cv.circle(
			self.image,
			self.eye_coord_left,
			size - 1,
			(255,255,255),
			thickness=-1
		)

		cv.circle(
			self.image,
			self.eye_coord_right,
			size,
			color,
			thickness=-1
		)

		cv.circle(
			self.image,
			self.eye_coord_right,
			size - 1,
			(255,255,255),
			thickness=-1
		)

	def _spectra(self):
		start = 0 + self.margin
		end = self.height - (2 * self.margin) - (2 * self.eye_size)

		for i in range(start, end):
			rgb = cs.hsv_to_rgb(i/(end - start), 1, 1)
			bgr = (
				int(rgb[2] * 255),
				int(rgb[1] * 255),
				int(rgb[0] * 255),
			)
			cv.circle(
				self.image,
				(self.eye_coord_left[0], i),
				self.eye_size,
				bgr,
				thickness=-1
			)
			cv.circle(
				self.image,
				(self.eye_coord_right[0], i),
				self.eye_size,
				bgr,
				thickness=-1
			)

		for i in range(start, end):
			cv.circle(
				self.image,
				(self.eye_coord_left[0], i),
				self.eye_size - 2,
				(255,255,255),
				thickness=-1
			)
			cv.circle(
				self.image,
				(self.eye_coord_right[0], i),
				self.eye_size - 2,
				(255,255,255),
				thickness=-1
			)

	def draw(self, size, span, color):
		self._eyes(size, span, color)
		self._spectra()

	def save(self, filename):
		cv.imwrite(filename, self.image)