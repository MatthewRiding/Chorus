import colorcet as cc
import numpy as np


def colors_by_gen_index(n_tx: int):
    colors_for_one_row = cc.m_rainbow(np.linspace(0, 1, n_tx))
    colors_for_fmc = np.tile(colors_for_one_row, (n_tx, 1))
    return colors_for_fmc


def colors_by_diagonal(n_tx: int):
    colors_increasing = cc.m_rainbow(np.linspace(0, 1, n_tx))
    colors_for_fmc = np.empty((n_tx**2, 4))
    # Assign the colors for each row using a for loop:
    for i in range(n_tx):
        colors_row_i = np.empty((n_tx, 4))
        # Assign reversed components:
        colors_row_i[0:i] = np.flipud(colors_increasing[1:(i+1)])
        # Assign increasing components:
        colors_row_i[i:n_tx] = colors_increasing[0:(n_tx-i)]
        # Add the colors for this row to the output array:
        output_row_start_index = n_tx * i
        colors_for_fmc[output_row_start_index: (output_row_start_index + n_tx)] = colors_row_i
    return colors_for_fmc
