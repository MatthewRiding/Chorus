import numpy as np

from classdefs.modmaskbehaviour import MaskBehaviour

dict_mask_behaviours = {'Ignore above': MaskBehaviour(np.ma.masked_greater,
                                                      True,
                                                      False),
                        'Ignore below': MaskBehaviour(np.ma.masked_less,
                                                      True,
                                                      False),
                        'Flip above': MaskBehaviour(np.ma.masked_greater,
                                                    False,
                                                    True),
                        'Flip below': MaskBehaviour(np.ma.masked_less,
                                                    False,
                                                    True)}
