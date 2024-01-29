model = load_model('models/cnncat2.h5')

# Convert Keras model to a tflite model
converter = tf.lite.TFLiteConverter.from_keras_model(model)
converter.optimizations = [tf.lite.Optimize.OPTIMIZE_FOR_SIZE]
tflite_model = converter.convert()

open("mymodel" + '.tflite', 'wb').write(tflite_model)