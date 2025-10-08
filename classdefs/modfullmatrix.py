import numpy as np


class FullMatrixLinearPeriodic:
    """
    A class to store all data and methods associated with full A-scan matrices captured from linear, periodic
    (constant pitch) arrays where both generation and detection are performed across a common set of array points.
    """
    def __init__(self, displacements_3d_dgt_nm, t_min_us, t_max_us):
        """
        :param displacements_3d_dgt_nm: A full matrix of displacement measurements in numpy[d,g,t] format.
        :param t_min_us: The time stamp of the first displacement measurement in each A-scan.
        :param t_max_us: The time stamp of the last displacement measurement in each A-scan.
        """
        self.displacements_3d_dgt_nm = displacements_3d_dgt_nm
        self.t_min_us = t_min_us
        self.t_max_us = t_max_us

        # Measure parameters from fmc_3d shape:
        self.n_elements, _, self.n_samples = np.shape(self.displacements_3d_dgt_nm)

        # Create time vector from limits:
        # Create an evenly spaced time vector using the min and max time values:
        self.time_vector_us = np.linspace(self.t_min_us, self.t_max_us, self.n_samples, endpoint=True)

        # Calculate the sampling period in us:
        self.period_sampling_us = self.time_vector_us[1] - self.time_vector_us[0]

        # Calculate the sampling frequency in Hz:
        self.frequency_sampling_hz = 1 / (self.period_sampling_us * 10 ** -6)
