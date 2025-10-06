import matplotlib.pyplot as plt
import numpy as np

from functions.modloadfullmatrixfrommatfile import load_full_matrix_from_mat_file
from functions.moddetrendfmc3d import detrend_full_matrix_3d_dgt
from functions.modfilterfmc3dbutterOLD import filter_fmc3d_butter_OLD
from functions.modfilterfmc3dbutter import filter_full_matrix_3d_dgt_butter

# User inputs:
mat_file_path = r"C:\Users\mattr\OneDrive - University of Strathclyde\Research project work\LU for fusion\Experimental data\2024_07_25_Matt_DEMO_monoblock\Side side no holes\scan 1 101 el 256av 22mm ap\fmc_compatible.mat"
t_min_us = -1
t_max_us = 19

butter_order = 10
band_min_MHz = 4
band_max_MHz = 10

# Import FMC from mat file:
fmc_3d = load_full_matrix_from_mat_file(mat_file_path)

# Measure size parameters:
n_samples = np.shape(fmc_3d)[0]

# Make time vector:
time_vector_us = np.linspace(t_min_us, t_max_us, n_samples)

# Calculate sampling frequency:
period_sampling_us = time_vector_us[1] - time_vector_us[0]
frequency_sampling_hertz = 1 / (period_sampling_us * 10**-6)

# De-trend:
fmc_3d_detrend = detrend_full_matrix_3d_dgt(fmc_3d)

# Create filtered versions:
fmc_3d_filt_OLD = filter_fmc3d_butter_OLD(fmc_3d_detrend, frequency_sampling_hertz,
                                          butter_order, band_min_MHz, band_max_MHz)
fmc_3d_filfilt = filter_full_matrix_3d_dgt_butter(fmc_3d_detrend, frequency_sampling_hertz,
                                                  butter_order, band_min_MHz, band_max_MHz)

# Plot:
fig, ax_1 = plt.subplots(figsize=(10, 5))


# Define plotting function:
def plot_a_scan(fmc_3d_array, color, label):
    ax_1.plot(time_vector_us, fmc_3d_array[:, 1, 1], color=color, label=label)


# Call plotting function:
plot_a_scan(fmc_3d_detrend, 'b', 'Unfiltered')
plot_a_scan(fmc_3d_filt_OLD, 'r', 'Old: filt')
plot_a_scan(fmc_3d_filfilt, 'g', 'New: filtfilt')

# Set plot parameters:
ax_1.set_xlim(t_min_us, t_max_us)
plt.legend()

plt.show()
