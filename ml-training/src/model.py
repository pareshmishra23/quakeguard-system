
import tensorflow as tf
from tensorflow import keras
from tensorflow.keras import layers

def create_model(input_shape=(6,)):
    model = keras.Sequential([
        layers.Input(shape=input_shape),
        layers.Dense(64, activation='relu'),
        layers.Dense(32, activation='relu'),
        layers.Dense(1, activation='sigmoid')
    ])
    model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])
    return model

if __name__ == "__main__":
    import numpy as np
    X = np.random.rand(100, 6)
    y = np.random.randint(0, 2, size=(100,))
    model = create_model()
    model.fit(X, y, epochs=5, batch_size=8)
    model.save("quake_model.h5")
