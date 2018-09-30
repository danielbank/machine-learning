import numpy as np

def running_mean(x):
    mu = 0
    mean_values = []
    for k in np.arange(0, len(x)):
        mu = mu + (x[k] - mu) / (k + 1)
        mean_values.append(mu)
    return mean_values
