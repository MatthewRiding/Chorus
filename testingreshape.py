import numpy as np


# Create some mock A-scans, each one just containing repeats of its column index:
# For example, the first A-scan will be '0,0,0,0,0,0,...' for n_samples.
n_tx = 3
n_samples = 17

n_a_scans = n_tx**2
columns = np.arange(0, n_a_scans)
# Store the A-scans in a 2D format, where each A-scan forms one column:
array_2d = np.tile(columns, (n_samples, 1))

# Now process as if unknown:
n_samples_measured = np.shape(array_2d)[0]
n_a_scans_measured = np.shape(array_2d)[1]
n_tx_measured = int(np.sqrt(n_a_scans))

array_3d = np.reshape(array_2d, (n_samples_measured,
                                 n_tx_measured, n_tx_measured))

# To access an A-scan in the 3D array according to its gen_index and det_index:
gen_index = 1
det_index = 2
# For n_tx = 3
a_scan_gd = array_3d[:, det_index, gen_index]

print('hello')
