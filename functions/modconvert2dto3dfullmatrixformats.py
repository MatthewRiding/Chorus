import numpy as np


def convert_2d_dnplusgt_to_3d_dgt(displacements_2d_dnplusgt):
    """
    Convert a full matrix of displacement measurements from 2D numpy format numpy[dn+g,t] to 3D numpy format numpy[d,g,t]

    :param displacements_2d_dnplusgt: The full matrix of displacement measurements in 2D numpy format numpy[dn+g,t]
    :return: The full matrix of displacement measurements in 3D numpy format numpy[d,g,t].
    """
    shape_2d_dnplusgt = np.shape(displacements_2d_dnplusgt)
    # The 1D, periodic full matrix in 2d numpy[dn+g,t] format should have a number of rows equal to n_tx^2:
    n_a_scans = shape_2d_dnplusgt[0]
    n_tx = int(np.sqrt(n_a_scans))
    # Likewise, a single row of the 2d numpy[dn+g,t] format should contain the displacement measurements for a single
    # A-scan.
    n_samples = shape_2d_dnplusgt[1]

    # Re-shape into 3D numpy[d,g,t] format:
    displacements_3d_dgt = np.reshape(displacements_2d_dnplusgt, (n_tx, n_tx, n_samples));

    return displacements_3d_dgt


def convert_2d_tdnplusg_to_3d_dgt(displacements_2d_tdnplusg):
    """
    Convert a full matrix of displacement measurements from 2D numpy format numpy[t,dn+g] to 3D numpy format numpy[d,g,t].

    This conversion is useful for importing full matrix data from MATLAB, as the column-major MATLAB 2D full matrix
    format MATLAB(t,dn+g+1) is imported as an ndarray with numpy[t,dn+g] format.

    :param displacements_2d_tdnplusg: The full matrix of displacement measurements in 2D format numpy[t,dn+g].
    :return: The full matrix of displacement measurements in 3D format numpy(t,d,g).
    """
    # Transpose numpy[t,dn+g] format to give numpy[dn+g,t] format.  Then pass transposed array to function converting
    # numpy[dn+g,t] format to numpy[d,g,t] format:
    displacements_3d_dgt = convert_2d_dnplusgt_to_3d_dgt(displacements_2d_tdnplusg.T)

    return displacements_3d_dgt
