import numpy as np


def order_gen_indices_for_cumsum(gen_angles, mask_angle_meaning):
    # Find ordering indices that will arrange gen angles in ascending order:
    gen_indices_in_cumsum_order = np.argsort(gen_angles)
    # The user can change the meaning of the mask angle- whether it corresponds to a
    # maximum angle: signals from gen elements at angles lower than the mask angle are summed.
    # or
    # minimum angle: signals from gen elements at angles greater than the mask angle are summed.
    if mask_angle_meaning == 'Minimum':
        # The cumsum should occur in order of decreasing gen angle:
        gen_indices_in_cumsum_order = np.flipud(gen_indices_in_cumsum_order)
    return gen_indices_in_cumsum_order
