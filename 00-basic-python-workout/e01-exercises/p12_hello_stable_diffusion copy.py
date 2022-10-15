import time
import keras_cv
import tensorflow as tf
from tensorflow import keras
import matplotlib.pyplot as plt

# tf.debugging.set_log_device_placement(True)

# gpu = tf.config.list_physical_devices('GPU')
# tf.config.experimental.set_memory_growth(gpu[0], True)


# using `with tf.device("/GPU:0"):` causes an OOM in my crappy GPU

with tf.device("/device:CPU:0"):
    model = keras_cv.models.StableDiffusion(jit_compile=True, img_width=512, img_height=512)

    images = model.text_to_image("photograph of a bear driving a motorcycle", batch_size=3)

    def plot_images(images):
        plt.figure(figsize=(20, 20))
        for i in range(len(images)):
            ax = plt.subplot(1, len(images), i + 1)
            plt.imshow(images[i])
            plt.axis("off")

    plot_images(images)
    plt.show()
