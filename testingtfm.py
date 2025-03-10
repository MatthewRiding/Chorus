import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.axes_grid1 import make_axes_locatable

from functions.modcomputetfm import compute_tfm
from functions.modloadfmclpfrommatfile import load_fmclp_from_mat_file
from functions.moddetrendfmc3d import detrend_fmc_3d
from classdefs.modtfmparams import TFMParams
from modfakesignal import FakeSignal

# User inputs:
mat_file_path = r"C:\Users\mattr\OneDrive - University of Strathclyde\Research project work\LU for fusion\Experimental data\2023_01_11_UKAEA_Stainless_12mm_thick_plate_weld_1D_LIPA_scans\Root_cavity\fmc_root_cavity_compatible.mat"
tfm_params = TFMParams('Test',
                       0.1,
                       5664,
                       3120,
                       'H-L',
                       50,
                       16,
                       300,
                       True,
                       10,
                       2.5,
                       12)
t_min_us = -1
t_max_us = 19

# Import FMC from mat file:
fmc_3d = load_fmclp_from_mat_file(mat_file_path)

# De-trend:
fmc_3d_detrend = detrend_fmc_3d(fmc_3d)

# Infer n_samples:
n_samples = np.shape(fmc_3d_detrend)[0]

# Build time vector:
time_vector_us = np.linspace(t_min_us, t_max_us, n_samples, endpoint=True)

# Build a progress signal:
signal_progress = FakeSignal()

# Call the compute tfm function:
image_decibels, fmc_3d_filtered = compute_tfm('', fmc_3d_detrend, tfm_params, time_vector_us, signal_progress)

# Plot the image:
SMALL_SIZE = 12
MEDIUM_SIZE = 14
BIGGER_SIZE = 16

plt.rc('font', size=BIGGER_SIZE)          # controls default text sizes
plt.rc('axes', titlesize=SMALL_SIZE)     # fontsize of the axes title
plt.rc('axes', labelsize=MEDIUM_SIZE)    # fontsize of the x and y labels
plt.rc('xtick', labelsize=SMALL_SIZE)    # fontsize of the tick labels
plt.rc('ytick', labelsize=SMALL_SIZE)    # fontsize of the tick labels
plt.rc('legend', fontsize=SMALL_SIZE)    # legend fontsize
plt.rc('figure', titlesize=BIGGER_SIZE)  # fontsize of the figure title

fig, ax_1 = plt.subplots(figsize=(10, 5))
axis_image = ax_1.imshow(image_decibels,
                         vmin=-20,
                         vmax=0,
                         extent=(-tfm_params.grid_size_x_mm / 2,
                                 tfm_params.grid_size_x_mm / 2,
                                 tfm_params.grid_size_z_mm, 0))

ax_1.set_title(f'{tfm_params.wave_set_string}, {tfm_params.band_min_MHz} - {tfm_params.band_max_MHz}MHz',
               fontsize=16)
ax_1.set_xlabel('$x$ (mm)')
ax_1.set_ylabel('$z$ (mm)')
ax_1.tick_params(top=True, labeltop=True, bottom=False, labelbottom=False)
ax_1.xaxis.set_label_position('top')

# Plot vertical lines for the side walls:
# side_width_mm = 27
# ax_1.vlines([-side_width_mm/2, side_width_mm/2], 0, 12, linestyles=(0, (8, 6)), colors=(1, 1, 1))

# Plot a horizontal line showing the back wall:
z_back_wall_mm = 12
ax_1.hlines(z_back_wall_mm, -20, 30, linestyles=(0, (6, 8)), colors=(1, 1, 1), linewidth=1)

# Plot lines for the weld bevels:
ax_1.plot([6, 12.928], [0, 12], linestyle=(0, (6, 8)), color=[1, 1, 1])
ax_1.plot([14.928, (14.928 + 6.928)], [12, 0], linestyle=(0, (6, 8)), color=[1, 1, 1])

ax_1.set_ylim(16, 0)
ax_1.set_xlim(-10, 23)

# Add colorbar:
divider = make_axes_locatable(ax_1)
cax1 = divider.append_axes("right", size="5%", pad=0.2)
fig.colorbar(axis_image, cax=cax1, label='Intensity (dB)')


plt.show()

a = 1
