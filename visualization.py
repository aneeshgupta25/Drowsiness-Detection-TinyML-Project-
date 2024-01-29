import visualkeras
from keras.models import load_model
import netron

# Visualization of CNN Model
model = load_model('models/cnncat2.h5')
visualkeras.layered_view(model, legend=True)

# Visualization of TensorFlow Lite Model
netron.start('models/cnncat2.h5')
