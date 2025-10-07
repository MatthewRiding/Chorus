import numpy as np

from functions.modreshape2dto3dfullmatrixformats import reshape_2d_dnplusgt_to_3d_dgt


def load_full_matrix_from_npy_file(file_path):
    """
    Load a full matrix of displacement measurements from a numpy .npy file.

    Expected formats of ndarray returned when np.load() is called passing file_path:
    - If 2D: numpy[dn+g,t] format.
    - If 3D: numpy[d,g,t] format.
    The number of dimensions of the ndarry returned by np.load() is automatically measured, and if 2D, reshaping to
    3D numpy[d,g,t] format is performed (assuming 2D numpy[dn+g,t] format).

    :param file_path: File path to .npy file.
    :return: Full matrix of displacement measurements in 3D numpy[d,g,t] format.
    """
    # Call numpy.load() function on file_path:
    displacement_array = np.load(file_path)

    # Measure number of dimensions:
    if np.ndim(displacement_array) == 2:
        # The ndarray returned by np.load() is 2D.
        # ASSUMPTION: This 2D ndarray is in numpy[dn+g,t] format.
        # Reshape to the target numpy[d,g,t] format:
        displacement_array_3d_dgt = reshape_2d_dnplusgt_to_3d_dgt(displacement_array)
    else:
        # ASSUMPTION: If not 2D, the ndarray is assumed to be 3D and already in numpy[d,g,t] format.
        displacement_array_3d_dgt = displacement_array

    return displacement_array_3d_dgt
