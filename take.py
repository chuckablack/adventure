import keywords
import snarky_replies


def take(current_location, command, inventory):

    item_name = command[1]
    if item_name not in current_location[keywords.General.ITEMS]:
        snarky_replies.print_snarky_reply_no_such_item(item_name)
        return

    item = current_location[keywords.General.ITEMS][item_name]
    inventory[item_name] = item
    del current_location[keywords.General.ITEMS][item_name]
