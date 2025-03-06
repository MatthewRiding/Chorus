import numpy as np


def create_time_plane_coords(n_tx, time_us):
    x_coords = np.array([[0, n_tx], [0, n_tx]])
    y_coords = np.array([[0, 0], [n_tx, n_tx]])
    z_coords = np.ones([2, 2]) * time_us
    return x_coords, y_coords, z_coords
