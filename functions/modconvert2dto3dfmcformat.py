import numpy as np


def convert_full_matrix_numpy_2d_to_numpy_3d(displacements_numpy_2d):
    """
    Convert a full matrix of displacement measurements from 2D numpy format (t, dn + g)

    :param displacements_numpy_2d: The full matrix of displacement measurements in 2D numpy format (t, dn + g)
    :return: The full matrix of displacement measurements in 3D numpy format (t, d, g).
    """
    # The fmclp in 2d-arry format will have a number of columns equal to n_tx^2:
    n_samples = np.shape(displacements_numpy_2d)[0]
    n_a_scans = np.shape(displacements_numpy_2d)[1]
    n_tx = int(np.sqrt(n_a_scans))

    # Re-shape the 2d-array into the equivalent 3d-array format:
    displacements_numpy_3d = np.reshape(displacements_numpy_2d, (n_samples, n_tx, n_tx))

    return displacements_numpy_3d


def convert_full_matrix_matlab_2d_to_numpy_3d(displacements_numpy_2d):
    """
    Convert a full matrix of displacement measurements from 2D numpy format (t, dn + g)

    :param displacements_numpy_2d: The full matrix of displacement measurements in 2D numpy format (t, dn + g)
    :return: The full matrix of displacement measurements in 3D numpy format (t, d, g).
    """
    # The fmclp in 2d-arry format will have a number of columns equal to n_tx^2:
    n_samples = np.shape(displacements_numpy_2d)[0]
    n_a_scans = np.shape(displacements_numpy_2d)[1]
    n_tx = int(np.sqrt(n_a_scans))

    # Re-shape the 2d-arry into the equivalent fmclp in 3d-array format:
    displacements_numpy_3d = np.reshape(displacements_numpy_2d, (n_samples, n_tx, n_tx))

    return displacements_numpy_3d
