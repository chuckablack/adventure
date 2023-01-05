from world.locations import locations
from actions.go import go
from actions.look import look, print_location_info
from actions.show import show_inventory
from take import take
from replies import snarky_replies
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


print_help()

location_name = keywords.Location.SCHOOLHOUSE_ENTRY
current_location = locations[keywords.Location.SCHOOLHOUSE_ENTRY]
inventory = {}
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

    # ---- GO action ------------------------------------------------
    if action in keywords.go_words:
        show_new_location_info, current_location = go(current_location, command)
        continue

    # ---- LOOK action ------------------------------------------------
    elif action in keywords.look_words:
        look(current_location, command, inventory)

    # ----- TAKE action -----------------------------------------------
    elif action in keywords.take_words:
        take(current_location, command, inventory)

    # ----- SHOW action -----------------------------------------------
    elif action == keywords.Action.SHOW:
        if len(command) > 1 and command[1] == keywords.General.INVENTORY:
            show_inventory(inventory)

    else:
        print(f"sorry it seems the developer has not implemented the action {action} yet!")
