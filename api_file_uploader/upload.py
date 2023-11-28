import requests

file = { 'file': open('random_file.png', 'rb')}

response = requests.post('http://127.0.0.1:8000/cadastro/api/file', files=file)

print(response.text)
