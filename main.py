from Simulator import *

cat = Simulator(320, 180, 16)

cat.draw(
	5,
	16,
	(0,255,0)
)

cat.save('output.jpg')