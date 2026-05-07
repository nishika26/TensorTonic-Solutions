import numpy as np

def sigmoid(x):
    x = np.array(x)
    output = 1/(1/1+np.exp(-x))
    return output