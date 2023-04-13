import requests

def call_predict_api(data):
  api_url = "http://localhost:5000/predict"
  headers = {
    'Content-Type': 'audio/wave'
  }
  response = requests.request("POST", api_url, headers=headers, data=data)
  return response.text
