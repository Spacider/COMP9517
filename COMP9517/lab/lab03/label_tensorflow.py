import tensorflow as tf
from tensorflow import keras

import numpy as np
import matplotlib.pyplot as plt

fashion_mnist = keras.datasets.fashion_mnist

(train_images, train_labels), (test_images, test_labels) = fashion_mnist.load_data()

print("The shape of train_images is ",train_images.shape)
print("The shape of train_labels is ",train_labels.shape)
print("The shape of test_images is ",test_images.shape)
print("The length of test_labels is ",len(test_labels))

plt.figure()
plt.imshow(train_images[0])
plt.colorbar()
plt.gca().grid(False)
plt.show()