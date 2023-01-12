from keywords import Location, LocationKey, Item, General
from world.items import items

locations = {

    # ----- Schoolhouse -----------------------------------------------
    Location.SCHOOLHOUSE_ENTRY: {
        General.DESCRIPTION: "\n\tYou stand at the main entry to the schoolhouse. \n" +
                             "\tYou are hoping for something interesting to happen in this game, \n" +
                             "\tbut knowing the developer, your hopes are not high.",
        General.LOOK: "\n\tTo the north, you see the entryway to the school that leads into the foyer",
        General.ITEMS: {Item.MAP: items[Item.MAP]},
        LocationKey.NORTH: Location.FOYER,
    },
    Location.FOYER: {
        General.DESCRIPTION: "\n\tYou are in the foyer. \n" +
                             "\t... and find yourself wondering, what the <bleep> is a 'foyer', anyway?!",
        General.LOOK: "\n\tTo the north leads outside to the back on the school.\n" +
                      "\tTo the west and east are hallways leading to classrooms.\n" +
                      "\tTo the south is the main entryway into the school.",
        General.ITEMS: {Item.GLOBE: items[Item.GLOBE],
                        Item.ANDROID_PHONE: items[Item.ANDROID_PHONE]},
        LocationKey.NORTH: Location.BACK_ENTRY,
        LocationKey.WEST: Location.WEST_HALLWAY,
        LocationKey.SOUTH: Location.SCHOOLHOUSE_ENTRY,
        LocationKey.EAST: Location.EAST_HALLWAY,
    },
    Location.WEST_ENTRY: {
        General.DESCRIPTION: "\n\tYou are at the west entryway into the school.",
        General.LOOK: "\n\tTo the east is the western entryway into the school.",
        General.ITEMS: {Item.SOCCER_BALL: items[Item.SOCCER_BALL],
                        Item.BAXTER: items[Item.BAXTER]},
        LocationKey.EAST: Location.WEST_HALLWAY,
    },
    Location.EAST_ENTRY: {
        General.DESCRIPTION: "\n\tYou are at the east entryway into the school.",
        General.LOOK: "\n\tTo the west is the eastern entryway into the school.",
        General.ITEMS: {Item.FRISBEE: items[Item.FRISBEE]},
        LocationKey.WEST: Location.EAST_HALLWAY,
    },
    Location.BACK_ENTRY: {
        General.DESCRIPTION: "\n\tYou are standing at the back entryway into the school.",
        General.LOOK: "\n\tTo the south is the entryway into the foyer of the school.",
        General.ITEMS: {},
        LocationKey.SOUTH: Location.FOYER,
    },
    Location.WEST_HALLWAY: {
        General.DESCRIPTION: "\n\tYou are in a hallway, with lockers on the walls,\n" +
                             "\tand doors to classrooms on either side.",
        General.LOOK: "\n\tTo the north is the science classroom.\n" +
                      "\tTo the south is the math classroom.\n" +
                      "\tTo the west is the door to exit the school via the west entrance.\n" +
                      "\tTo the east leads into the foyer.",
        General.ITEMS: {},
        LocationKey.NORTH: Location.CLASSROOM_SCIENCE,
        LocationKey.SOUTH: Location.CLASSROOM_MATH,
        LocationKey.WEST: Location.WEST_ENTRY,
        LocationKey.EAST: Location.FOYER,
    },
    Location.EAST_HALLWAY: {
        General.DESCRIPTION: "\n\tYou arrive in a hallway, walls lined with trophy cabinets\n" +
                             "\t ... for all the academic and athletic awards won by the school.\n" +
                             "\t ... in other words, filled with empty cabinets.",
        General.LOOK: "\n\tTo the north is the accounting classroom.\n" +
                      "\tTo the south is the english classroom.\n" +
                      "\tTo the east is the door to exit the school via the east entrance.\n" +
                      "\tTo the west leads into the foyer.",
        General.ITEMS: {},
        LocationKey.NORTH: Location.CLASSROOM_ACCOUNTING,
        LocationKey.SOUTH: Location.CLASSROOM_ENGLISH,
        LocationKey.WEST: Location.FOYER,
        LocationKey.EAST: Location.EAST_ENTRY,

    },
    Location.CLASSROOM_ENGLISH: {
        General.DESCRIPTION: "\n\tYou have stumbled into the english classroom, filled with dangling participles.\n" +
                             "\t ... You're not sure if that is a euphemism or not.",
        General.LOOK: "\n\tTo the north is a door back into the east hallway.",
        General.ITEMS: {},
        LocationKey.NORTH: Location.EAST_HALLWAY,
    },
    Location.CLASSROOM_SCIENCE: {
        General.DESCRIPTION: "\n\tYou are in the science classroom. Or so you believe.\n" +
                             "\t ... Unfortunately, the entire room has been obliterated" +
                             "\t ... by a science experiment gone bad.",
        General.LOOK: "\n\tTo the south is a door back into the west hallway.",
        General.ITEMS: {},
        LocationKey.SOUTH: Location.WEST_HALLWAY,
    },
    Location.CLASSROOM_MATH: {
        General.DESCRIPTION: "\n\tYou have entered the math classroom.\n" +
                             "\t ... Unsurprisingly, there seem to be no females in here.",
        General.LOOK: "\n\tTo the north is a door back into the west hallway.",
        General.ITEMS: {},
        LocationKey.NORTH: Location.WEST_HALLWAY,
    },
    Location.CLASSROOM_ACCOUNTING: {
        General.DESCRIPTION: "\n\tYou find yourself in the accounting classroom.\n" +
                             "\t ... Unsurprisingly, everybody seems to be asleep.",
        General.LOOK: "\n\tTo the south is a door back into the east hallway.",
        General.ITEMS: {},
        LocationKey.SOUTH: Location.EAST_HALLWAY,
    },

    # ----- Mountains -------------------------------------------------
    Location.MOUNTAINS_ENTRY: {
        General.DESCRIPTION: "\n\tYou stand at the main entry to the mountains. \n" +
                             "\tYou feel small and insignificant as sheer cliff faces tower before you, \n"
                             "\tbut you notice a cleft that you might be able to fit through.",
        General.LOOK: "\n\tTo the east, you see the cleft in the mountains that you might be able to sneak through.",
        General.ITEMS: {Item.MAP: items[Item.MAP]},
        LocationKey.NORTH: Location.FOYER,
    },

    # ----- Forest ----------------------------------------------------
    Location.FOREST_ENTRY: {
        General.DESCRIPTION: "\n\tYou stand at the foot of a huge forest. " +
                             "\tMost of the huge behemoths before you are evergreen, redwoods and pine mostly, " +
                             "\tbut through the branches you think you spot a silver, glimmering tree.",
        General.LOOK: "\n\tTo the north, you see the path into the forest",
        General.ITEMS: {Item.MAP: items[Item.MAP]},
        LocationKey.NORTH: Location.FOYER,
    },

    # ----- City ------------------------------------------------------
    Location.CITY_ENTRY: {
        General.DESCRIPTION: "\n\tYou stand at the main street which leads through the old-fashioned city before you. " +
                             "\tYou see a cafe, a motel, a hardware store, and of course, a Starbucks. ",
        General.LOOK: "\n\tTo the north you see the street leading into the city.",
        General.ITEMS: {Item.MAP: items[Item.MAP]},
        LocationKey.NORTH: Location.FOYER,
    },

}
