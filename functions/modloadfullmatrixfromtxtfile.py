import numpy as np

from functions.modreshape2dto3dfullmatrixformats import reshape_2d_dnplusgt_to_3d_dgt


def load_full_matrix_from_txt_file(file_path):
    """
    Load a full matrix of displacement measurements from the .txt file at file_path.

    This function is designed to be complimentary to the numpy.savetxt() function, which can save 1D and 2D Numpy
    arrays into a delimited variable txt file.

    Given that numpy.savetxt() does not support saving 3D Numpy arrays, this function expects to load a full matrix in
    2D numpy[dn+g,t] format as a 2D numpy array, which it will then convert into 3D numpy[d,g,t] full matrix
    format.
    """
    # Default delimiter (whitespace) and newline (\n) characters, matching the default np.savetxt() function.
    displacements_2d_dnplusgt_raw = np.loadtxt(file_path)

    # Convert 2D array FMC format into 3D array format:
    displacements_3d_dgt_raw = reshape_2d_dnplusgt_to_3d_dgt(displacements_2d_dnplusgt_raw)
    return displacements_3d_dgt_raw