import numpy as np

from functions.modcalculatedirectrayangles import calculate_direct_ray_angles_all_pixels_single_el_radians


class IsochronManager:
    def __init__(self, tfm_image_widget):
        self.tfm_image_widget = tfm_image_widget
        # Instance variables assigned in methods:
        self.selected_tfm_image = None
        self.aperture_mm = None
        self.travel_times_send_s = None
        self.travel_times_receive_s = None
        self.travel_times_total_s = None
        self.time_selected_s = None
        self.datapoint_selected = False

    def update_selected_tfm_image(self, selected_tfm_image):
        self.selected_tfm_image = selected_tfm_image
        if selected_tfm_image:
            self.aperture_mm = self.selected_tfm_image.tfm_constructor.get_aperture_mm()
        if self.datapoint_selected:
            self.tfm_image_widget.clear_isochron()
            self.datapoint_selected = False

    def iso_time_click_response(self, coords_tuple):
        # If no TFM image is selected, do nothing:
        if self.selected_tfm_image:
            if self.selected_tfm_image.complete:
                # Check if the tuple contains None values, which are a request to clear the isochron plot:
                if coords_tuple[0] is None:
                    self.datapoint_selected = False
                    self.tfm_image_widget.clear_isochron()
                else:
                    self.datapoint_selected = True
                    # Compute the new travel times:
                    # A click in the iso-time widget canvas specifies a new i_gen and a new i_det.
                    i_gen_float, i_det_float = coords_tuple
                    self.update_send_travel_times_from_i_gen(i_gen_float)
                    self.update_receive_travel_times_from_i_det(i_det_float)
                    # Update total travel times by summing send and receive legs, and filling with -10 where masked:
                    # mask_send = np.ma.getmask(self.travel_times_send_s)
                    # mask_receive = np.ma.getmask(self.travel_times_receive_s)
                    # mask_combined = np.ma.mask_or(mask_send, mask_receive)
                    # travel_times_total_masked_s = np.ma.masked_where(mask_combined,
                    #                                                  (self.travel_times_send_s + self.travel_times_receive_s),
                    #                                                  copy=False)
                    # self.travel_times_total_s = np.ma.filled(travel_times_total_masked_s, -10)
                    self.travel_times_total_s = self.travel_times_send_s + self.travel_times_receive_s
                    # Plot the new isochron in the TFM image widget:
                    self.update_isochron_plot()
            else:
                self.datapoint_selected = False
                self.tfm_image_widget.clear_isochron()
        else:
            self.datapoint_selected = False
            self.tfm_image_widget.clear_isochron()

    def selected_time_changed(self, time_selected_s):
        self.time_selected_s = time_selected_s
        if self.datapoint_selected:
            self.update_isochron_plot()

    def update_send_travel_times_from_i_gen(self, i_gen_float):
        # Convert i_gen from index into x_coordinate:
        x_gen_m = self.convert_element_index_to_x_coordinate(i_gen_float)
        # Compute new send travel times:
        wave_type_send = self.selected_tfm_image.tfm_constructor.wave_type_send
        travel_times_send_s = wave_type_send.func_calculate_travel_times_all_pixels_single_el_s(
            self.selected_tfm_image.x_grid_m, self.selected_tfm_image.z_grid_m, x_gen_m,
            self.selected_tfm_image.tfm_constructor)

        # Apply gen mask if requested:
        if self.selected_tfm_image.tfm_constructor.mask_spec_gen:
            mask_spec_gen = self.selected_tfm_image.tfm_constructor.mask_spec_gen
            # Apply mask to the delay matrix based on send ray angle:
            gen_angle_matrix_deg = calculate_direct_ray_angles_all_pixels_single_el_radians(
                self.selected_tfm_image.x_grid_m, self.selected_tfm_image.z_grid_m, x_gen_m)
            # Use the logic of the chosen mask behaviour:
            numpy_masking_function_gen = mask_spec_gen.mask_behaviour.numpy_masking_function
            gen_angle_matrix_masked = numpy_masking_function_gen(gen_angle_matrix_deg,
                                                                 np.deg2rad(mask_spec_gen.mask_angle_deg))
            mask_matrix_gen = np.ma.getmask(gen_angle_matrix_masked)
        else:
            mask_matrix_gen = np.ma.nomask

        # Apply mask to send travel times:
        self.travel_times_send_s = np.ma.masked_where(mask_matrix_gen, travel_times_send_s, copy=False)

    def update_receive_travel_times_from_i_det(self, i_det_float):
        # Convert i_det from index into x_coordinate:
        x_det_m = self.convert_element_index_to_x_coordinate(i_det_float)
        # Compute new receive travel times:
        wave_type_receive = self.selected_tfm_image.tfm_constructor.wave_type_receive
        travel_times_receive_s = wave_type_receive.func_calculate_travel_times_all_pixels_single_el_s(
            self.selected_tfm_image.x_grid_m, self.selected_tfm_image.z_grid_m, x_det_m,
            self.selected_tfm_image.tfm_constructor)

        # Apply det mask if requested:
        if self.selected_tfm_image.tfm_constructor.mask_spec_det:
            mask_spec_det = self.selected_tfm_image.tfm_constructor.mask_spec_det
            # Apply mask to the delay matrix based on send ray angle:
            det_angle_matrix_deg = calculate_direct_ray_angles_all_pixels_single_el_radians(
                self.selected_tfm_image.x_grid_m, self.selected_tfm_image.z_grid_m, x_det_m)
            # Use the logic of the chosen mask behaviour:
            numpy_masking_function_det = mask_spec_det.mask_behaviour.numpy_masking_function
            det_angle_matrix_masked = numpy_masking_function_det(det_angle_matrix_deg,
                                                                 np.deg2rad(mask_spec_det.mask_angle_deg))
            mask_matrix_det = np.ma.getmask(det_angle_matrix_masked)
        else:
            mask_matrix_det = np.ma.nomask

        # Apply mask to send travel times:
        self.travel_times_receive_s = np.ma.masked_where(mask_matrix_det, travel_times_receive_s, copy=False)

    def convert_element_index_to_x_coordinate(self, index):
        # Assuming a linear, periodic array:
        x_index_m = (((index / self.selected_tfm_image.tfm_constructor.n_elements) * self.aperture_mm)
                     - self.aperture_mm / 2) * 10 ** -3
        return x_index_m

    def update_isochron_plot(self):
        # Update contour plot on tfm_image_widget:
        self.tfm_image_widget.update_isochron(self.selected_tfm_image.x_grid_m / 10 ** -3,
                                              self.selected_tfm_image.z_grid_m / 10 ** -3,
                                              self.travel_times_total_s, self.time_selected_s)
