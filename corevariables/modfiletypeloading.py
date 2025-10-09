import numpy as np

from functions.modloadfullmatrixfromnpyfile import load_full_matrix_from_npy_file
from functions.modloadfullmatrixfromtxtfile import load_full_matrix_from_txt_file
from functions.modloadfullmatrixfrommatfile import load_full_matrix_from_mat_file

dict_loading_functions = {'.npy': load_full_matrix_from_npy_file,
                          '.txt': load_full_matrix_from_txt_file,
                          '.mat': load_full_matrix_from_mat_file}