import numpy as np

from functions.modconvert2dto3dfmcformat import convert_2d_to_3d_fmclp_format


def load_fmclp_from_txt_file(file_path):
    # Load the contents of the .txt file as a 2D NumPy array:
    # Default delimiter (whitespace) and newline (\n) characters, matching the default np.savetxt() function.
    displacements_fmc_2d_v = np.loadtxt(file_path)

    # The recorded displacement measurements are assumed to be in units of volts, output
    # from the Sound and Bright Quartet.

    # Convert 2D array FMC format into 3D array format:
    displacements_fmc_3d_v = convert_2d_to_3d_fmclp_format(displacements_fmc_2d_v)
    return displacements_fmc_3d_v