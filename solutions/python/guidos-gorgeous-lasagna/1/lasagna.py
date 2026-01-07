EXPECTED_BAKE_TIME = 40
PREPARATION_TIME = 2

def bake_time_remaining(elapsed_bake_time):
    """Calculate the bake time remaining.
    
    :param elapsed_bake_time: int - baking time already elapsed.
    :return: int - remaining bake time (in minutes) derived from 'EXPECTED_BAKE_TIME'.
    """
    return EXPECTED_BAKE_TIME - elapsed_bake_time

def preparation_time_in_minutes(number_of_layers):
    """Calculate the preparation time in minutes.
    
    :param number_of_layers: int - the number of layers in the lasagna.
    :return: int - total preparation time (in minutes) based on the number of layers.
    """
    return number_of_layers * PREPARATION_TIME

def elapsed_time_in_minutes(number_of_layers, elapsed_bake_time):
    """Calculate the total elapsed cooking time.
    
    :param number_of_layers: int - the number of layers added to the lasagna.
    :param elapsed_bake_time: int - the number of minutes the lasagna has been baking in the oven.
    :return: int - total number of minutes you've been cooking.
    """
    return preparation_time_in_minutes(number_of_layers) + elapsed_bake_time

