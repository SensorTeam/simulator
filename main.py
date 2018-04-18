import numpy as np
from random import uniform
from Spectrum import Spectrum
from Simulator import Simulator

def random_spectrum():
	empty = Spectrum()
	data = empty.data
	for i in range(len(data)):
		data[i][1] = uniform(0,1)
	return Spectrum(data)

def green_spectrum():
	empty = Spectrum()
	data = empty.data
	green_index = 532 - int(empty.data[0][0])
	for i in range(green_index - 50, green_index + 50):
		data[i][1] = uniform(0,1)
	return Spectrum(data)

if __name__ == '__main__':
	# Initialise simulation environment
	simulator = Simulator()

	# Generate random spectrum
	spectrum = random_spectrum()

	# Render simulation to file
	simulator.render({
		'image-filename': 'random.jpg',
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