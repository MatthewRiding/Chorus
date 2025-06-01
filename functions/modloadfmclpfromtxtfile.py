import numpy as np

from functions.modconvert2dto3dfmcformat import convert_2d_to_3d_fmclp_format


def load_fmclp_from_txt_file(file_path):
    # Load the contents of the .txt file as a 2D NumPy array:
    # Default delimiter (whitespace) and newline (\n) characters, matching the default np.savetxt() function.
    fmc_2d = np.loadtxt(file_path)

    # Convert 2D array FMC format into 3D array format:
    fmc_3d = convert_2d_to_3d_fmclp_format(fmc_2d)
    return fmc_3d