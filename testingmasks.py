import numpy as np


angles = np.array([1, 2, 3, 4, 5])
times_direct = np.array([10, 20, 30, 40, 50])
times_send_masked = np.ma.masked_where(angles > 3, times_direct)

delays = times_direct + times_send_masked

a_scan_amplitudes = np.arange(50)
a_scan_times = np.linspace(0, 100, 50)

sampled_amps = np.interp(delays, a_scan_times, a_scan_amplitudes, left=0, right=0)
sampled_amps_masked = np.ma.array(sampled_amps, mask=delays.mask)
sampled_amps_filled = np.ma.filled(sampled_amps_masked, fill_value=0)

a = 1
