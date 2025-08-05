import numpy as np
from scipy.signal import hilbert


def compute_tfm_complex(worker_id, fmc_3d, tfm_constructor, time_vector_us, signal_progress):
    """A generic TFM function that can run for different combinations of send and
    receive wave type."""
    # Emit the progress signal with the string 'Initialising...' to tell the user that
    # the calculation has begun:
    signal_progress.emit((worker_id, ' Initialising...'))

    # Calculate additional parameters from supplied data:
    n_samples = np.shape(fmc_3d)[0]
    n_tx = np.shape(fmc_3d)[1]
    period_sampling_us = time_vector_us[1] - time_vector_us[0]
    frequency_sampling_hertz = 1 / (period_sampling_us * 10**-6)

    # Build 2D arrays storing the imaging grid pixel coordinates:
    x_grid_m, z_grid_m = tfm_constructor.get_pixel_meshgrid_m()

    # Calculate travel times for send and receive legs:
    times_send_s, times_receive_s = tfm_constructor.get_travel_times_all_pixels_all_el(x_grid_m, z_grid_m)

    # Get any masks if specs have been provided to the constructor:
    gen_angles_rad_masked, det_angles_rad_masked = tfm_constructor.get_masks(x_grid_m, z_grid_m)

    # Apply bandpass filter to A-scans if requested:
    if tfm_constructor.filter_spec:
        signal_progress.emit((worker_id, ' Filtering...'))

        fmc_3d_filtered = tfm_constructor.filter_spec.apply_to_fmc(fmc_3d, frequency_sampling_hertz)

        # Use the analytic filtered fmc_3d in the subsequent calculations:
        fmc_3d_processed = hilbert(fmc_3d_filtered, axis=0)
    else:
        # No filtering: Use the analytic fmc_3d in the subsequent calculations:
        fmc_3d_processed = hilbert(fmc_3d, axis=0)

        # This function (compute_tfm) returns the filtered fmc_3d back to the caller for display in B-scan & fmc plots.
        # When not filtering, we want to return the 'fmc_3d_filtered' variable as 'None':
        fmc_3d_filtered = None

    # Main imaging algorithm loop:

    # Pre-allocate an accumulator array for the intensity image:
    intensity_image_complex = np.zeros(np.shape(x_grid_m))

    # Nested loops over detection (slow, outer) and generation (fast, inner) index:
    for det_index in range(n_tx):
        # Emit the 'progress' signal, transmitting a string showing the current detection index out of the total:
        signal_progress.emit((worker_id, f' TFM ({det_index + 1}/{n_tx})...'))

        # Inner loop: over generation index (fast):
        for gen_index in range(n_tx):
            # Calculate total travel time for send and receive via each pixel for this combination of det_index and
            # gen_index:
            delays_for_this_a_scan_s = times_send_s[gen_index] + times_receive_s[det_index]

            # Submit the array of total travel times as 1D-interpolation query points for the A-scan associated with
            # this combination of gen_index and det_index:
            a_scan_amplitudes_analytic = fmc_3d_processed[:, det_index, gen_index]
            sampled_amps_complex = np.interp(delays_for_this_a_scan_s,
                                             (time_vector_us * 10**-6), a_scan_amplitudes_analytic, left=0, right=0)

            # Apply gen and det angle masks, if any:
            if gen_angles_rad_masked is not None or det_angles_rad_masked is not None:
                # Some masking has been requested:

                # Get gen mask for this gen index:
                if gen_angles_rad_masked is not None:
                    mask_gen = np.ma.getmask(gen_angles_rad_masked[gen_index])
                else:
                    mask_gen = np.ma.nomask

                # Get det mask for this det index:
                if det_angles_rad_masked is not None:
                    mask_det = np.ma.getmask(det_angles_rad_masked[det_index])
                else:
                    mask_det = np.ma.nomask

                # Combine gen and det masks:
                mask_gen_and_det = np.ma.mask_or(mask_gen, mask_det)
                # Apply the combined mask to the pixel contributions:
                sampled_amps_complex_processed = np.ma.masked_where(mask_gen_and_det, sampled_amps_complex, copy=False)
            else:
                # The user has requested no masking:
                sampled_amps_complex_processed = sampled_amps_complex

            # Sum the sampled amplitudes onto the intensity image accumulator array:
            # Fill any masked elements with zeros:
            intensity_image_complex = intensity_image_complex + np.ma.filled(sampled_amps_complex_processed,
                                                                             fill_value=0)

    # Main loop over A-scans complete.  Complex intensity image created.

    # # Convert intensity to root-power decibels by normalising relative to a maximum intensity value.
    # # To avoid saturation by SAW crosstalk, ignore pixels in the upper third of the image.
    # row_index_below_which_to_max = round(tfm_params.n_pixels_z / 3)
    # reference_amplitude_0dB = np.max(np.abs(intensity_image_complex[row_index_below_which_to_max:, :]))
    #
    # # Convert to root-power dB using this reference amplitude:
    # image_decibels = 20 * np.log10(np.abs(intensity_image_complex) / reference_amplitude_0dB)

    # Return the image in dB units back to the script calling this function.
    return intensity_image_complex, fmc_3d_filtered
