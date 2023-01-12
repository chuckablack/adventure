class Action:
    HELP = "help"
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

    SCHOOLHOUSE_ENTRY = "schoolhouse-entry"
    FOYER = "foyer"
    WEST_ENTRY = "west-entry"
    EAST_ENTRY = "east-entry"
    BACK_ENTRY = "back-entry"
    WEST_HALLWAY = "west-hallway"
    EAST_HALLWAY = "east-hallway"
    CLASSROOM_ENGLISH = "classroom-english"
    CLASSROOM_SCIENCE = "classroom-science"
    CLASSROOM_MATH = "classroom-math"
    CLASSROOM_ACCOUNTING = "classroom-accounting"

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


class GoWords:
    GO = "go"
    MOVE = "move"
    PROCEED = "proceed"
    ADVANCE = "advance"
    WALK = "walk"
    RUN = "run"
    TRAVEL = "travel"
    SHUFFLE = "shuffle"
    SKIP = "skip"
    DANCE = "dance"
    SCOOT = "scoot"
    MOSEY = "mosey"


class TakeWords:
    TAKE = "take"
    GRAB = "grab"
    SNATCH = "snatch"
    SNAG = "snag"
    ACQUIRE = "acquire"
    PICK_UP = "pick-up"


class LeaveWords:
    LEAVE = "leave"
    DROP = "drop"
    DUMP = "dump"
    PUT_DOWN = "put-down"


class LookWords:
    LOOK = "look"
    DISPLAY = "display"
    EXAMINE = "examine"
    STUDY = "study"


allowed_actions = [Action.GO, Action.TAKE, Action.LEAVE, Action.USE, Action.LOOK, Action.SHOW]
allowed_directions = [Direction.NORTH, Direction.SOUTH, Direction.EAST, Direction.WEST, Direction.UP, Direction.DOWN]
allowed_areas = [Area.FOREST, Area.CITY, Area.MOUNTAINS, Area.SCHOOLHOUSE]

go_words = [v for k, v in GoWords.__dict__.items() if not k.startswith('__') and not callable(k)]
take_words = [v for k, v in TakeWords.__dict__.items() if not k.startswith('__') and not callable(k)]
leave_words = [v for k, v in LeaveWords.__dict__.items() if not k.startswith('__') and not callable(k)]
look_words = [v for k, v in LookWords.__dict__.items() if not k.startswith('__') and not callable(k)]
