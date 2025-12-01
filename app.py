from flask import Flask, request, render_template
import joblib
import numpy as np
import time

app = Flask(__name__)
#Changed rainy to rain
weather_classes = ['clear', 'cloudy', 'drizzly', 'foggy', 'hazey', 'misty', 'rain', 'smokey', 'thunderstorm']

# FIX 1: Point to model in the root directory
def load_model(model_path = 'weather_model.pkl'):
	with open(model_path, 'rb') as file: # Fix resource warning
		return joblib.load(file)

def classify_weather(features):
	model = load_model()
	start = time.time()
	prediction = model.predict(features)[0]
	latency = round((time.time() - start) * 1000, 2) #we are here
# Fix 2: Removed the harcoded line so we can actually return the models prediction
	
	return prediction, latency # corrected return


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
			# Fix 3: Ensure all inputs are converted to float
			features = np.array([
				float(temperature),float(pressure), float(humidity),
				float(wind_speed), float(wind_deg), float(rain_1h),
				float(rain_3h), float(snow), float(clouds)
			]).reshape(1, -1)

			
			prediction, latency = classify_weather(features)


			return render_template('result.html', prediction=prediction, latency=latency)

		except Exception as e:
			error_msg = f"Error processing input: {e}"
			return render_template('form.html', error=error_msg), 400 # Fix 4: Return 400 status code
	# GET method: show the input form
	return render_template('form.html')


if __name__ == '__main__':
	app.run(host="0.0.0.0", port=5000)
