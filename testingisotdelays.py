import matplotlib.pyplot as plt
from matplotlib import colormaps
import numpy as np
from scipy.ndimage import binary_erosion


from functions.delaylawfunctions.moddelaylawfunctions import calculate_delay_law_tl, calculate_delay_law_tt_subcrit
from functions.modbuildxgenandxdetmatrices import build_x_gen_and_x_det_matrices_m
from functions.modcalculatecriticalangle import calculate_critical_angle_radians
from functions.modfindascanswithclosestdelays import find_a_scans_with_closest_delays

# Input parameters:
x_pixel_m = 0
z_pixel_m = 5 * 10**-3
n_tx = 51
pitch_mm = 0.2
v_l_mpers = 5664
v_t_mpers = 3120
sampling_time_us = 3.7

# Build derived objects:
x_gen_matrix_m, x_det_matrix_m = build_x_gen_and_x_det_matrices_m(n_tx, pitch_mm)
angle_critical_radians = calculate_critical_angle_radians(v_l_mpers, v_t_mpers)

# Calculate delay matrix:
delay_matrix_s = calculate_delay_law_tt_subcrit(x_pixel_m, z_pixel_m, x_gen_matrix_m, x_det_matrix_m,
                                                angle_critical_radians, v_l_mpers, v_t_mpers)
delay_matrix_us = np.ma.getdata(delay_matrix_s) / 10**-6
# Extract mask:
mask = np.ma.getmask(delay_matrix_s)
# Find boundary of data, ignoring mask:
# Binarize:
delay_matrix_binary = np.where(delay_matrix_us <= sampling_time_us, 1, 0)
# Erode by 1 pixel:
delay_matrix_binary_erosion = binary_erosion(delay_matrix_binary, border_value=True).astype(delay_matrix_binary.dtype)
# Calculate boundary as difference:
boundary_binary = delay_matrix_binary - delay_matrix_binary_erosion
# Re-apply mask:
boundary_binary_masked = np.ma.masked_where(mask, boundary_binary, copy=False)

# Use boundary as mask to obtain plottable co-ordinate vectors:
delay_plot_y, delay_plot_x = np.ma.nonzero(boundary_binary_masked)

# Test function version:
gen_indices_closest, det_indices_nearest = find_a_scans_with_closest_delays(delay_matrix_s, sampling_time_us)

# Plotting:

# Index meshgrid for plotting:
indices = np.arange(n_tx)
indices_gen_matrix, indices_det_matrix = np.meshgrid(indices, indices)

# Quad co-ordinates for sampling time plane:
x_sampling_plane = np.array([[0, 50], [0, 50]])
y_sampling_plane = np.array([[0, 0], [50, 50]])
z_sampling_plane = np.ones([2, 2]) * sampling_time_us

# 3D surface plot:
fig_3d, ax = plt.subplots(subplot_kw={"projection": "3d"})
ax.plot_surface(indices_gen_matrix, indices_det_matrix, delay_matrix_us, cmap=colormaps['viridis'])
ax.plot_surface(x_sampling_plane, y_sampling_plane, z_sampling_plane, alpha=1, color='r')

# 2D binary plot:
fig_erosion, (ax_before, ax_after, ax_boundary) = plt.subplots(1, 3)

ax_before.imshow(delay_matrix_binary.data)
ax_before.set_title('Before :')

ax_after.imshow(delay_matrix_binary_erosion)
ax_after.set_title('After erosion :')

ax_boundary.imshow(boundary_binary_masked)
ax_boundary.set_title('Boundary\n(before - erosion) :')
ax_boundary.plot(gen_indices_closest, det_indices_nearest, linestyle='None', marker='D', markerfacecolor='None',
                 markeredgecolor='k')

plt.show()

a = 1
