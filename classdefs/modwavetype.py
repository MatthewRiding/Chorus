from functions.delayfuncstfm.mod


class WaveType:
    def __init__(self, wave_type_string):
        # Assign instance variables from given parameters:
        self.wave_type_string = wave_type_string

    def get_travel_times_tfm_s(self, tfm_constructor):
        delay_function_all_pixels_all_el = dict_delay_funcs_tfm[self.wave_type_string]
        travel_timess_all_pixels_all_el_s = delay_function_all_pixels_all_el(tfm_constructor)
        return travel_timess_all_pixels_all_el_s

    def get_travel_times_cheops(self, x_pixel_m, z_pixel_m, x_gen_matrix_m, x_det_matrix_m,
                                tfm_constructor):
        delay_function_single_pixel_all_gd = dict_delay_funcs_cheops[self.wave_type_string]
        travel_times_single_pixel_all_gd_s = delay_function_single_pixel_all_gd(x_pixel_m, z_pixel_m,
                                                                                x_gen_matrix_m, x_det_matrix_m,
                                                                                tfm_constructor)
        return travel_times_single_pixel_all_gd_s
