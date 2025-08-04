from functions.modbuildtfmgrid import build_tfm_grid
from functions.modbuildxelements import build_x_elements_m
from functions.modcalculatedistancesdirect import calculate_distances_direct_all_pixels_all_elements_m


class TFMConstructor:
    def __init__(self,
                 image_name_string,
                 n_elements,
                 pitch_mm,
                 grid_size_x_mm,
                 grid_size_z_mm,
                 n_pixels_z,
                 material,
                 wave_type_send,
                 wave_type_receive,
                 filter_tf,
                 butter_order,
                 band_min_MHz,
                 band_max_MHz,
                 gen_mask_tf,
                 mask_angle_deg,
                 mask_behaviour_string
                 ):

        # Pin given values for variables to class instance as instance variables:
        self.n_elements = n_elements
        self.pitch_mm = pitch_mm
        self.grid_size_x_mm = grid_size_x_mm
        self.grid_size_z_mm = grid_size_z_mm
        self.n_pixels_z = n_pixels_z
        self.material = material
        self.wave_type_send = wave_type_send
        self.wave_type_receive = wave_type_receive
        self.filter_tf = filter_tf
        self.butter_order = butter_order
        self.band_min_MHz = band_min_MHz
        self.band_max_MHz = band_max_MHz
        self.gen_mask_tf = gen_mask_tf
        self.mask_angle_deg = mask_angle_deg
        self.mask_behaviour_string = mask_behaviour_string

        # Calculate some derived instance variables:
        # If a custom image name string has been give, assign it, else create a
        # default name using the given parameters.
        if image_name_string:
            self.image_name_string = image_name_string
        else:
            # No custom name given.  Build a default name:
            wave_set_string = wave_type_send.wave_type_string + '-' + wave_type_receive.wave_type_string
            filter_string = f' {band_min_MHz:g}-{band_max_MHz:g}MHz' if filter_tf else ''
            masked_string = ' masked' if gen_mask_tf else ''
            # Combine:
            self.image_name_string = wave_set_string + filter_string + masked_string

    def get_pixel_meshgrid_m(self):
        # Build pixel co-ordinate mesh grid:
        x_grid_m, z_grid_m = build_tfm_grid(self.grid_size_x_mm, self.grid_size_z_mm, self.n_pixels_z)
        return x_grid_m, z_grid_m

    def get_x_elements_m(self):
        # Build a vector of the element x coordinates using pitch and n_tx:
        x_elements_m = build_x_elements_m(self.n_elements, self.pitch_mm)
        return x_elements_m

    def get_direct_ray_distances_all_pixels_all_el_m(self):
        x_grid_m, z_grid_m = self.get_pixel_meshgrid_m()
        x_elements_m = self.get_x_elements_m()
        distances_direct_all_pixels_all_el_m = calculate_distances_direct_all_pixels_all_elements_m(x_grid_m,
                                                                                                    z_grid_m,
                                                                                                    x_elements_m)
        return distances_direct_all_pixels_all_el_m
