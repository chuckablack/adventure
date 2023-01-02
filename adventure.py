from world import locations
from go import go
from look import look, print_location_info
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

        show_new_location_info, current_location = go(current_location, command)
        continue

    # ---- LOOK action ------------------------------------------------
    elif action == keywords.Action.LOOK:

        look(current_location, command, inventory)

    else:
        print(f"sorry it seems the developer has not implemented the action {action} yet!")
