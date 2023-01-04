from world.locations import locations
from world.areas import areas
from replies import snarky_replies
import keywords


def go(current_location, command):

    if len(command) == 1:
        snarky_replies.print_snarky_reply_bad_direction_name()
        return False, current_location

    # ----- Handle 'go to <area>' -------------------------------------
    if command[1] == keywords.General.TO:

        if len(command) == 2 or command[2] not in keywords.allowed_areas:
            snarky_replies.print_snarky_reply_bad_go_to_area()
            return False, current_location

        area_name = command[2]
        new_location = areas[area_name][keywords.General.DEFAULT_LOCATION]
        if new_location not in locations:
            snarky_replies.print_snarky_reply_bad_world(new_location)
            return False, current_location

        return True, locations[new_location]

    # ----- Handle 'go <direction>' -----------------------------------
    direction = command[1]
    if direction not in keywords.allowed_directions:
        snarky_replies.print_snarky_reply_bad_direction_name()
        return False, current_location

    if direction not in current_location:
        snarky_replies.print_snarky_reply_bad_direction()
        return False, current_location

    new_location = current_location[direction]
    if new_location not in locations:
        snarky_replies.print_snarky_reply_bad_world(new_location)
        return False, current_location

    return True, locations[new_location]

