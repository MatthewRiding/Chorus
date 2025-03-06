from functions.modcalculatecriticalangle import calculate_critical_angle_degrees


def return_45(**kwargs):
    return 45


dict_mask_angles = {'Critical angle': calculate_critical_angle_degrees,
                    '45°': return_45,
                    'Manual entry': None}
