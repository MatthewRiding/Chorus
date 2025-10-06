from scipy.io import loadmat
import numpy as np

from functions.modgetvariablekeysfrommatcontentsdict import get_variable_keys_from_mat_contents_dict
from functions.modconvert2dto3dfmcformat import convert_full_matrix_numpy_2d_to_3d


def load_fmclp_from_mat_file(file_path):
    # Load the contents of the .mat file as a dictionary using scipy.io.loadmat():
    mat_contents_dict = loadmat(file_path)

    # Find the variables from the .mat file by examining the keys of mat_contents_dict:
    mat_variables_keys = get_variable_keys_from_mat_contents_dict(mat_contents_dict)

    # Allocate the variables found in the .mat file to their correct workspace objects:
    # ASSUMPTION: A-scan matrix is the only variable present in the .mat file.
    displacements_fmc_raw = mat_contents_dict[mat_variables_keys[0]]

    if np.ndim(displacements_fmc_raw) == 2:
        # Convert 2D array FMC format into 3D array format:
        displacements_fmc_3d_raw = convert_full_matrix_numpy_2d_to_3d(displacements_fmc_raw)
    else:
        # Array is already 3D:
        # Transpose from MATLAB Fortran-ordered array order to Numpy C-ordered array order:
        # MATLAB: (n_rows, n_columns, n_pages)
        # Numpy: (n_pages, n_rows, n_columns)
        displacements_fmc_3d_raw = np.transpose(displacements_fmc_raw, (2, 0, 1))

    return displacements_fmc_3d_raw
