# Description - test model preduiction 
# Using the saved model deployed to Google Kubernetes Engine 
# Served using containarized TF Serving 

import json 
from tensorflow import keras
import requests

# fashion mnist dataset
fashion_mnist = keras.datasets.fashion_mnist
(train_images, train_labels), (test_images, test_labels) = fashion_mnist.load_data()

train_images = train_images.reshape(train_images.shape[0], 28, 28, 1)
test_images = test_images.reshape(test_images.shape[0], 28, 28, 1)

data = json.dumps({"signature_name": "serving_default", "instances": test_images[0:3].tolist()})
headers = {"content-type": "application/json"}

host = '35.193.110.183' # update this based on kubectl get svc fashion - External IP
url = str('http://')+host+str(':8501/v1/models/fashion:predict')

# make request
json_response = requests.post(url, data=data)
predictions = json.loads(json_response.text)['predictions']
print(predictions)