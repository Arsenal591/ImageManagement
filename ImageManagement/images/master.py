import numpy as np
from keras_squeezenet import SqueezeNet
from keras.applications.imagenet_utils import preprocess_input, decode_predictions
from scipy import misc

def recognize(x):
    #pass
    x = misc.imresize(x, (227,227)).astype('float64')
    x = np.expand_dims(x, axis=0)
    x = preprocess_input(x)

    preds = SqueezeNet().predict(x)
    return decode_predictions(preds)
