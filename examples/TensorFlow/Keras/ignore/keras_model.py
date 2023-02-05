import tensorflow as tf

# tf.__version__
import matplotlib.pyplot as plt
import numpy as np

print("Loading data")
mnist = tf.keras.datasets.mnist  # 28*28 images of handwritten digits (0-9)

(x_train, y_train), (x_test, y_test) = mnist.load_data()

# data Normalizations ( scalling numbers between 0 and 1)
print("Normalizing data")
x_train = tf.keras.utils.normalize(x_train, axis=1)
x_test = tf.keras.utils.normalize(x_test, axis=1)

# Build Model
print("Building the Model")
kr_model = tf.keras.models.Sequential()
kr_model.add(tf.keras.layers.Flatten())  # input layer

kr_model.add(tf.keras.layers.Dense(128, activation=tf.nn.relu))  # hidden layers
kr_model.add(tf.keras.layers.Dense(128, activation=tf.nn.relu))
kr_model.add(tf.keras.layers.Dense(10, activation=tf.nn.softmax))  # output layer

# Compile Model
print("Compiling the model")
kr_model.compile(
    optimizer="adam", loss="sparse_categorical_crossentropy", metrics=["accuracy"]
)

# train the model
print("Training the Model")
kr_model.fit(x_train, y_train, epochs=3)

# save model
print("Saving the Model")
kr_model.save("num_reader.model")

# loadthe model above
# new_model = tf.keras.models.load_model("num_reader.model")


# check if the model actually generalize the data.
print("Accuracy of our model is:")
val_loss, val_acc = kr_model.evaluate(x_test, y_test)
print(val_loss, val_acc)

# predict example for index 0
print("Predict value at index 0:")
predictions = kr_model.predict([x_test])
print("The predicted number at index 0 is", np.argmax(predictions[0]))

# print the actauly value at that index
print("The actually number at index zero is (see the image below):")
plt.imshow(x_test[0])
plt.show()
