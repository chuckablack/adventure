import keywords

locations = {
    keywords.Location.MAIN_ENTRY: {
        keywords.LocationKey.DESCRIPTION: "You stand at the main entry to the schoolhouse.\n" +
                       "You are hoping for something interesting to happen in this game,\n" +
                       "but knowing the developer, your hopes are not high.",
        keywords.LocationKey.LOOK: "To the north, you see the entryway to the school that leads into the foyer",
        keywords.LocationKey.NORTH: "foyer",
    },
    keywords.Location.FOYER: {
        keywords.LocationKey.DESCRIPTION: "You are in the foyer.\n" +
                       "... and find yourself wondering, what the <bleep> is a 'foyer', anyway?!",
        keywords.LocationKey.LOOK: "To the north leads outside to the back on the school.\n" +
                "To the west and east are hallways leading to classrooms.\n" +
                "To the south is the main entryway into the school.",
        keywords.LocationKey.NORTH: "back_entry",
        keywords.LocationKey.WEST: "west_hallway",
        keywords.LocationKey.SOUTH: "main_entry",
        keywords.LocationKey.EAST: "east_hallway",
    },
    keywords.Location.WEST_ENTRY: {
        keywords.LocationKey.DESCRIPTION: "You are at the west entryway into the school.",
        keywords.LocationKey.LOOK: "To the east is the western entryway into the school.",
        keywords.LocationKey.EAST: "west_hallway",
    },
    keywords.Location.EAST_ENTRY: {
        keywords.LocationKey.DESCRIPTION: "You are at the east entryway into the school.",
        keywords.LocationKey.LOOK: "To the west is the eastern entryway into the school.",
        keywords.LocationKey.WEST: "east_hallway",
    },
    keywords.Location.BACK_ENTRY: {
        keywords.LocationKey.DESCRIPTION: "You are standing at the back entryway into the school.",
        keywords.LocationKey.LOOK: "To the south is the entryway into the foyer of the school.",
        keywords.LocationKey.SOUTH: "foyer",
    },
    keywords.Location.WEST_HALLWAY: {
        keywords.LocationKey.DESCRIPTION: "You are in a hallway, with lockers on the walls, and doors to classrooms on either side.",
        keywords.LocationKey.LOOK: "To the north is the science classroom.\n" +
                "To the south is the math classroom.\n" +
                "To the west is the door to exit the school via the west entrance.\n" +
                "To the east leads into the foyer.",
        keywords.LocationKey.NORTH: "classroom_science",
        keywords.LocationKey.SOUTH: "classroom_math",
        keywords.LocationKey.WEST: "west_entry",
        keywords.LocationKey.EAST: "foyer",
    },
    keywords.Location.EAST_HALLWAY: {
        keywords.LocationKey.DESCRIPTION: "You arrive in a hallway, walls lined with trophy cabinets\n" +
                       " ... for all the academic and athletic awards won by the school.\n" +
                       " ... in other words, filled with empty cabinets.",
        keywords.LocationKey.LOOK: "To the north is the accounting classroom.\n" +
                "To the south is the english classroom.\n" +
                "To the east is the door to exit the school via the east entrance.\n" +
                "To the west leads into the foyer.",
        keywords.LocationKey.NORTH: "classroom_accounting",
        keywords.LocationKey.SOUTH: "classroom_english",
        keywords.LocationKey.WEST: "foyer",
        keywords.LocationKey.EAST: "east_entry",

    },
    keywords.Location.CLASSROOM_ENGLISH: {
        keywords.LocationKey.DESCRIPTION: "You have stumbled into the english classroom, filled with dangling participles.\n" +
                       " ... You're not sure if that is a euphemism or not.",
        keywords.LocationKey.LOOK: "To the north is a door back into the east hallway.",
        keywords.LocationKey.NORTH: "east_hallway",
    },
    keywords.Location.CLASSROOM_SCIENCE: {
        keywords.LocationKey.DESCRIPTION: "You are in the science classroom. Or so you believe.\n" +
                       " ... Unfortunately, the entire room has been obliterated by a science experiment gone bad.",
        keywords.LocationKey.LOOK: "To the south is a door back into the west hallway.",
        keywords.LocationKey.SOUTH: "west_hallway",
    },
    keywords.Location.CLASSROOM_MATH: {
        keywords.LocationKey.DESCRIPTION: "You have entered the math classroom.\n" +
                       " ... Unsurprisingly, there seem to be no females in here.",
        keywords.LocationKey.LOOK: "To the north is a door back into the west hallway.",
        keywords.LocationKey.NORTH: "west_hallway",
    },
    keywords.Location.CLASSROOM_ACCOUNTING: {
        keywords.LocationKey.DESCRIPTION: "You find yourself in the accounting classroom.\n" +
                       " ... Unsurprisingly, everybody seems to be asleep.",
        keywords.LocationKey.LOOK: "To the south is a door back into the east hallway.",
        keywords.LocationKey.SOUTH: "east_hallway",
    },
}
