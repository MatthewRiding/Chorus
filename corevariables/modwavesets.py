from classdefs.modwaveset import WaveSet
from functions.xztraveltimefunctions.modtraveltimeswavesets import (calculate_xz_travel_times_ll,
                                                                    calculate_xz_travel_times_tt,
                                                                    calculate_xz_travel_times_lt,
                                                                    calculate_xz_travel_times_tl,
                                                                    calculate_xz_travel_times_hl,
                                                                    calculate_xz_travel_times_ht)
from functions.delaylawfunctions.moddelaylawfunctions import (calculate_delay_law_ll,
                                                              calculate_delay_law_tt,
                                                              calculate_delay_law_lt,
                                                              calculate_delay_law_tl,
                                                              calculate_delay_law_hl,
                                                              calculate_delay_law_ht)


# Place the travel time calculation functions into a dictionary, each keyed by a short wave set string:
dict_wave_sets = {'L-L': WaveSet(travel_time_function=calculate_xz_travel_times_ll,
                                 delay_law_function=calculate_delay_law_ll),
                  'T-T': WaveSet(travel_time_function=calculate_xz_travel_times_tt,
                                 delay_law_function=calculate_delay_law_tt),
                  'L-T': WaveSet(travel_time_function=calculate_xz_travel_times_lt,
                                 delay_law_function=calculate_delay_law_lt),
                  'T-L': WaveSet(travel_time_function=calculate_xz_travel_times_tl,
                                 delay_law_function=calculate_delay_law_tl),
                  'H-L': WaveSet(travel_time_function=calculate_xz_travel_times_hl,
                                 delay_law_function=calculate_delay_law_hl),
                  'H-T': WaveSet(travel_time_function=calculate_xz_travel_times_ht,
                                 delay_law_function=calculate_delay_law_ht)
                  }
