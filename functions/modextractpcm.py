import numpy as np
from scipy.signal import hilbert


def extract_pcm(displacements_3d_nm, time_vector_us, delay_matrix_s):
    """Samples a 3D full matrix of A-scans using a 2D matrix of delays (one delay per A-scan) to extract a 2D matrix
    of complex displacement values that would be summed to a given pixel in a TFM image (the pixel contribution matrix (
    PCM))."""

    # Measure n_tx:
    n_tx = np.shape(delay_matrix_s)[1]

    # Convert seconds (s) to microseconds (us):
    time_vector_s = time_vector_us * 10 ** -6

    # Pre-allocate output PCM- this will be an array of complex numbers:
    pcm_complex_nm = np.zeros([n_tx, n_tx], dtype=np.complex128)

    for det_index in range(n_tx):
        for gen_index in range(n_tx):
            # Extract A-scan [i,j]:
            displacements_a_scan_nm = hilbert(displacements_3d_nm[det_index, gen_index, :])
            # Extract delay [i,j]:
            delay_s = delay_matrix_s[det_index, gen_index]
            # Interpolate A-scan at delay time & save into PCM:
            pcm_complex_nm[det_index, gen_index] = np.interp(delay_s, time_vector_s, displacements_a_scan_nm,
                                                             left=0, right=0)

    # Since the numpy.interp() function does not propagate the mask from delay_matrix_s (if it is a
    # MaskedArray), we have to manually re-apply the mask:
    mask = np.ma.getmask(delay_matrix_s)
    pcm_complex_processed_nm = np.ma.masked_where(mask, pcm_complex_nm, copy=False)

    return pcm_complex_processed_nm
