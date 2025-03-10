import numpy as np

from functions.modcalculatedirectrayanglesradians import calculate_direct_ray_angles_radians


def create_tfm_masks(x_grid_m, z_grid_m, x_elements_m, mask_angle_deg, numpy_masking_function):
    # Calculate send ray angles:
    angles_rays_radians = calculate_direct_ray_angles_radians(x_grid_m, z_grid_m, x_elements_m)

    # Mask the 'send' travel times: Pixels with rays above the critical angle are masked:
    angles_rad_masked = numpy_masking_function(angles_rays_radians, np.deg2rad(mask_angle_deg))
    return angles_rad_masked
