from functions.modcalculatecriticalangle import (calculate_critical_angle_radians,
                                                 calculate_critical_angle_degrees)


class Material:
    def __init__(self, c_l_mpers, c_t_mpers, c_lsaw_mpers=None):
        self.c_l_mpers = c_l_mpers
        self.c_t_mpers = c_t_mpers
        self.c_lsaw_mpers = c_lsaw_mpers

    def get_critical_angle_radians(self):
        critical_angle_radians = calculate_critical_angle_radians(self.c_l_mpers, self.c_t_mpers)
        return critical_angle_radians

    def get_critical_angle_degrees(self):
        critical_angle_degrees = calculate_critical_angle_degrees(self.c_l_mpers, self.c_t_mpers)
        return critical_angle_degrees