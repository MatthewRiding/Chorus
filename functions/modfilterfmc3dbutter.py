from scipy.signal import butter, sosfiltfilt


def filter_full_matrix_3d_dgt_butter(displacements_3d_dgt_nm, frequency_sampling_hertz,
                                     butter_order, band_min_MHz, band_max_MHz):
    # Apply a Butterworth band pass filter of order 'butter_order' to the A-scans in fmc_3d,
    # with a pass band of (band_min, band_max):

    # First, create the second-order sections (sos) for the butterworth filter:
    sos = butter(butter_order, [band_min_MHz * 10**6, band_max_MHz * 10**6],
                 btype='bandpass', fs=frequency_sampling_hertz, output='sos')

    # Next, apply the filter to the A-scan matrix using the sosfilt function (along final array axis by default):
    displacements_3d_dgt_filtered_nm = sosfiltfilt(sos, displacements_3d_dgt_nm)

    return displacements_3d_dgt_filtered_nm
