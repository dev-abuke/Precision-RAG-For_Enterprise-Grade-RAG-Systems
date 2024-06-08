import requests

url = 'http://127.0.0.1:5000/generate'
data = {'question': 'When is the deadline for interim report submission?'}

response = requests.post(url, data=data)

print('Status Code:', response.status_code)
print('Response Text:', response.text)
