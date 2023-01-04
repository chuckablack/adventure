import keywords


def print_snarky_reply_bad_action():
    print(f"legal command actions begin with one of the following: {keywords.allowed_actions}")


def print_snarky_reply_bad_direction_name():
    print(f"legal directions are one of the following: {keywords.allowed_directions}")


def print_snarky_reply_bad_direction():
    print("Ouch! You bump into a wall and bruise your nose.")


def print_snarky_reply_bad_go_to_area():
    print(f"Whoops - you are only allow to 'go to' these areas: {keywords.allowed_areas}")


def print_snarky_reply_bad_world(location):
    print("looks like the designer of this adventure world is a moron!")
    print(f"... because there is no location named: {location}")


def print_snarky_reply_bad_look_command():
    print(f"Huh? You slap your forehead and ask 'How could I write my command so poorly??!'")


def print_snarky_reply_dont_have_item(item):
    print(f"Hmm. I don't see {item} in your inventory or in the current location.")


def print_snarky_reply_no_such_item(item):
    print(f"That's funny, I don't see {item} anywhere in this location.")
