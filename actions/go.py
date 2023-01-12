from world.locations import locations
from world.areas import areas
from replies import snarky_replies
from keywords import General, allowed_directions, allowed_areas


def go(location_name, command):

    current_location = locations[location_name]
    if len(command) == 1:
        print(f"allowed directions: {[d for d in current_location.keys() if d in allowed_directions]}")
        return False, location_name

    # ----- Handle 'go to <area>' -------------------------------------
    if command[1] == General.TO:

        if len(command) == 2 or command[2] not in allowed_areas:
            snarky_replies.print_snarky_reply_bad_go_to_area()
            return False, location_name

        area_name = command[2]
        new_location_name = areas[area_name][General.DEFAULT_LOCATION]
        if new_location_name not in locations:
            snarky_replies.print_snarky_reply_bad_world(new_location_name)
            return False, location_name

        return True, new_location_name

    # ----- Handle 'go <direction>' -----------------------------------
    direction = command[1]
    if direction not in allowed_directions:
        snarky_replies.print_snarky_reply_bad_direction_name()
        return False, location_name

    if direction not in current_location:
        snarky_replies.print_snarky_reply_bad_direction()
        return False, location_name

    new_location_name = current_location[direction]
    if new_location_name not in locations:
        snarky_replies.print_snarky_reply_bad_world(new_location_name)
        return False, location_name

    return True, new_location_name
