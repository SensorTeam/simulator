import numpy as np
from random import uniform
from Spectrum import Spectrum
from Simulator import Simulator

def full_spectrum():
	empty = Spectrum()
	data = empty.data
	for i in range(0, len(empty.data)):
		data[i][1] = 1.0
	return Spectrum(data)

def yellow_spectrum():
	# Generate an empty spectrum (all wavelengths with 0 intensity)
	empty = Spectrum()
	data = empty.data
	# Set green wavelengths to full intensity
	green_index = 532 - int(empty.data[0][0])
	for i in range(green_index - 10, green_index + 10):
		data[i][1] = uniform(0,1)
	# Set red wavelengths to full intensity
	red_index = 625 - int(empty.data[0][0])
	for i in range(red_index - 10, red_index + 10):
		data[i][1] = uniform(0,1)
	# Return a yellow spectrum
	return Spectrum(data)

def green_spectrum():
	empty = Spectrum()
	data = empty.data
	green_index = 532 - int(empty.data[0][0])
	for i in range(green_index - 10, green_index + 10):
		data[i][1] = uniform(0,1)
	return Spectrum(data)

if __name__ == '__main__':
	# Initialise simulation environment
	simulator = Simulator()

	# Generate full spectrum
	spectrum = full_spectrum()

	# Render simulation to file
	simulator.render({
		'image-filename': 'full.jpg',
		'image-margin': 32,
		'image-height': 300,
		'image-width': 300,
		'pupil-distance-inter': 32,
		'pupil-distance': 100,
		'pupil-size': 8,
		'spectrum': spectrum,
	})

	# Generate yellow spectrum
	spectrum = yellow_spectrum()

	# Render simulation to file
	simulator.render({
		'image-filename': 'yellow.jpg',
		'image-margin': 32,
		'image-height': 300,
		'image-width': 300,
		'pupil-distance-inter': 32,
		'pupil-distance': 100,
		'pupil-size': 8,
		'spectrum': spectrum,
	})

	# Generate green spectrum
	spectrum = green_spectrum()

	# Render simulation to file
	simulator.render({
		'image-filename': 'green.jpg',
		'image-margin': 32,
		'image-height': 300,
		'image-width': 300,
		'pupil-distance-inter': 32,
		'pupil-distance': 100,
		'pupil-size': 8,
		'spectrum': spectrum,
	})