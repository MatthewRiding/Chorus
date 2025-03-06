import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import hilbert

# Create wavelet:
n_samples = 100
time_vector = np.arange(n_samples)
frequency = (6 * 2 * np.pi)/100
sin_component = np.sin(time_vector * frequency)
t_centre = (5/12) * 100
std = np.pi
gaussian_component = np.exp(-(time_vector - t_centre)**2 / (2 * std**2))
signal_pos = gaussian_component * sin_component

signal_pos_analytic = hilbert(signal_pos)
signal_neg_analytic = hilbert(-signal_pos)

# Sampling at time of interest:
sampling_time = 41.6
z_pos = np.interp(sampling_time, time_vector, signal_pos_analytic, left=0, right=0)
z_neg = np.interp(sampling_time, time_vector, signal_neg_analytic)

# Debugging complex interpolation:
# Pre-allocate output PCM:
n_tx = 64
pcm = np.zeros([n_tx, n_tx], dtype=np.complex128)
pcm[1, 1] = np.interp(sampling_time, time_vector, signal_pos_analytic, left=0, right=0)

# Plotting:

# Wavelet:
fig_1, ax = plt.subplots(1, 1)
ax.plot(time_vector, sin_component, label='Sine')
ax.plot(time_vector, gaussian_component, label='Gaussian')
ax.plot(time_vector, signal_pos, label='Signal pos')
ax.set_xlabel('Time')
ax.set_ylabel('Amplitude')
ax.set_title('Building wavelet')
ax.legend()

# Pos and neg signals:
fig_2 = plt.figure(layout="constrained", figsize=(9, 6))
gs = fig_2.add_gridspec(2, 2)

ax_pos = fig_2.add_subplot(gs[0, 0])
ax_pos.set_title('Signal pos')
ax_pos.plot(time_vector, np.real(signal_pos_analytic), label='Real')
ax_pos.plot(time_vector, np.imag(signal_pos_analytic), label='Imag')
ax_pos.plot(time_vector, np.abs(signal_pos_analytic), label='Abs')
ax_pos.axhline(0, color='black', linewidth=.5)
ax_pos.vlines(sampling_time, -1, 1, linestyles='dashed')
ax_pos.set_ylim(-1, 1)
ax_pos.legend()
ax_pos.set_xlabel('Time')
ax_pos.set_ylabel('Amplitude')

ax_neg = fig_2.add_subplot(gs[1, 0])
ax_neg.set_title('Signal neg')
ax_neg.plot(time_vector, np.real(signal_neg_analytic), label='Real')
ax_neg.plot(time_vector, np.imag(signal_neg_analytic), label='Imag')
ax_neg.plot(time_vector, np.abs(signal_neg_analytic), label='Abs')
ax_neg.axhline(0, color='black', linewidth=.5)
ax_neg.vlines(sampling_time, -1, 1, linestyles='dashed')
ax_neg.set_ylim(-1, 1)
ax_neg.legend()
ax_neg.set_xlabel('Time')
ax_neg.set_ylabel('Amplitude')

# Plot sampled values on Phasor:
ax_phasor = fig_2.add_subplot(gs[:, 1])
ax_phasor.axis('equal')
ax_phasor.axhline(0, color='black', linewidth=.5)
ax_phasor.axvline(0, color='black', linewidth=.5)
# Vectors at sampling time:
# ax_phasor.arrow(0, 0, np.real(z_pos), np.imag(z_pos), label='z_pos', color='magenta')
# ax_phasor.arrow(0, 0, np.real(z_neg), np.imag(z_neg), label='z_neg', color='cyan')
complex_numbers = signal_pos_analytic
colors = [(0, 0, 0) for i in range(n_samples)]
# [ax_phasor.annotate("", xy=(np.real(z), np.imag(z)), xytext=(0, 0),
#                     arrowprops=dict(arrowstyle="->", color=color))
#  for z, color in zip(complex_numbers, colors)]
[ax_phasor.arrow(0, 0, np.real(z), np.imag(z),
                 color=color)
 for z, color in zip(complex_numbers, colors)]
ax_phasor.set_title(f'Phasor at t={sampling_time}')
# Complete Lissajous for signals:
ax_phasor.plot(np.real(signal_pos_analytic), np.imag(signal_pos_analytic), label='pos lissajous')
ax_phasor.plot(np.real(signal_neg_analytic), np.imag(signal_neg_analytic), label='neg lissajous')
ax_phasor.legend()
ax_phasor.set_xlabel('Real')
ax_phasor.set_ylabel('Imag')

plt.show()
