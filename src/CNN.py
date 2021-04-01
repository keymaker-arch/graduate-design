from tensorflow import keras
from tensorflow.keras import layers
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


def make_dataset(positive_train_file, negative_train_file, positive_validation_file, negative_validation_file, batch_size):
    def transpose(matrix):
        new_matrix = []
        for i in range(len(matrix[0])):
            matrix1 = []
            for j in range(len(matrix)):
                matrix1.append(matrix[j][i])
            new_matrix.append(matrix1)
        return new_matrix

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
                        rtn_array.append(transpose(matrix))
                        matrix = []
        except:
            print("file not found: " + file_path)
        return rtn_array

    positive_train = read_file(positive_train_file)
    positive_train_label = [1 for x in positive_train]
    positive_validation = read_file(positive_validation_file)
    positive_validation_label = [1 for x in positive_validation]
    negative_train = read_file(negative_train_file)
    negative_train_label = [0 for x in negative_train]
    negative_validation = read_file(negative_validation_file)
    negative_validation_label = [0 for x in negative_validation]

    train_data = positive_train + negative_train
    validation_data = positive_validation + negative_validation
    train_data_label = positive_train_label +negative_train_label
    validation_data_label = positive_validation_label + negative_validation_label

    train_dataset = tf.data.Dataset.from_tensor_slices((train_data, train_data_label))
    validation_dataset = tf.data.Dataset.from_tensor_slices((validation_data, validation_data_label))

    return train_dataset.shuffle(50).batch(batch_size), validation_dataset.batch(batch_size)

if __name__ == '__main__':
    dir_base = '/home/han/文档/毕设/datasets/antimicrobial/'
    train_pos = dir_base + 'antimicrobial_matrix_training_pos'
    train_neg = dir_base + 'antimicrobial_matrix_training_neg'
    vali_pos = dir_base + 'antimicrobial_matrix_validation_pos'
    vali_neg = dir_base + 'antimicrobial_matrix_validation_neg'
    train, validation = make_dataset(train_pos, train_neg, vali_pos, vali_neg, 50)
    for ele in train:
        print(ele)
