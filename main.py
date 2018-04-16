from Simulator import *

cat = Simulator(320, 180, 16)

cat.draw_eyes(
	5,
	16,
	(0,255,255)
)

cat.save('output.jpg')