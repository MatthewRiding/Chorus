import numpy as np


def calculate_travel_times_direct(tfm_constructor, c_mpers):
    """Calculate direct straight-ray travel times to/from all pixels in the grid specified by tfm_constructor
    from/to all elements in the array specified by tfm_constructor, at the bulk elastic wave speed c_mpers."""
    # Calculate straight ray distances to all pixels from all elements:
    distances_direct_all_pixels_all_el_m = tfm_constructor.get_direct_ray_distances_all_pixels_all_el_m()
    # Divide straight-ray-distances by given bulk wave speed:
    travel_times_all_pixels_all_el_s = distances_direct_all_pixels_all_el_m / c_mpers
    return travel_times_all_pixels_all_el_s


def calculate_travel_times_l_direct(tfm_constructor):
    """Calculate direct bulk longitudinal wave travel times to/from all pixels in the specified grid,
    and from/to all elements in the specified linear periodic array."""
    travel_times_l_all_pixels_all_el_s = calculate_travel_times_direct(tfm_constructor,
                                                                       tfm_constructor.material.c_l_mpers)
    return travel_times_l_all_pixels_all_el_s


def calculate_travel_times_t_direct(tfm_constructor):
    """Calculate direct bulk transverse (shear) wave travel times to/from all pixels in the specified grid,
    and from/to all elements in the specified linear periodic array."""
    travel_times_t_all_pixels_all_el_s = calculate_travel_times_direct(tfm_constructor,
                                                                       tfm_constructor.material.c_t_mpers)
    return travel_times_t_all_pixels_all_el_s


def calculate_travel_times_head_wave_to_pixels(tfm_constructor):
    """To calculate the time taken for the head wave to reach this pixel, extrapolate from the pixel back up to
    the surface in a straight line at the critical angle to the surface normal.  The point where this angled
    line reaches the surface will be called the T-wave birth point.  The lateral distance between the T-wave
    birth point and the surface point directly above the pixel (x_pixel) will be called 'g_m'.  The delay law
    is computed by adding the time taken for a leaky surface wave (LSW) to travel from the source point to the
    T-wave birth point, and then for the T-wave to travel from the birth point to the pixel at the critical angle."""

    # Get data from tfm_constructor:
    c_t_over_c_l = tfm_constructor.material.c_t_mpers / tfm_constructor.material.c_l_mpers
    x_grid_m, z_grid_m = tfm_constructor.get_pixel_meshgrid_m()
    x_elements_m = tfm_constructor.get_x_elements_m()
    c_lsaw_mpers = tfm_constructor.material.c_lsaw_mpers
    c_t_mpers = tfm_constructor.material.c_t_mpers

    # Calculate lateral distance 'g'- the lateral distance between the pixel and the T-wave birth point.
    # g = tan(theta_crit) * z_pixel_mm
    # tan(theta_crit) = tan(arcsin(v_T/v_L)) = (v_T/v_L) / sqrt(1 - (v_T/v_L)**2)

    # tan(theta_crit) can be expressed more compactly using trig identities (WolframAlpha):

    g_m = (c_t_over_c_l / np.sqrt(1 - c_t_over_c_l ** 2)) * z_grid_m

    # Pre-allocate travel times array, with one page per element:
    n_tx = len(x_elements_m)
    shape = (n_tx,) + np.shape(x_grid_m)
    times_head_wave_to_pixel_s = np.zeros(shape)

    # For the final calculation of travel times, loop over element positions:
    for element_index, x_element_m in enumerate(x_elements_m):
        times_head_wave_to_pixel_s[element_index, :, :] = (((np.abs(x_grid_m - x_element_m) - g_m) / c_lsaw_mpers)
                                                           + (np.sqrt(g_m ** 2 + z_grid_m ** 2) / c_t_mpers))

    return times_head_wave_to_pixel_s


def calculate_travel_times_head_wave_to_pixels_subcrit_masked(tfm_constructor):
    """Calls 'calculate_travel_times_head_wave_to_pixels', and then applies a numpy mask to the pixels whose direct rays
    are below the critical angle."""
    # Calculate head wave travel times for all pixels:
    times_head_wave_to_pixel = calculate_travel_times_head_wave_to_pixels(tfm_constructor)

    # Apply a mask to these 'send' travel times, masking those pixels where direct send ray angle would be less than
    # the critical angle:

    # Calculate send ray angles:
    angles_direct_rays_radians = calculate_direct_ray_angles_radians(x_grid_m, z_grid_m, x_elements_m)
    # Calculate critical angle:
    angle_critical_radians = calculate_critical_angle_radians(
        v_L_mpers, v_T_mpers)

    # Mask the 'send' travel times: Pixels with rays above the critical angle are masked:
    travel_times_h_subcrit_masked = np.ma.masked_where(angles_direct_rays_radians < angle_critical_radians,
                                                       times_head_wave_to_pixel)
    return travel_times_h_subcrit_masked


dict_send_delay_funcs_tfm = {'L': calculate_travel_times_l_direct,
                             'T': calculate_travel_times_t_direct,
                             'H': calculate_travel_times_head_wave_to_pixels,
                             'Hybrid': func}
