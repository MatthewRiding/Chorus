import numpy as np

from classdefs.modmaskbehaviour import MaskBehaviour


mask_behaviour_ignore_above = MaskBehaviour('Ignore above', np.ma.masked_greater)
mask_behaviour_ignore_below = MaskBehaviour('Ignore below', np.ma.masked_less)

dict_mask_behaviours = {mask_behaviour_ignore_above.string_name: mask_behaviour_ignore_above,
                        mask_behaviour_ignore_below.string_name: mask_behaviour_ignore_below}
