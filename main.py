import numpy as np
from random import uniform
from Spectrum import Spectrum
from Simulator import Simulator

def random_spectrum():
	empty = Spectrum()
	data = empty.data
	for i in range(len(data)):
		data[i][1] = uniform(0,1)
	spectrum = Spectrum(data)

if __name__ == '__main__':
	# Initialise simulation environment
	simulator = Simulator()

	# Generate random spectrum
	spectrum = random_spectrum()

	# Render simulation to file
	simulator.render({
		'pupil-distance-inter': None,
		'pupil-distance': None,
		'pupil-size': None,
		'spectrum': spectrum,
	})