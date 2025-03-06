from classdefs.modphasorscheme import PhasorScheme
from functions.modphasorarrowcolorfuncs import colors_by_gen_index, colors_by_diagonal
from functions.modpcmsummingfuncsforphasor import sum_pcm_iso_gen_columns, sum_pcm_iso_offset_sub_diagonals


dict_phasor_schemes = {'By gen index': PhasorScheme(summing_func=sum_pcm_iso_gen_columns,
                                                    color_func=colors_by_gen_index),
                       'By diagonal': PhasorScheme(summing_func=sum_pcm_iso_offset_sub_diagonals,
                                                   color_func=colors_by_diagonal)}
