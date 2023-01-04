from world.locations import locations
import snarky_replies
import keywords


def go(current_location, command):

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

