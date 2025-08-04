import numpy as np


from functions.modbuildxelements import build_x_elements_m
from functions.modcalculatecriticalangle import calculate_critical_angle_radians
from functions.modbuildxgenandxdetmatrices import build_x_gen_and_x_det_matrices_m


class ListedTFMImage:
    def __init__(self, worker_id, tfm_constructor, n_tx):

        # Define instance variables:
        self.worker_id = worker_id
        self.tfm_constructor = tfm_constructor
        self.n_tx = n_tx

        # Make space for instance variables not assigned in constructor:
        self.image_decibels = None
        self.fmc_3d_filtered = None
        self.progress_string = None
        self.complete = False
        self.x_gen_matrix_m = None
        self.x_det_matrix_m = None

        # Build instance variables derived from tfm_constructor:
        self.x_gen_matrix_m, self.x_det_matrix_m = build_x_gen_and_x_det_matrices_m(self.n_tx, self.tfm_constructor.pitch_mm)
        self.angle_critical_radians = calculate_critical_angle_radians(self.tfm_constructor.v_l_mpers,
                                                                       self.tfm_constructor.v_t_mpers)

    def completed(self):
        self.progress_string = ''
        self.complete = True

    def get_display_string(self):
        return self.tfm_constructor.image_name_string + self.progress_string
