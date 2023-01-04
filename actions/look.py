import keywords
import snarky_replies


def print_location_info(location):

    print("\n--------------------\n")
    print(location["description"])
    print("\nItems in this location:")
    for item in location[keywords.General.ITEMS]:
        print(f"--- {item}")
    print("\n--------------------\n")


def print_item_info(item):

    print("\n--------------------")
    print(item["description"])
    print("--------------------\n")


def look(current_location, command, inventory):

    # If just 'look', print info about the current location
    if len(command) == 1:
        print_location_info(current_location)
        return

    # Otherwise, look at requested item, which must be in inventory or in the current location
    if len(command) > 1:

        if len(command) == 2:
            item_name = command[1]
        elif command[1] == keywords.General.AT:
            item_name = command[2]
        else:
            snarky_replies.print_snarky_reply_bad_look_command()
            return

        # Make sure we have this item in inventory or in the room
        if item_name not in current_location[keywords.General.ITEMS] and item_name not in inventory:
            snarky_replies.print_snarky_reply_dont_have_item(item_name)
            return

        print_item_info(world.items[item_name])
