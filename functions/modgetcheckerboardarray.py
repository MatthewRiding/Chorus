import numpy as np


def get_checkerboard_array(grid_width_x_mm, grid_height_z_mm, n_pixels_z):
    """Build a 2D numpy array with alternating 1 and 0 values, representing a TFM pixel grid."""
    # Calculate n_pixels_x from default grid parameters:
    # Calculate pixel size:
    pixel_size_mm = grid_height_z_mm / n_pixels_z
    n_pixels_x = np.floor_divide(grid_width_x_mm, pixel_size_mm)
    shape = (int(n_pixels_z), int(n_pixels_x))
    checkerboard_array = np.indices(shape).sum(axis=0) % 2
    return checkerboard_array