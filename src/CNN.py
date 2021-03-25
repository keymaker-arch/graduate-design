import tensorflow as tf
from tensorflow import keras
from tensorflow.keras import layers


# matrix_shape is a tuple (line_num, row_num)
def make_model(matrix_shape, filter_len):
    # inputs = keras.Input(shape=(None, matrix_shape[1], matrix_shape[0]))
    inputs = keras.Input(shape=(matrix_shape[1], matrix_shape[0]))

    x = layers.Conv1D(
        input_shape=(matrix_shape[0], matrix_shape[1]),
        filters=matrix_shape[0],
        kernel_size=filter_len,
        strides=1,
        padding="valid",
        groups=matrix_shape[0]
    )(inputs)
    # print(x.output_shape())
    # x = keras.layers
    model = keras.Model(inputs, x)
    model.summary()

if __name__ == '__main__':
    make_model((13, 5), 5)