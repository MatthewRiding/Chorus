import numpy as np

from functions.modconvert2dto3dfullmatrixformats import convert_2d_dnplusgt_to_3d_dgt


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
    displacements_2d_dnplusgt_raw = np.loadtxt(file_path)

    # Convert 2D array FMC format into 3D array format:
    displacements_3d_dgt_raw = convert_2d_dnplusgt_to_3d_dgt(displacements_2d_dnplusgt_raw)
    return displacements_3d_dgt_raw