from tensorflow import keras
from tensorflow.keras import layers
import numpy as np
import tensorflow as tf


# matrix_shape is a tuple (aa_num, property_num)
def make_model(matrix_shape, kernel_len=5):
    inputs = keras.Input(shape=(matrix_shape[0], matrix_shape[1]))
    slice_list = []
    for prop in range(0, matrix_shape[1]):
        slice_list.append(layers.Conv1D(filters=1, kernel_size=kernel_len, activation='sigmoid')(inputs[:, :, prop:prop+1]))
    x = layers.Concatenate(axis=1)(slice_list)
    x = layers.Dense(50, activation='sigmoid')(x)
    x = layers.Dense(2, activation='sigmoid')(x)
    model = keras.Model(inputs, x)
    model.summary()
    return model


def make_dataset(positive_train_file, positive_test_file, negative_train_file, negative_test_file, batch_size):
    def read_file(file_path):
        rtn_array = []
        try:
            with open(file_path, 'r') as fp:
                matrix = []
                for line in fp:
                    if line != '\n':
                        line = line.strip('\t\n')
                        vector = line.split('\t')
                        vector = [float(x) for x in vector]
                        matrix.append(vector)
                    else:
                        rtn_array.append(np.array(matrix).T)
                        matrix = []
        except:
            print("file not found: " + file_path)
        return rtn_array

    positive_train = read_file(positive_train_file)
    positive_train_label = [1 for x in positive_train]
    positive_test = read_file(positive_test_file)
    positive_test_label = [1 for x in positive_test]
    negative_train = read_file(negative_train_file)
    negative_train_label = [0 for x in negative_train]
    negative_test = read_file(negative_test_file)
    negative_test_label = [0 for x in negative_test]

    train_data = positive_train + negative_train
    test_data = positive_test + negative_test
    train_data_label = positive_train_label +negative_train_label
    test_data_label = positive_test_label + negative_test_label

    train_dataset = tf.data.Dataset.from_tensor_slices((train_data, train_data_label))
    test_dataset = tf.data.Dataset.from_tensor_slices((test_data, test_data_label))

    return train_dataset.shuffle(50).batch(batch_size), test_dataset.batch(batch_size)


if __name__ == '__main__':
    train, test = make_dataset('/home/han/test', '', '', '', 1)
    for elem in train:
        print(elem)