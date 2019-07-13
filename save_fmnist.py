import tensorflow as tf
from tensorflow import keras

fashion_mnist = keras.datasets.fashion_mnist
(train_images, train_labels), (test_images, test_labels) = fashion_mnist.load_data()
#train_images = train_images / 255.0

from PIL import Image
import numpy as np
import os

if not os.path.exists('images'):
    os.mkdir('images')

for index, image in enumerate(test_images):
	a = np.array(image)
	pilImg = Image.fromarray(np.uint8(a))
	pilImg.save('images/{0}.png'.format(index))