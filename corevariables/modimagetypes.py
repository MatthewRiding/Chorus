import numpy as np
import colorcet as cc
from matplotlib import colormaps as mpl_colormaps

from classdefs.modimagetype import ImageType
from functions.modgetdecibelimage import get_decibel_image_from_complex


cmap_viridis = mpl_colormaps['viridis']
cmap_cet_d07_blue_beige_yellow = cc.m_CET_D7

image_type_real = ImageType('Real', np.real, 'Max |u|', cmap_cet_d07_blue_beige_yellow)
image_type_imag = ImageType('Imag', np.imag, 'Max |u|', cmap_cet_d07_blue_beige_yellow)
image_type_abs = ImageType('Abs', np.abs, 'Max |u|', cmap_viridis, can_be_positive_and_negative=False)

image_type_dB = ImageType('dB', get_decibel_image_from_complex, 'dB min', cmap_viridis, -40)

dict_image_types = {image_type_dB.name_string:image_type_dB,
                    image_type_real.name_string:image_type_real,
                    image_type_imag.name_string:image_type_imag,
                    image_type_abs.name_string:image_type_abs}
