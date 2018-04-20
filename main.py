import os
from flask import Flask, render_template, request, redirect

from random import uniform
from Spectrum import Spectrum
from Simulator import Simulator

app = Flask(__name__)
simulator = Simulator()

def green_spectrum():
	empty = Spectrum()
	data = empty.data
	green_index = 532 - int(empty.data[0][0])
	for i in range(green_index - 10, green_index + 10):
		data[i][1] = uniform(0,1)
	return Spectrum(data)

@app.route('/')
def home():
	return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit():
	spectrum = green_spectrum()
	simulator.render({
		'image-filename': 'static/output.jpg',
		'image-margin': 32,
		'image-height': 300,
		'image-width': 300,
		'pupil-distance-inter': int(request.form['pupil-distance-inter'].strip()),
		'pupil-distance': int(request.form['pupil-distance'].strip()),
		'pupil-size': int(request.form['pupil-size'].strip()),
		'spectrum': spectrum,
	})
	return redirect('/')

if __name__ == '__main__':
	app.run(debug=os.getenv('FLASK_DEBUG', True))