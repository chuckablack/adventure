def print_snarky_reply_bad_action():
    print("legal commands begin with 'go', 'take', 'put', or 'use'")


def print_snarky_reply_bad_direction_name():
    print("legal directions are 'north', 'south', 'east', 'west'")


def print_snarky_reply_bad_direction():
    print("Ouch! You bump into a wall and bruise your nose.")


def print_snarky_reply_bad_world(location):
    print("looks like the designer of this adventure world is a moron!")
    print(f"... because there is no location named: {location}")
