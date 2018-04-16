import cv2 as cv
import numpy as np

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

	def draw_eyes(self, size, span, color):
		coord_left = (
			(self.width // 2) - (span // 2),
			self.height - size - self.margin
		)

		cv.circle(
			self.image,
			coord_left,
			size,
			color,
			thickness=-1
		)

		cv.circle(
			self.image,
			coord_left,
			size - 1,
			(255,255,255),
			thickness=-1
		)

		coord_right = (
			(self.width // 2) + (span // 2),
			self.height - size - self.margin
		)

		cv.circle(
			self.image,
			coord_right,
			size,
			color,
			thickness=-1
		)

		cv.circle(
			self.image,
			coord_right,
			size - 1,
			(255,255,255),
			thickness=-1
		)

	def save(self, filename):
		cv.imwrite(filename, self.image)