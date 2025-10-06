import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.axes_grid1 import make_axes_locatable
import colorcet as cc

from functions.modcomputetfmcommonsource import compute_tfm_common_source
from functions.modloadfullmatrixfrommatfile import load_full_matrix_from_mat_file
from functions.moddetrendfmc3d import detrend_fmc_3d
from classdefs.modtfmparams import TFMConstructor
from modfakesignal import FakeSignal

# User inputs:
mat_file_path = r"C:\Users\mattr\OneDrive - University of Strathclyde\Research project work\Back wall method\Data sets\2022_10_13_Tungsten_broken_end_thickness_1D_LIPA\2022_10_13_Tungsten_broken_end_thickness_1D_LIPA_v7.mat"
tfm_constructor = TFMConstructor('Test',
                            0.25,
                            5182,
                            2870,
                       'T-T',
                            30,
                            12,
                            100,
                            True,
                            10,
                            4,
                            12,
                            True,
                            45,
                            'Maximum')
t_min_us = -1
t_max_us = 19

# Import FMC from mat file:
fmc_3d = load_full_matrix_from_mat_file(mat_file_path)

# De-trend:
fmc_3d_detrend = detrend_fmc_3d(fmc_3d)

# Infer n_samples:
n_samples = np.shape(fmc_3d_detrend)[0]

# Build time vector:
time_vector_us = np.linspace(t_min_us, t_max_us, n_samples, endpoint=True)

# Build a progress signal:
signal_progress = FakeSignal()

# Call the compute tfm function:
gen_index = 20
image_complex, fmc_3d_filtered = compute_tfm_common_source('', fmc_3d_detrend, tfm_constructor, time_vector_us,
                                                           signal_progress, gen_index)

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
mod_intensity_limit_mV = 15
axis_image = ax_1.imshow(np.real(image_complex) * 1000,
                         extent=(-tfm_constructor.grid_size_x_mm / 2,
                                 tfm_constructor.grid_size_x_mm / 2,
                                 tfm_constructor.grid_size_z_mm, 0),
                         cmap=cc.m_CET_D7,
                         vmin=-mod_intensity_limit_mV,
                         vmax=mod_intensity_limit_mV)

ax_1.set_title(f'{tfm_constructor.wave_set_string}, {tfm_params.band_min_MHz} - {tfm_params.band_max_MHz}MHz',
               fontsize=16)
ax_1.set_xlabel('$x$ (mm)')
ax_1.set_ylabel('$z$ (mm)')
ax_1.tick_params(top=True, labeltop=True, bottom=False, labelbottom=False)
ax_1.xaxis.set_label_position('top')

# Plot vertical lines for the side walls:
# side_width_mm = 27
# ax_1.vlines([-side_width_mm/2, side_width_mm/2], 0, 12, linestyles=(0, (8, 6)), colors=(1, 1, 1))

# Plot a horizontal line showing the back wall:
# z_back_wall_mm = 12
# ax_1.hlines(z_back_wall_mm, -20, 30, linestyles=(0, (6, 8)), colors=(1, 1, 1), linewidth=1)

# Plot lines for the weld bevels:
# ax_1.plot([6, 12.928], [0, 12], linestyle=(0, (6, 8)), color=[1, 1, 1])
# ax_1.plot([14.928, (14.928 + 6.928)], [12, 0], linestyle=(0, (6, 8)), color=[1, 1, 1])

# ax_1.set_ylim(16, 0)
# ax_1.set_xlim(-10, 23)

# Add colorbar:
divider = make_axes_locatable(ax_1)
cax1 = divider.append_axes("right", size="5%", pad=0.2)
fig.colorbar(axis_image, cax=cax1, label='Intensity (mV)')


plt.show()

a = 1
