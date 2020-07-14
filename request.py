import requests

url = 'http://localhost:5000/predict_api'
r = requests.post(url,json={'pH':7, 'TDS[ppm]':115, 'D.O.[ppm]':3.5})

print(r.json())