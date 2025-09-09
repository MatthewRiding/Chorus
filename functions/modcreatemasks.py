import numpy as np

from functions.modcalculatedirectrayangles import calculate_direct_ray_angles_all_pixels_all_el_radians


def create_tfm_masks(x_grid_m, z_grid_m, x_elements_m, mask_spec):
    # Calculate send ray angles:
    angles_direct_all_pixels_all_el_radians = calculate_direct_ray_angles_all_pixels_all_el_radians(x_grid_m, z_grid_m, x_elements_m)

    # Mask the 'send' travel times: Pixels with rays above the critical angle are masked:
    numpy_masking_function = mask_spec.mask_behaviour.numpy_masking_function
    mask_angle_deg = mask_spec.mask_angle_deg
    angles_all_pixels_all_el_rad_masked = numpy_masking_function(angles_direct_all_pixels_all_el_radians, np.deg2rad(mask_angle_deg))
    return angles_all_pixels_all_el_rad_masked
