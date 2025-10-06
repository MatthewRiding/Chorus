import numpy as np
import matplotlib.pyplot as plt

from functions.modloadfullmatrixfrommatfile import load_full_matrix_from_mat_file


# Import a full matrix from a .mat file:
mat_file_path = r"C:\Users\mattr\OneDrive - University of Strathclyde\General\00_Experimental Data\2025_02_05_Matt_SDH_polarity_Al_FMC\Scan 2 long\FMC_v7.mat"
fmc_3d_mat = load_full_matrix_from_mat_file(mat_file_path)

# The format of the 3d numpy array 'fmc_3d' is such that a given A-scan can be accessed by:
# a_scan_gd = fmc_3d[:, det_index, gen_index]
# See the test script 'testingreshape.py' for an interactive toy example.

# Save the numpy array 'fmc_3d_mat' into a .npy file:
np.save('fmc_3d', fmc_3d_mat)

# Read the saved file:
fmc_3d_npy = np.load('fmc_3d.npy')

# Plot A-scans to check:
gen_index = 37
det_index = 18
a_scan_gd_mat = fmc_3d_mat[:, det_index, gen_index]
a_scan_gd_npy = fmc_3d_npy[:, det_index, gen_index]

fig, (ax_1, ax_2) = plt.subplots(2, 1, layout='constrained')

ax_1.plot(a_scan_gd_mat)
ax_1.set_title('From .mat file')

ax_2.plot(a_scan_gd_npy)
ax_2.set_title('From .npy file')

plt.show()

a=1