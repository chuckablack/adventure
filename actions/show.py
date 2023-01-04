import keywords


def show_inventory(player_inventory):

    print("----- inventory -----------------------")
    for item_name, item in player_inventory.items():
        print(f"{item_name}: {item[keywords.General.DESCRIPTION]}")
    print("---------------------------------------")
