import numpy as np


def sum_pcm_iso_gen_columns(pcm_complex):
    sums_of_columns = np.sum(pcm_complex, axis=0, dtype=np.complex128)
    return sums_of_columns


def sum_pcm_iso_offset_sub_diagonals(pcm_complex):
    n_tx = np.shape(pcm_complex)[0]
    sums_of_sub_diagonals = np.zeros(n_tx)
    for i in range(n_tx):
        if i == 0:
            sums_of_sub_diagonals[i] = np.trace(pcm_complex)
        else:
            sums_of_sub_diagonals[i] = (np.trace(pcm_complex, offset=i, dtype=np.complex128)
                                        + np.trace(pcm_complex, offset=-i, dtype=np.complex128))
    return sums_of_sub_diagonals
