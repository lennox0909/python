import tensorflow as tf
# import keras

converter = tf.lite.TFLiteConverter.from_keras_model_file("B_MobileV2-PIL-78_70.h5")
tflite_model = converter.convert()
open("converted_model.tflite", "wb").write(tflite_model)
