import numpy as np
import matplotlib.pyplot as plt

from functions.modordergenindicesforcumsum import order_gen_indices_for_cumsum
from functions.modpcmangularcumsumfuncs import cumsum_sum

gen_angles = np.array([58, 50, 30, 0, 30])
mask_angle_meaning = 'Maximum'
gen_indices_ordered_for_cumsum = order_gen_indices_for_cumsum(gen_angles, mask_angle_meaning)

pcm_complex = np.array([[0, -1, 1, 0, 1],
                        [0, -1, 1, 0, 1]])
cumsum_abs = cumsum_sum(pcm_complex, gen_indices_ordered_for_cumsum)
gen_angles_ascending = gen_angles[gen_indices_ordered_for_cumsum]

plt.plot(gen_angles_ascending, cumsum_abs, marker='x')
plt.show()

a=1
