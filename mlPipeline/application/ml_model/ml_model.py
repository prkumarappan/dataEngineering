# Dataset: fashion_mnist
# Use the dataset to create a ML Model that can predict the class of the fashion item based on the image of the item.
# Save the model in SavedModel format
# Reference: https://www.tensorflow.org/tfx/tutorials/serving/rest_simple

import tensorflow as tf
from tensorflow import keras
import os
import json

# fashion mnist dataset
fashion_mnist = keras.datasets.fashion_mnist
(train_images, train_labels), (test_images, test_labels) = fashion_mnist.load_data()

# scale the values to 0.0 to 1.0
train_images = train_images / 255.0
test_images = test_images / 255.0

#reshape for feeding into the model
reshape_train_images = train_images.reshape(train_images.shape[0], 28, 28, 1)
reshape_test_images = test_images.reshape(test_images.shape[0], 28, 28, 1)

class_names = ['T-shirt/top', 'Trouser', 'Pullover', 'Dress', 'Coat',
                'Sandal', 'Shirt', 'Sneaker', 'Bag', 'Ankle boot']

# train the model
fashion = keras.Sequential([
    keras.layers.Conv2D(input_shape=(28,28,1), filters=8, kernel_size=3,
                        strides=2, activation='relu', name='Conv1'),
    keras.layers.Flatten(),
    keras.layers.Dense(10, activation=tf.nn.softmax, name='Softmax')
])
fashion.summary()

epochs = 5

fashion.compile(optimizer='adam',
                loss='sparse_categorical_crossentropy',
                metrics=['accuracy'])
fashion.fit(reshape_train_images, train_labels, epochs=epochs)

test_loss, test_acc = fashion.evaluate(reshape_test_images, test_labels)
print('Test accuracy: {:2.2f}%'.format(test_acc*100))

# save model in SavedModel format
MODEL_DIR = os.getcwd()
name = 'fashion'
version = 1
export_path = os.path.join(MODEL_DIR, str(name), str(version))
print('export_path = {}\n'.format(export_path))

tf.keras.models.save_model(
    fashion,
    export_path,
    overwrite=True,
    include_optimizer=True,
    save_format=None,
    signatures=None,
    options=None
)

print('\nSaved model')

# test the model.predict
predictions = fashion.predict(test_images[0:1])
print(predictions[0])
