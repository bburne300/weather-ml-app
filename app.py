from flask import Flask, request, render_template
import pickle
import numpy as np
import time

app = Flask(__name__)

weather_classes = ['clear', 'cloudy', 'drizzly', 'foggy', 'hazey', 'misty', 'rainy', 'smokey', 'thunderstorm']

def load_model(model_path = 'model/model.pkl'):
	return pickle.load(open(model_path, 'rb'))

def classify_weather(features):
	model = load_model()
	start = time.time()
	prediction_index = model.predict(features)[0]
	latency = round((time.time() - start) * 1000, 2) #we are here
	prediction = weather_classes[1]
	
	return prediction, latency


@app.route('/', methods=['GET', 'POST'])
def home():
	if request.method == 'POST':
		try:
			# Extract floats from form data
			temperature = request.form['temperature']
			pressure = request.form['pressure']
			humidity = request.form['humidity']
			wind_speed = request.form['wind_speed']
			wind_deg = request.form['wind_deg']
			rain_1h = float(request.form.get('rain_1h', 0) or 0)
			rain_3h = float(request.form.get('rain_3h', 0) or 0)
			snow = float(request.form.get('snow', 0) or 0)
			clouds = float(request.form.get('clouds', 0) or 0)

			features = np.array([
				temperature, pressure, humidity,
				wind_speed, wind_deg, rain_1h,
				rain_3h, snow, clouds
			]).reshape(1, -1)

			
			prediction, latency = classify_weather(features)


			return render_template('result.html', prediction=prediction, latency=latency)

		except Exception as e:
			error_msg = f"Error processing input: {e}"
			return render_template('form.html', error=error_msg)
	# GET method: show the input form
	return render_template('form.html')


if __name__ == '__main__':
	app.run(host="0.0.0.0", port=5000)
