import numpy as np


def calculate_gen_angle_matrix_deg(x_pixel_m, z_pixel_m, x_gen_matrix_m):
    opposite_m = np.abs(x_pixel_m - x_gen_matrix_m)
    adjacent_m = z_pixel_m
    gen_angle_matrix_deg = np.rad2deg(np.arctan2(opposite_m, adjacent_m))
    return gen_angle_matrix_deg
