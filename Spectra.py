from random import uniform

class Spectra:
	def __init__(self):
		self.size = 100
		self.color = None
		self.spectra = [0 for _ in range(self.size)]

	def full(self):
		for i in range(self.size):
			self.spectra[i] = 1.0
		return self.spectra

	def red(self):
		for i in range(0,30):
			self.spectra[i] = 1.0
		for i in range(50, self.size):
			self.spectra[i] = 0.5
		return self.spectra

	def random(self, chunks=3):
		for j in range(chunks):
			start = 0
			end = self.size
			a = int(uniform(0,1) * self.size)
			b = int(uniform(0,1) * self.size)

			if b > a:
				start = a
				end = b
			else:
				start = b
				end = a 
			for i in range(start, end):
				self.spectra[i] = uniform(0.5,1.0)

		return self.spectra

