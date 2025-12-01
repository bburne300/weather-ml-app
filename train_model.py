import pandas as np
from sklearn.ensemble import RandomForestClassifier
import joblib

X_train = [
	[269.686, 1002, 78, 0, 23, 0, 0, 0, 0],
	[279.626, 998, 99, 1, 314, 0.3, 0, 0, 88],
	[289.47, 1015, 88, 2, 300, 0, 0, 0, 20],
	[275.15, 1013, 85, 3.6, 180, 0, 0, 0, 20],
]

y_train = ['clear', 'rain', 'foggy', 'rain']

model = RandomForestClassifier(n_estimators=10, random_state=42)
model.fit(X_train, y_train)

joblib.dump(model, 'weather_model.pkl')
print("Success! New weather_model.pkl created.")
