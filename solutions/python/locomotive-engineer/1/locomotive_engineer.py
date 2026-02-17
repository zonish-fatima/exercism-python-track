"""Functions which helps the locomotive engineer to keep track of the train."""


def get_list_of_wagons(*args):
    """Return a list of wagons.

    :param: arbitrary number of wagons.
    :return: list - list of wagons.
    """
    return list(args)


def fix_list_of_wagons(each_wagons_id, missing_wagons):
    """Fix the list of wagons.

    :param each_wagons_id: list - the list of wagons.
    :param missing_wagons: list - the list of missing wagons.
    :return: list - list of wagons.
    """
    list_one = each_wagons_id[2:] + each_wagons_id[:2]
    
    # Find locomotive position
    loco_index = list_one.index(1)
    
    # Insert second list after locomotive
    fixed_list = (
        list_one[:loco_index + 1] +
        missing_wagons +
        list_one[loco_index + 1:]
    )
    
    return fixed_list


def add_missing_stops(routing_dict, **kwargs):
    """Add missing stops to route dict.

    :param route: dict - the dict of routing information.
    :param: arbitrary number of stops.
    :return: dict - updated route dictionary.
    """
    stops_list = list(kwargs.values())
    routing_dict["stops"] = stops_list
    return routing_dict


def extend_route_information(route, more_route_information):
    """Extend route information with more_route_information.

    :param route: dict - the route information.
    :param more_route_information: dict -  extra route information.
    :return: dict - extended route information.
    """
    combined_routes_information = {**route, **more_route_information}
    return combined_routes_information


def fix_wagon_depot(wagons_rows):
    """Fix the list of rows of wagons.

    :param wagons_rows: list[list[tuple]] - the list of rows of wagons.
    :return: list[list[tuple]] - list of rows of wagons.
    """
    fixed_grid = []
    
    # There are 3 positions in each row
    for i in range(3):
        new_row = [
            wagons_rows[0][i],
            wagons_rows[1][i],
            wagons_rows[2][i]
        ]
        fixed_grid.append(new_row)
    
    return fixed_grid
