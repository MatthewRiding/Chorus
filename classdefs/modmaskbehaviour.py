class MaskBehaviour:
    def __init__(self, numpy_masking_function, apply_mask_during_summing, flip_polarity_where_masked):
        self.numpy_masking_function = numpy_masking_function
        self.apply_mask_during_summing = apply_mask_during_summing
        self.flip_polarity_where_masked = flip_polarity_where_masked
