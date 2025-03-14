import requests

url = "http://127.0.0.1:5000/predict/can"
files = {"file": open(r"Picture Path", "rb")}
response = requests.post(url, files=files) 

print(response.json())

