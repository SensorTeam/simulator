from Spectrum import Spectrum
from Simulator import Simulator

data = None

simulator = Simulator()

spectrum = Spectrum(data)

simulator.render({
	'pupil-distance-inter': None,
	'pupil-distance': None,
	'pupil-size': None,
	'spectrum': spectrum,
})