from world import locations
from go import go
import snarky_replies
import keywords


def print_help():

    print("\n--------------------")
    print("Adventure commands look like the following: <action> <option>")
    print(f"    ... where <action> can be one of: {keywords.Action.GO}")
    print(f"                                      {keywords.Action.USE}")
    print(f"                                      {keywords.Action.LEAVE}")
    print(f"                                      {keywords.Action.TAKE}")
    print(f"                                      {keywords.Action.LOOK}")
    print("The <option> depends on the <action>. Some examples:")
    print(f"         {keywords.Action.GO}: north, south, east, west")
    print(f"         {keywords.Action.TAKE}: <name of item being taken>")
    print(f"         {keywords.Action.LEAVE}: <name of item being left>")
    print(f"         {keywords.Action.USE}: <name of item being used>")
    print("Enjoy, and good luck!")
    print("--------------------\n")


def print_location_info(location):

    print("\n--------------------")
    print(location["description"])
    print("--------------------\n")


def print_look_info(location):

    print("\n--------------------")
    print(location["look"])
    print("--------------------\n")


print_help()

location_name = "main_entry"
current_location = locations["main_entry"]
inventory = []
show_new_location_info = True

while True:

    if show_new_location_info:
        print_location_info(current_location)
        show_new_location_info = False

    command_string = ""
    while command_string == "":
        command_string = input("-- adventure -- #  ")
    if command_string == "exit":
        print("\n\nsee ya later...\n\n")
        exit()

    command = command_string.lower().split()

    action = command[0]

    if action not in keywords.allowed_actions:
        snarky_replies.print_snarky_reply_bad_action()
        continue

    # ---- GO action ------------------------------------------------
    if action == keywords.Action.GO:

        # direction = command[1]
        # if direction not in keywords.allowed_directions:
        #     snarky_replies.print_snarky_reply_bad_direction_name()
        #     continue
        #
        # if direction not in current_location:
        #     snarky_replies.print_snarky_reply_bad_direction()
        #     continue
        #
        # new_location = current_location[direction]
        # if new_location not in locations:
        #     snarky_replies.print_snarky_reply_bad_world(new_location)
        #     continue
        #
        # current_location = locations[new_location]
        # show_new_location_info = True

        show_new_location_info, current_location = go(current_location, command)
        continue

    # ---- LOOK action ------------------------------------------------
    elif action == keywords.Action.LOOK:

        print_look_info(current_location)

    else:
        print(f"sorry it seems the developer has not implemented the action {action} yet!")
