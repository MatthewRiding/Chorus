import numpy as np


# Create some mock A-scans, each one just containing repeats of its generation index:
# For example, the first A-scan will be '0,0,0,0,0,0,...' for n_samples.
n_elements = 3
n_samples = 17

n_a_scans = n_elements ** 2
column = np.arange(0, n_a_scans)
# Store the A-scans in a 2D format, where each A-scan forms one row:
array_2d_dnplusgt = np.tile(column, (n_samples, 1)).T

# Now process as if unknown:
shape = np.shape(array_2d_dnplusgt)
n_a_scans_measured = shape[0]
n_samples_measured = shape[1]
n_elements_measured = int(np.sqrt(n_a_scans))

array_3d_dgt = np.reshape(array_2d_dnplusgt, (n_elements_measured, n_elements_measured, n_samples_measured))

# To access an A-scan in the 3D array according to its gen_index and det_index:
gen_index = 1
det_index = 2
# For n_tx = 3
a_scan_gd = array_3d_dgt[:, det_index, gen_index]

# Does an iso time slice look correct?  Generation indices should form rows, detection indices should form columns.
iso_time_slice = array_3d_dgt[:, :, 0]

print('hello')
