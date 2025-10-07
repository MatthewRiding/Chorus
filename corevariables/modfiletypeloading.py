import numpy as np

from functions.modloadfullmatrixfrommatfile import load_full_matrix_from_mat_file
from functions.modloadfullmatrixfromtxtfile import load_full_matrix_from_txt_file

dict_loading_functions = {'.mat': load_full_matrix_from_mat_file,
                          '.npy': np.load,
                          '.txt': load_full_matrix_from_txt_file}