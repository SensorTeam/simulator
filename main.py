from Spectra import *
from Simulator import *

cat_eyes = Simulator(320, 180, 16)
cat_spectra = Spectra().full()

cat_eyes.draw(
	5,
	16,
	(255,255,255),
	cat_spectra
)

cat_eyes.save('output.jpg')