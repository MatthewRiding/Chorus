import numpy as np
from scipy.signal import hilbert
import matplotlib.pyplot as plt

from functions.modloadfullmatrixfrommatfile import load_full_matrix_from_mat_file


mat_file_path = r"C:\Users\mattr\OneDrive - University of Strathclyde\Research project work\LU for fusion\Experimental data\2022_10_05_notched_tungsten_1D_LIPA\2022_10_05_Notched_Tungsten_1D_LIPA_v7.mat"

# Import FMC from mat file:
fmc_3d = load_full_matrix_from_mat_file(mat_file_path)

# Extract one A-scan:
det_index = 45
gen_index = 12
a_scan_amplitudes = hilbert(fmc_3d[:, det_index, gen_index])

# Create time vector:
time_vector_us = np.linspace(-1, 18.98, 1000)

# Plot real and imaginary parts of A-scan:
t_min_us = 2.5
t_max_us = 4.5
amp_min = -0.015
amp_max = 0.015
fig, (ax_real, ax_imag) = plt.subplots(2, 1, layout="constrained")
ax_real.plot(time_vector_us, np.real(a_scan_amplitudes))
ax_real.set_title('Real')
ax_real.set_xlabel('Time (μs)')
ax_real.set_xlim(t_min_us, t_max_us)
ax_real.set_ylim(amp_min, amp_max)

ax_imag.plot(time_vector_us, np.imag(a_scan_amplitudes))
ax_imag.set_title('Imag')
ax_imag.set_xlabel('Time (μs)')
ax_imag.set_xlim(t_min_us, t_max_us)
ax_imag.set_ylim(amp_min, amp_max)

plt.show()
