import cv2 as cv
import numpy as np

class Simulator:
	def __init__(self):
		# Initialises the Simulator object
		self.__pupil_distance_inter = None
		self.__pupil_distance = None
		self.__pupil_size = None
		self.__spectrum = None
		self.__output = None

	def render(self, parameters):
		# Main render method
		self.__set_params(parameters)
		self.__render_spectra()
		self.__render_eyes()
		self.__render_blur()
		self.__export()

	def __set_params(parameters):
		# Sets simulation parameters
		self.__pupil_distance_inter = parameters['pupil-distance-inter']
		self.__pupil_distance = parameters['pupil-distance']
		self.__pupil_size = parameters['pupil-size']
		self.__spectrum = parameters['spectrum']

	def __render_spectra(self):
		# Draws the spectrum

	def __render_eyes(self):
		# Draws the eyes
		pass

	def __render_blur(self):
		# Blurs the drawing according to parameters
		pass

	def __export(self):
		# Writes output to an image file
		pass