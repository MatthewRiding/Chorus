class ImageType:
    """
    Stores all information relating to a particular type of TFM image, such as a normalised image in decibels,
    or an image displaying the real part of the raw summed displacement values.
    """
    def __init__(self, name_string, conversion_function, string_slider_meaning, cmap, spinbox_min:float=0,
                 can_be_positive_and_negative=True):
        """
        Constructor for class ImageType.

        :param name_string: The name of this image type, to be used in the image types combobox.
        :param conversion_function: A function which will act on the complex summed displacement image array (units: nm)
        to produce the array that will be displayed by matplotlib's imshow in the MplCanvas.
        :param string_slider_meaning: A string that will be displayed in the QLabel above the colormap slider,
        describing the meaning of the slider's numeric output.
        :param spinbox_min: Minimum value of slider.  If negative (e.g. as needed for Decibel representation), slider is
        given inverted appearance.
        """
        self.name_string = name_string
        self.conversion_function = conversion_function
        self.string_slider_meaning = string_slider_meaning
        self.cmap = cmap
        self.spinbox_min = spinbox_min
        self.can_be_positive_and_negative = can_be_positive_and_negative

        self.slider_inverted_appearance = True if self.spinbox_min < 0 else False
