class Action:
    GO = "go"
    TAKE = "take"
    LEAVE = "leave"
    USE = "use"
    LOOK = "look"
    SHOW = "show"
    SPIN = "spin"
    PLAY = "play"
    READ = "read"
    THROW = "throw"
    CALL = "call"
    TYPE = "type"
    KICK = "kick"
    PLUG_IN = "plug in"
    WRITE = "write"
    MEASURE = "measure"
    UNSCREW = "unscrew"
    FEED = "feed"


class Area:
    FOREST = "forest"
    SCHOOLHOUSE = "schoolhouse"
    MOUNTAINS = "mountains"
    CITY = "city"


class Direction:
    NORTH = "north"
    SOUTH = "south"
    EAST = "east"
    WEST = "west"
    UP = "up"
    DOWN = "down"


class Location:

    SCHOOLHOUSE_ENTRY = "main_entry"
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

    FOREST_ENTRY = "forest-entry"

    CITY_ENTRY = "city-entry"

    MOUNTAINS_ENTRY = "mountains-entry"


class LocationKey:
    WEST = Direction.WEST
    EAST = Direction.EAST
    NORTH = Direction.NORTH
    SOUTH = Direction.SOUTH


class Item:
    MAP = "map"
    COMPASS = "compass"
    KNIFE = "knife"
    DICTIONARY = "dictionary"
    ANDROID_PHONE = "android-phone"
    IPHONE = "iphone"
    BALL = "ball"
    SCREWDRIVER = "screwdriver"
    LAPTOP = "laptop"
    LAPTOP_POWER_CABLE = "laptop-power-cable"
    GLOBE = "globe"
    RULER = "ruler"
    PENCIL = "pencil"
    SOCCER_BALL = "soccer-ball"
    FOOTBALL = "football"
    FRISBEE = "frisbee"
    BAXTER = "baxter-the-dog"
    PESTO = "pesto-the-dog"
    BUDDY = "buddy-the-cat"


class General:
    AT = "at"
    TO = "to"
    DESCRIPTION = "description"
    ITEMS = "items"
    LOOK = "look"
    INVENTORY = "inventory"
    HEALTH = "health"
    POWER = "power"
    KNOWLEDGE = "knowledge"
    MAGIC = "magic"
    DEFAULT_LOCATION = "default-location"


allowed_actions = [Action.GO, Action.TAKE, Action.LEAVE, Action.USE, Action.LOOK, Action.SHOW]
allowed_directions = [Direction.NORTH, Direction.SOUTH, Direction.EAST, Direction.WEST]
allowed_areas = [Area.FOREST, Area.CITY, Area.MOUNTAINS, Area.SCHOOLHOUSE]
