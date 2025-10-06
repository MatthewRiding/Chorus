from scipy.io import loadmat
import numpy as np

from functions.modgetvariablekeysfrommatcontentsdict import get_variable_keys_from_mat_contents_dict
from functions.modconvert2dto3dfullmatrixformats import convert_full_matrix_numpy_2d_to_3d


def load_full_matrix_from_mat_file(file_path_mat):
    """
    Loads a full matrix of displacement measurements from a MATLAB .mat data file.

    This function assumes the .mat file contains only one variable, and that variable is the array of displacement
    measurements.

    The number of dimensions of the data array contained in the .mat file are measured.  If 2D, automatic re-shaping to
    3D numpy[d,g,t] format is performed assuming the original MATLAB array had MATLAB(t, dn + g + 1) format.  If 3D,
    this function automatically transposes the array assuming it is in MATLAB(t, g, d) format, to give a numpy ndarray
    in numpy[d,g,t] format.  See the data format guides on the Chorus wiki for more context and descriptions of these
    formats, and the differences between MATLAB (column-major) and Numpy (row-major) arrays.

    Note: This function uses the loadmat function from SciPy, which often lags in compatibility with the latest MATLAB
    file formats.  Check the documentation for scipy.io.loadmat() to see .mat version compatibility.

    :param file_path_mat: Path to a MATLAB .mat file.
    :return: Full matrix of displacement measurements as a numpy array in (d, g, t) format.
    """
    # Load the contents of the .mat file as a dictionary using scipy.io.loadmat():
    mat_contents_dict = loadmat(file_path_mat)

    # Find the variables from the .mat file by examining the keys of mat_contents_dict:
    mat_variables_keys = get_variable_keys_from_mat_contents_dict(mat_contents_dict)

    # Allocate the variables found in the .mat file to their correct workspace objects:
    # ASSUMPTION: A-scan matrix is the only variable present in the .mat file.
    displacements_fmc_raw = mat_contents_dict[mat_variables_keys[0]]

    if np.ndim(displacements_fmc_raw) == 2:
        # Convert 2D array FMC format into 3D array format:
        displacements_3d_dgt_raw = convert_full_matrix_numpy_2d_to_3d(displacements_fmc_raw)
    else:
        # Array is already 3D:
        # Transpose from MATLAB Fortran-ordered array order to Numpy C-ordered array order:
        # MATLAB: (n_rows, n_columns, n_pages)
        # Numpy: (n_pages, n_rows, n_columns)
        displacements_3d_dgt_raw = np.transpose(displacements_fmc_raw, (2, 0, 1))

    return displacements_3d_dgt_raw
