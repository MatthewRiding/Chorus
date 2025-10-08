from scipy.signal import detrend


def detrend_full_matrix_3d_dgt(displacements_3d_dgt):
    """Subtract the mean of each A-scan from all its displacement values using scipy de-trend in 'constant' mode."""
    # scipy.signal.detrend() acts along the last axis of an array by default.  For the numpy[d,g,t] full matrix format,
    # this is the time axis (so A-scans have their individual means subtracted separately).
    displacements_3d_dgt_detrend = detrend(displacements_3d_dgt, type='constant')
    return displacements_3d_dgt_detrend
