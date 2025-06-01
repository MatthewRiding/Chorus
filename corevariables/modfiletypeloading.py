import numpy as np

from functions.modloadfmclpfrommatfile import load_fmclp_from_mat_file
from functions.modloadfmclpfromtxtfile import load_fmclp_from_txt_file

dict_loading_functions = {'.mat': load_fmclp_from_mat_file,
                          '.npy': np.load,
                          '.txt': load_fmclp_from_txt_file}