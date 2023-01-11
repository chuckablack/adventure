from keywords import allowed_areas, go_words, take_words, leave_words, look_words, allowed_directions


def print_general_help():

    print("""
GENERAL HELP:

This adventure game allows you to explore and interact with its imaginary world.

The world consists of the following areas:
""")
    for area in allowed_areas:
        print(f"    {area}")

    print("""
Within each area, you can:
--- move about using the GO command,
--- examine your location and items with the LOOK command,
--- pick things up with the TAKE command,
--- put things down with the LEAVE command,
--- and perform various other actions which are item-specific.
""")

    print("""
There are synonyms that can be used for these general commands, as follows:
""")
    print(f"--- GO words: {go_words}")
    print(f"--- LOOK words: {look_words}")
    print(f"--- TAKE words: {take_words}")
    print(f"--- LEAVE words: {leave_words}")

    print(f"\nWhen moving using GO, the allowed directions are: {allowed_directions}")
    print(f"    ... an exception being that you can immediately 'go to' a specific area")
    print(f"        for example, 'go to {allowed_areas[0]}'")


def get_help(command):

    # General help
    if len(command) == 1:
        print_general_help()

    # Specific help
    else:
        topic = command[1]
