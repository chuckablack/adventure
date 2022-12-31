class Action:
    GO = "go"
    TAKE = "take"
    LEAVE = "leave"
    USE = "use"
    LOOK = "look"


class Direction:
    NORTH = "north"
    SOUTH = "south"
    EAST = "east"
    WEST = "west"


class Location:
    MAIN_ENTRY = "main_entry"
    FOYER = "foyer"
    WEST_ENTRY = "west_entry"
    EAST_ENTRY = "east_entry"
    BACK_ENTRY = "back_entry"
    WEST_HALLWAY = "west_hallway"
    EAST_HALLWAY = "east_hallway"
    CLASSROOM_ENGLISH = "classroom_english"
    CLASSROOM_SCIENCE = "classroom_science"
    CLASSROOM_MATH = "classroom_math"
    CLASSROOM_ACCOUNTING = "classroom_accounting"


class LocationKey:
    DESCRIPTION = "description"
    LOOK = "look"
    WEST = Direction.WEST
    EAST = Direction.EAST
    NORTH = Direction.NORTH
    SOUTH = Direction.SOUTH


allowed_actions = [Action.GO, Action.TAKE, Action.LEAVE, Action.USE, Action.LOOK]
allowed_directions = [Direction.NORTH, Direction.SOUTH, Direction.EAST, Direction.WEST]
