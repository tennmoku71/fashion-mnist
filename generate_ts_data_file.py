import json
import tensorflow as tf
from tensorflow import keras

fashion_mnist = keras.datasets.fashion_mnist
(train_images, train_labels), (test_images, test_labels) = fashion_mnist.load_data()

d = {
    "signature_name": 'serving_default',
    "inputs": [test_images[0].tolist()]
}

with open('./test_data.json', mode='w') as f:
    f.write(json.dumps(d))
    
d = {
    "signature_name": 'serving_default',
    "inputs": [test_images[1].tolist()]
}

with open('./ruby_data.json', mode='w') as f:
    f.write(json.dumps(d))
    
print("{}, {}".format(test_labels[0], test_labels[1]))
# => 9, 2