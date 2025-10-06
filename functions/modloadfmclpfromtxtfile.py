import numpy as np

from functions.modconvert2dto3dfmcformat import convert_full_matrix_numpy_2d_to_3d


def load_fmclp_from_txt_file(file_path):
    """
    Load a full matrix of displacement measurements from the .txt file at file_path.

    This function is designed to be complimentary to the numpy.savetxt() function, which can save 1D and 2D Numpy
    arrays into a delimited variable txt file.

    Given that numpy.savetxt() does not support saving 3D Numpy arrays, this function expects to load a full matrix in
    2D numpy (t, dn + g) format as a 2D numpy array, which it will then convert into 3D numpy (t, d, g) full matrix
    format.
    """
    # Default delimiter (whitespace) and newline (\n) characters, matching the default np.savetxt() function.
    displacements_fmc_2d_raw = np.loadtxt(file_path)

    # Convert 2D array FMC format into 3D array format:
    displacements_fmc_3d_v = convert_full_matrix_numpy_2d_to_3d(displacements_fmc_2d_raw)
    return displacements_fmc_3d_v