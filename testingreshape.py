import numpy as np
columns = np.arange(0, 9)
array_2d = np.tile(columns, (17, 1))

n_samples = np.shape(array_2d)[0]
n_a_scans = np.shape(array_2d)[1]
n_tx = int(np.sqrt(n_a_scans))

array_3d = np.reshape(array_2d, (n_samples, n_tx, n_tx))

print('hello')
