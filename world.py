from keywords import Location, LocationKey, Item, General

locations = {
    Location.MAIN_ENTRY: {
        General.DESCRIPTION: "You stand at the main entry to the schoolhouse. " +
                             "You are hoping for something interesting to happen in this game, " +
                             "but knowing the developer, your hopes are not high.",
        General.LOOK: "To the north, you see the entryway to the school that leads into the foyer",
        General.ITEMS: [Item.MAP],
        LocationKey.NORTH: Location.FOYER,
    },
    Location.FOYER: {
        General.DESCRIPTION: "You are in the foyer. " +
                             "... and find yourself wondering, what the <bleep> is a 'foyer', anyway?!",
        General.LOOK: "To the north leads outside to the back on the school.\n" +
                      "To the west and east are hallways leading to classrooms.\n" +
                      "To the south is the main entryway into the school.",
        General.ITEMS: [Item.GLOBE, Item.ANDROID_PHONE],
        LocationKey.NORTH: Location.BACK_ENTRY,
        LocationKey.WEST: Location.WEST_HALLWAY,
        LocationKey.SOUTH: Location.MAIN_ENTRY,
        LocationKey.EAST: Location.EAST_HALLWAY,
    },
    Location.WEST_ENTRY: {
        General.DESCRIPTION: "You are at the west entryway into the school.",
        General.LOOK: "To the east is the western entryway into the school.",
        General.ITEMS: [Item.SOCCER_BALL, Item.BAXTER],
        LocationKey.EAST: Location.WEST_HALLWAY,
    },
    Location.EAST_ENTRY: {
        General.DESCRIPTION: "You are at the east entryway into the school.",
        General.LOOK: "To the west is the eastern entryway into the school.",
        General.ITEMS: [Item.FRISBEE],
        LocationKey.WEST: Location.EAST_HALLWAY,
    },
    Location.BACK_ENTRY: {
        General.DESCRIPTION: "You are standing at the back entryway into the school.",
        General.LOOK: "To the south is the entryway into the foyer of the school.",
        General.ITEMS: [],
        LocationKey.SOUTH: Location.FOYER,
    },
    Location.WEST_HALLWAY: {
        General.DESCRIPTION: "You are in a hallway, with lockers on the walls," +
                             "and doors to classrooms on either side.",
        General.LOOK: "To the north is the science classroom.\n" +
                      "To the south is the math classroom.\n" +
                      "To the west is the door to exit the school via the west entrance.\n" +
                      "To the east leads into the foyer.",
        General.ITEMS: [],
        LocationKey.NORTH: Location.CLASSROOM_SCIENCE,
        LocationKey.SOUTH: Location.CLASSROOM_MATH,
        LocationKey.WEST: Location.WEST_ENTRY,
        LocationKey.EAST: Location.FOYER,
    },
    Location.EAST_HALLWAY: {
        General.DESCRIPTION: "You arrive in a hallway, walls lined with trophy cabinets\n" +
                             " ... for all the academic and athletic awards won by the school.\n" +
                             " ... in other words, filled with empty cabinets.",
        General.LOOK: "To the north is the accounting classroom.\n" +
                      "To the south is the english classroom.\n" +
                      "To the east is the door to exit the school via the east entrance.\n" +
                      "To the west leads into the foyer.",
        General.ITEMS: [],
        LocationKey.NORTH: Location.CLASSROOM_ACCOUNTING,
        LocationKey.SOUTH: Location.CLASSROOM_ENGLISH,
        LocationKey.WEST: Location.FOYER,
        LocationKey.EAST: Location.EAST_ENTRY,

    },
    Location.CLASSROOM_ENGLISH: {
        General.DESCRIPTION: "You have stumbled into the english classroom, filled with dangling participles.\n" +
                             " ... You're not sure if that is a euphemism or not.",
        General.LOOK: "To the north is a door back into the east hallway.",
        General.ITEMS: [],
        LocationKey.NORTH: Location.EAST_HALLWAY,
    },
    Location.CLASSROOM_SCIENCE: {
        General.DESCRIPTION: "You are in the science classroom. Or so you believe.\n" +
                             " ... Unfortunately, the entire room has been obliterated" +
                             " ... by a science experiment gone bad.",
        General.LOOK: "To the south is a door back into the west hallway.",
        General.ITEMS: [],
        LocationKey.SOUTH: Location.WEST_HALLWAY,
    },
    Location.CLASSROOM_MATH: {
        General.DESCRIPTION: "You have entered the math classroom.\n" +
                             " ... Unsurprisingly, there seem to be no females in here.",
        General.LOOK: "To the north is a door back into the west hallway.",
        General.ITEMS: [],
        LocationKey.NORTH: Location.WEST_HALLWAY,
    },
    Location.CLASSROOM_ACCOUNTING: {
        General.DESCRIPTION: "You find yourself in the accounting classroom.\n" +
                             " ... Unsurprisingly, everybody seems to be asleep.",
        General.LOOK: "To the south is a door back into the east hallway.",
        General.ITEMS: [],
        LocationKey.SOUTH: Location.EAST_HALLWAY,
    },
}

items = {

    Item.GLOBE: {
        General.DESCRIPTION: "A beautiful antique globe which can spin on its axis, from the early 1900s."
    },
    Item.BAXTER: {
        General.DESCRIPTION: "A Jack Russell - Border Terrier mix, a little bit crazy but adorable all the same."
    },
    Item.FRISBEE: {
        General.DESCRIPTION: "A standard Ultimate disc, with 'SPORGY BOOGLES' written on the inside."
    },
    Item.ANDROID_PHONE: {
        General.DESCRIPTION: "A Google Pixel 6A, with a shatterproof case and a broken screen."
    },
    Item.MAP: {

    },
    Item.SOCCER_BALL: {

    },
    Item.BALL: {

    },
    Item.BUDDY: {

    },
    Item.COMPASS: {

    },
    Item.DICTIONARY: {

    },
    Item.FOOTBALL: {

    },
    Item.IPHONE: {

    },
    Item.KNIFE: {

    },
    Item.LAPTOP: {

    },
    Item.LAPTOP_POWER_CABLE: {

    },
    Item.PENCIL: {

    },
    Item.PESTO: {

    },
    Item.RULER: {

    },
    Item.SCREWDRIVER: {

    },
}
