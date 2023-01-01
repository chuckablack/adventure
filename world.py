from keywords import Location, LocationKey

locations = {
    Location.MAIN_ENTRY: {
        LocationKey.DESCRIPTION: "You stand at the main entry to the schoolhouse.\n" +
                       "You are hoping for something interesting to happen in this game,\n" +
                       "but knowing the developer, your hopes are not high.",
        LocationKey.LOOK: "To the north, you see the entryway to the school that leads into the foyer",
        LocationKey.NORTH: Location.FOYER,
    },
    Location.FOYER: {
        LocationKey.DESCRIPTION: "You are in the foyer.\n" +
                       "... and find yourself wondering, what the <bleep> is a 'foyer', anyway?!",
        LocationKey.LOOK: "To the north leads outside to the back on the school.\n" +
                "To the west and east are hallways leading to classrooms.\n" +
                "To the south is the main entryway into the school.",
        LocationKey.NORTH: Location.BACK_ENTRY,
        LocationKey.WEST: Location.WEST_HALLWAY,
        LocationKey.SOUTH: Location.MAIN_ENTRY,
        LocationKey.EAST: Location.EAST_HALLWAY,
    },
    Location.WEST_ENTRY: {
        LocationKey.DESCRIPTION: "You are at the west entryway into the school.",
        LocationKey.LOOK: "To the east is the western entryway into the school.",
        LocationKey.EAST: Location.WEST_HALLWAY,
    },
    Location.EAST_ENTRY: {
        LocationKey.DESCRIPTION: "You are at the east entryway into the school.",
        LocationKey.LOOK: "To the west is the eastern entryway into the school.",
        LocationKey.WEST: Location.EAST_HALLWAY,
    },
    Location.BACK_ENTRY: {
        LocationKey.DESCRIPTION: "You are standing at the back entryway into the school.",
        LocationKey.LOOK: "To the south is the entryway into the foyer of the school.",
        LocationKey.SOUTH: Location.FOYER,
    },
    Location.WEST_HALLWAY: {
        LocationKey.DESCRIPTION: "You are in a hallway, with lockers on the walls, and doors to classrooms on either side.",
        LocationKey.LOOK: "To the north is the science classroom.\n" +
                "To the south is the math classroom.\n" +
                "To the west is the door to exit the school via the west entrance.\n" +
                "To the east leads into the foyer.",
        LocationKey.NORTH: Location.CLASSROOM_SCIENCE,
        LocationKey.SOUTH: Location.CLASSROOM_MATH,
        LocationKey.WEST: Location.WEST_ENTRY,
        LocationKey.EAST: Location.FOYER,
    },
    Location.EAST_HALLWAY: {
        LocationKey.DESCRIPTION: "You arrive in a hallway, walls lined with trophy cabinets\n" +
                       " ... for all the academic and athletic awards won by the school.\n" +
                       " ... in other words, filled with empty cabinets.",
        LocationKey.LOOK: "To the north is the accounting classroom.\n" +
                "To the south is the english classroom.\n" +
                "To the east is the door to exit the school via the east entrance.\n" +
                "To the west leads into the foyer.",
        LocationKey.NORTH: Location.CLASSROOM_ACCOUNTING,
        LocationKey.SOUTH: Location.CLASSROOM_ENGLISH,
        LocationKey.WEST: Location.FOYER,
        LocationKey.EAST: Location.EAST_ENTRY,

    },
    Location.CLASSROOM_ENGLISH: {
        LocationKey.DESCRIPTION: "You have stumbled into the english classroom, filled with dangling participles.\n" +
                       " ... You're not sure if that is a euphemism or not.",
        LocationKey.LOOK: "To the north is a door back into the east hallway.",
        LocationKey.NORTH: Location.EAST_HALLWAY,
    },
    Location.CLASSROOM_SCIENCE: {
        LocationKey.DESCRIPTION: "You are in the science classroom. Or so you believe.\n" +
                       " ... Unfortunately, the entire room has been obliterated by a science experiment gone bad.",
        LocationKey.LOOK: "To the south is a door back into the west hallway.",
        LocationKey.SOUTH: Location.WEST_HALLWAY,
    },
    Location.CLASSROOM_MATH: {
        LocationKey.DESCRIPTION: "You have entered the math classroom.\n" +
                       " ... Unsurprisingly, there seem to be no females in here.",
        LocationKey.LOOK: "To the north is a door back into the west hallway.",
        LocationKey.NORTH: Location.WEST_HALLWAY,
    },
    Location.CLASSROOM_ACCOUNTING: {
        LocationKey.DESCRIPTION: "You find yourself in the accounting classroom.\n" +
                       " ... Unsurprisingly, everybody seems to be asleep.",
        LocationKey.LOOK: "To the south is a door back into the east hallway.",
        LocationKey.SOUTH: Location.EAST_HALLWAY,
    },
}
