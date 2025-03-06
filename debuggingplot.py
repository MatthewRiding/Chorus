import matplotlib.pyplot as plt
import matplotlib as mpl


mpl.use('TkAgg')

# plt.plot(np.real(a_scan_amplitudes_analytic))
plt.imshow(np.real(sampled_amps_complex))
