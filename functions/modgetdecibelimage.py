import numpy as np


def get_decibel_image(image_complex):
    # Convert intensity to root-power decibels by normalising relative to a maximum intensity value.
    # To avoid saturation by SAW crosstalk, ignore pixels in the upper third of the image.
    n_pixels_z = np.shape(image_complex)[0]
    row_index_below_which_to_max = round(n_pixels_z / 3)
    reference_amplitude_0db = np.max(np.abs(image_complex[row_index_below_which_to_max:, :]))

    # Convert to root-power dB using this reference amplitude:
    image_decibels = 20 * np.log10(np.abs(image_complex) / reference_amplitude_0db)
    return image_decibels
