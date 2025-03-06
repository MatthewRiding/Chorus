import numpy as np
from scipy.ndimage import binary_erosion


def find_a_scans_with_closest_delays(delay_matrix_s, time_viewing_us):
    """Finds the gen and det indices of the A-scans whose delays are closest to the current viewing time.

    The A-scans whose gen & det indices are returned sit on the morphological boundary between the set of A-scans with
    delays greater than or equal to the viewing time, and the surrounding A-scans whose delays are still greater than
    the viewing time.
    """
    delay_matrix_us_data = np.ma.getdata(delay_matrix_s) / 10**-6
    # If all the delays are less than the viewing time, then return empty lists:
    if np.max(delay_matrix_us_data) < time_viewing_us:
        gen_indices_nearest = []
        det_indices_nearest = []
    else:
        # Extract the mask from the original delay_matrix_s, if it has one:
        mask = np.ma.getmask(delay_matrix_s)
        # Binarize the data, separating the delays that are less than or equal to the viewing time from those greater
        # than:
        delay_matrix_binary = np.where(delay_matrix_us_data <= time_viewing_us, 1, 0)
        # Erode by 1 pixel:
        delay_matrix_binary_erosion = binary_erosion(delay_matrix_binary, border_value=True).astype(delay_matrix_binary.dtype)
        # Calculate boundary as difference:
        boundary_binary = delay_matrix_binary - delay_matrix_binary_erosion
        # Re-apply the original validity mask:
        boundary_binary_masked = np.ma.masked_where(mask, boundary_binary, copy=False)
        # Use np.ma.nonzero() to obtain the indices of the un-masked boundary A-scans:
        det_indices_nearest, gen_indices_nearest = np.ma.nonzero(boundary_binary_masked)

    return gen_indices_nearest, det_indices_nearest
