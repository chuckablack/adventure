from keywords import General, allowed_directions
from replies import snarky_replies
from world.items import items


def print_location_info(location_name, location):

    print(f"""
Location Information:
    name: {location_name}
    description: {location[General.DESCRIPTION]}
    allowed directions: {[d for d in location.keys() if d in allowed_directions]}
    items: {list(location[General.ITEMS].keys())}
""")

    # print("\n")
    # print(location[General.DESCRIPTION])
    # print(location[General.LOOK])
    # print("\nItems in this location:")
    # for item in location[General.ITEMS]:
    #     print(f"--- {item}")
    # print("\n--------------------\n")


def print_item_info(item):

    print("\n--------------------")
    print(item["description"])
    print("--------------------\n")


def look(location_name, current_location, command, inventory):

    # If just 'look', print info about the current location
    if len(command) == 1:
        print_location_info(location_name, current_location)
        return

    # Otherwise, look at requested item, which must be in inventory or in the current location
    if len(command) > 1:

        if len(command) == 2:
            item_name = command[1]
        elif command[1] == General.AT:
            item_name = command[2]
        else:
            snarky_replies.print_snarky_reply_bad_look_command()
            return

        # Make sure we have this item in inventory or in the room
        if item_name not in current_location[General.ITEMS] and item_name not in inventory:
            snarky_replies.print_snarky_reply_dont_have_item(item_name)
            return

        print_item_info(items[item_name])
