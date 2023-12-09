import requests
import os
import hashlib

# For car+evaluation.zip

hash = '1559d51dcf327f4f8c71b711ceed7fd95a382fc8d8e1998667f4f23b82860403'

url = 'https://archive.ics.uci.edu/static/public/19/car+evaluation.zip'
response = requests.get(url)

if not os.path.exists('data'):
  print("data path not found! Creating Path...")
  os.mkdir('data')

with open('data/car+evaluation.zip', mode='wb') as f:
  f.write(response.content)

filename = 'data/car+evaluation.zip'
with open(filename, 'rb') as f:
  data = f.read()
  sha256hash = hashlib.sha256(data).hexdigest()

uci_car_sha256 = hash
if uci_car_sha256 != sha256hash:
  print("Computed hash does not match expected hash")
else:
  print("Computed hash matches expected hash")