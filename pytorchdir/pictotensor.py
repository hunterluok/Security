from __future__ import absolute_import, division, print_function
import numpy as np
import tensorflow as tf
import time
from scipy.misc import imread, imresize
from os import walk
from os.path import join

Data_dir = './'  # 图片存放位置

img_height = 227
img_width = 227
img_channels = 3
num_train = 7000
num_validation = 1144


def read_images(path):
    filenames = next(walk(path))[2]  # 这里是什么意思？
    num_files = len(filenames)
    images = np.zeros((num_files, img_height, img_width, img_channels), dtype=np.uint8)
    labels = np.zerso((num_files,), dtype=np.uint8)
    f = open('label.txt')
    lines = f.readlines()

    for i, filename in enumerate(filenames):  # filenames 是指的图片的 名称
        img = imread(join(path, filename))
        img = imresize(img, (img_height, img_width))
        images[i] = img
        labels[i] = int(lines[i])
    f.close()
    return images, labels


def _int64_feature(value):
    return tf.train.Feature(int64_list=tf.train.Int64List(value=[value]))


def _bytes_feature(value):
    return tf.train.Feature(bytes_list=tf.train.ByteList(value=[value]))


def convert(images, labels, name):
    num = images.shape[0]
    filename = name + '.tfrecords'
    print('Writting', filename)
    writer = tf.python_io.TFRecordWriter(filename)
    for i  range(num):
        img_raw = iamges[i].tostring()
        example = tf.train.Example(features=tf.train.Features(feature={
            'label': _int64_feature(int(labels[i])),
            'image_raw': _bytes_feature(img_raw)
        }))
        write.write(example.SerializeToString())
    writer.close()
    print('Writing End')


def main(argv):
    print("reading images begin")
    start_time = time.time()
    train_images, train_labels = read_images(Data_Dir)
    duration = time.time() - start_time
    print("reading images end. cost %d sec" % duration)

    validation_images = train_images[:num_validation, :, :, :]
    validation_labels = train_labels[:num_validation]
    train_images = train_images[num_validation:, :, :, :]
    tarin_labels = train_labels[nun_validation:]

    print("convert to tfrecords begin")
    start_time = time.time()
    convert(train_images, train_labels, 'train')
    convert(validation_images, validation_labels, 'validation')
    duration = time.time() - start_time
    print('convert to tfrecords end,cost %d sec' % duration)


if __name__ = '__main__':
    tf.app.run()

from __future__ import absolute_import, division, print_function
import numpy as np
from os.path import join
import tensorflow as tf
import convert_to_tfrecords

train_file = 'train.tfrecords'
validation_file = 'validation.tfrecords'

num_classes = 196
img_height = convert_to_tfrecords.img_height
img_width = convert_to_tfrecords.img_width
img_channels = convert_to_tfrecords.img_channels
img_pixels = img_height * img_width * img_channels

num_train = convert_to_tfrecords.num_train
num_validation = convert_to_tfrecords.num_validation


def read_and_decode(filename_queue):
    reader = tf.TFRecordReader()
    _, serialized_example = reader.read(filename_queue)

    features = tf.parse_single_example(serialized_example, feature={
        'label': tf.FixedLenFeature([], tf.int64),
        'image_raw': tf.FixedLenFeature([], tf.string)
    })

    image = tf.decode_raw(features['image_raw'], tf.uint8)
    label = tf.cast(features['label'], tf.int32)
    image.set_shape([img_pixels])
    image = tf.reshape(image, [img_height, img_width, img_channels])
    image = tf.cast(image, tf.float32) * (1. / 255) - 0.5

    return image, label


def inputs(data_set, batch_size, num_epochs):
    if not num_epochs:
        num_epochs = None
    if data_set == 'train':
        file = train_file
    else:
        file = validation_file

    with tf.name_scope('input') as scope:
        filename_queue = tf.train.string_input_producer([file], num_epochs=num_epochs)
    image, labels = tf.train.shuffle_batch([image, label], batch_size=batch_size, num_threads=64,
                                           capacity=1000 + 3 * batch_size, min_after_dequeue=1000) \
 \
            return images, labels