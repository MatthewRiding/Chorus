import numpy as np


def calculate_critical_angle_radians(c_l_mpers, c_t_mpers):
    angle_critical_radians = np.arcsin(c_t_mpers / c_l_mpers)
    return angle_critical_radians


def calculate_critical_angle_degrees(c_l_mpers, c_t_mpers):
    angle_critical_degrees = np.rad2deg(calculate_critical_angle_radians(c_l_mpers, c_t_mpers))
    return angle_critical_degrees
