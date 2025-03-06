import numpy as np


from functions.modcalculatedistancesdirect import calculate_distances_direct_m
from functions.traveltimefunctions.modldirect import calculate_travel_times_l_direct
from functions.traveltimefunctions.modtdirect import calculate_travel_times_t_direct
from functions.traveltimefunctions.modh import calculate_travel_times_head_wave_to_pixels
from functions.modcalculatecriticalangle import calculate_critical_angle_radians
from functions.modcalculatedirectrayanglesradians import calculate_direct_ray_angles_radians


def calculate_travel_times_ll(x_grid_m, z_grid_m, x_elements_m, v_L_mpers, v_T_mpers):
    # L-L requires direct send and direct return paths:
    distances_direct_m = calculate_distances_direct_m(x_grid_m, z_grid_m, x_elements_m)

    # Convert distance to time for send and receive:
    travel_times_l_direct = calculate_travel_times_l_direct(distances_direct_m, v_L_mpers)

    # Return (send, return) travel times:
    return travel_times_l_direct, travel_times_l_direct


def calculate_travel_times_tt(x_grid_m, z_grid_m, x_elements_m, v_L_mpers, v_T_mpers):
    # T-T requires direct send and direct return paths:
    distances_direct_m = calculate_distances_direct_m(x_grid_m, z_grid_m, x_elements_m)

    # Convert distance to time for send and receive:
    travel_times_t_direct = calculate_travel_times_t_direct(distances_direct_m, v_T_mpers)

    # Return (send, return) travel times:
    return travel_times_t_direct, travel_times_t_direct


def calculate_travel_times_lt(x_grid_m, z_grid_m, x_elements_m, v_L_mpers, v_T_mpers):
    # L-T requires direct send and direct return paths:
    distances_direct_m = calculate_distances_direct_m(x_grid_m, z_grid_m, x_elements_m)

    # Convert distance to time for send and receive:
    travel_times_l_direct = calculate_travel_times_l_direct(distances_direct_m, v_L_mpers)
    travel_times_t_direct = calculate_travel_times_t_direct(distances_direct_m, v_T_mpers)

    # Return (send, return) travel times:
    return travel_times_l_direct, travel_times_t_direct


def calculate_travel_times_tl(x_grid_m, z_grid_m, x_elements_m, v_L_mpers, v_T_mpers):
    # T-L requires direct send and direct return paths:
    distances_direct_m = calculate_distances_direct_m(x_grid_m, z_grid_m, x_elements_m)

    # Convert distance to time for send and receive:
    travel_times_t_direct = calculate_travel_times_t_direct(distances_direct_m, v_T_mpers)
    travel_times_l_direct = calculate_travel_times_l_direct(distances_direct_m, v_L_mpers)

    # Return (send, return) travel times:
    return travel_times_t_direct, travel_times_l_direct


def calculate_travel_times_ht(x_grid_m, z_grid_m, x_elements_m, v_L_mpers, v_T_mpers):
    # H-T requires head wave send and direct return paths:
    distances_direct_m = calculate_distances_direct_m(x_grid_m, z_grid_m, x_elements_m)

    # Times:
    travel_times_h_subcrit_masked = calculate_travel_times_head_wave_to_pixels(x_grid_m, z_grid_m, x_elements_m,
                                                                               v_L_mpers, v_T_mpers)
    travel_times_t_direct = calculate_travel_times_t_direct(distances_direct_m, v_T_mpers)

    # Return (send, return) travel times:
    return travel_times_h_subcrit_masked, travel_times_t_direct


def calculate_travel_times_hl(x_grid_m, z_grid_m, x_elements_m, v_L_mpers, v_T_mpers):
    # H-L requires head wave send and direct return paths:
    distances_direct_m = calculate_distances_direct_m(x_grid_m, z_grid_m, x_elements_m)

    # Times:
    travel_times_h_subcrit_masked = calculate_travel_times_head_wave_to_pixels(x_grid_m, z_grid_m, x_elements_m,
                                                                               v_L_mpers, v_T_mpers)
    travel_times_l_direct = calculate_travel_times_l_direct(distances_direct_m, v_L_mpers)

    # Return (send, return) travel times:
    return travel_times_h_subcrit_masked, travel_times_l_direct
