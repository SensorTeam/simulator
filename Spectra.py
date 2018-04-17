from random import uniform

class Spectra:
	def __init__(self):
		self.size = 100
		self.color = None
		self.spectra = [0 for _ in range(self.size)]

	def generate(self):
		for i in range(self.size):
			self.spectra[i] = uniform(0,1)
		return self.spectra
