import numpy as np
from keras_squeezenet import SqueezeNet
from keras.applications.imagenet_utils import preprocess_input, decode_predictions
from scipy import misc

def recognize(img_path):
    model = SqueezeNet()
 
    x = misc.imread(img_path).resize((227, 227))
    x = np.expand_dims(x, axis=0)
    x = preprocess_input(x)

    preds = model.predict(x)
    return decode_predictions(preds)
