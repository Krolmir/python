import random

# List of words from http://www.free-teacher-worksheets.com/
words = [
    "aardvark",
    "air",
    "airplane",
    "airport",
    "alarm",
    "alligator",
    "alphabet",
    "ambulance",
    "animal",
    "ankle",
    "army",
    "answer",
    "ant",
    "antelope",
    "apple",
    "arm",
    "armchair",
    "arrow",
    "asparagus",
    "baby",
    "back",
    "backbone",
    "bacon",
    "badge",
    "badger",
    "bag",
    "bagpipe",
    "bait",
    "bakery",
    "ball",
    "balloon",
    "bamboo",
    "banana",
    "band",
    "bandana",
    "bangle",
    "banjo",
    "bank",
    "baseball",
    "basket",
    "basketball",
    "bat",
    "bath",
    "bathroom",
    "bathtub",
    "battery",
    "battle",
    "bay",
    "beach",
    "bead",
    "bean",
    "bear",
    "beard",
    "beast",
    "beat",
    "beauty",
    "beaver",
    "bed",
    "bedroom",
    "bee",
    "beef",
    "beetle",
    "bell",
    "belt",
    "bench",
    "beret",
    "berry",
    "bicycle",
    "bike",
    "bird",
    "birthday",
    "bite",
    "black",
    "blade",
    "blanket",
    "block",
    "blood",
    "blouse",
    "blow",
    "board",
    "boat",
    "bobcat",
    "body",
    "bolt",
    "bone",
    "bonsai",
    "book",
    "bookcase",
    "booklet",
    "boot",
    "border",
    "bottle",
    "bottom",
    "boundary",
    "bow",
    "bowling",
    "box",
    "boy",
    "brain",
    "brake",
    "branch",
    "brass",
    "bread",
    "break",
    "breakfast",
    "breath",
    "brick",
    "bridge",
    "broccoli",
    "brochure",
    "brother",
    "brush",
    "bubble",
    "bucket",
    "building",
    "bulb",
    "bull",
    "bulldozer",
    "bumper",
    "bun",
    "bus",
    "bush",
    "butter",
    "button",
    "cabbage",
    "cactus",
    "cafe",
    "cake",
    "calculator",
    "calendar",
    "calf",
    "call",
    "camel",
    "camera",
    "camp",
    "candle",
    "canoe",
    "canvas",
    "cap",
    "captain",
    "car",
    "card",
    "cardboard",
    "cardigan",
    "carpenter",
    "carrot",
    "cartoon",
    "cat",
    "caterpillar",
    "cathedral",
    "cattle",
    "cauliflower",
    "cave",
    "CD",
    "ceiling",
    "celery",
    "cello",
    "cement",
    "cemetery",
    "cereal",
    "chain",
    "chair",
    "chalk",
    "channel",
    "character",
    "cheek",
    "cheese",
    "cheetah",
    "cherry",
    "chess",
    "chest",
    "chick",
    "chicken",
    "children",
    "chimpanzee",
    "chin",
    "chive",
    "chocolate",
    "church",
    "cicada",
    "cinema",
    "circle",
    "city",
    "clam",
    "clarinet",
    "click",
    "clock",
    "close",
    "closet",
    "cloth",
    "cloud",
    "cloudy",
    "coach",
    "coal",
    "coast",
    "coat",
    "cobweb",
    "cockroach",
    "cocoa",
    "coffee",
    "coil",
    "coin",
    "coke",
    "cold",
    "collar",
    "college",
    "colt",
    "comb",
    "comics",
    "comma",
    "computer",
    "copy",
    "corn",
    "cost",
    "cotton",
    "couch",
    "cougar",
    "country",
    "course",
    "court",
    "cousin",
    "cow",
    "crab",
    "crack",
    "cracker",
    "crate",
    "crayfish",
    "crayon",
    "cream",
    "creek",
    "cricket",
    "crocodile",
    "crop",
    "crow",
    "crowd",
    "crown",
    "cucumber",
    "cup",
    "cupboard",
    "curtain",
    "curve",
    "cushion",
    "cyclone",
    "dad",
    "daffodil",
    "daisy",
    "dance",
    "daughter",
    "day",
    "deer",
    "denim",
    "dentist",
    "desert",
    "desk",
    "dessert",
    "detective",
    "dew",
    "diamond",
    "dictionary",
    "dinghy",
    "dinosaur",
    "dirt",
    "dish",
    "dog",
    "doll",
    "dollar",
    "door",
    "dragon",
    "dragonfly",
    "drain",
    "drawer",
    "dream",
    "dress",
    "dresser",
    "drill",
    "drink",
    "drum",
    "dryer",
    "duck",
    "duckling",
    "dungeon",
    "dust",
    "eagle",
    "ear",
    "earth",
    "earthquake",
    "eel",
    "egg",
    "eggplant",
    "elbow",
    "elephant",
    "energy",
    "engine",
    "equipment",
    "evening",
    "eye",
    "eyebrow",
    "face",
    "fact",
    "factory",
    "fairies",
    "family",
    "fan",
    "fang",
    "farm",
    "fear",
    "feast",
    "feather",
    "feet",
    "ferryboat",
    "field",
    "fight",
    "finger",
    "fire",
    "fireplace",
    "fish",
    "flag",
    "flame",
    "flood",
    "floor",
    "flower",
    "flute",
    "fly",
    "foam",
    "fog",
    "food",
    "foot",
    "football",
    "forehead",
    "forest",
    "fork",
    "fountain",
    "fox",
    "frame",
    "freckle",
    "freezer",
    "frog",
    "frost",
    "fruit",
    "fuel",
    "fur",
    "furniture",
    "game",
    "garage",
    "garden",
    "garlic",
    "gas",
    "gate",
    "gear",
    "ghost",
    "giraffe",
    "girl",
    "glass",
    "glove",
    "glue",
    "goal",
    "goat",
    "gold",
    "goldfish",
    "golf",
    "gorilla",
    "government",
    "grape",
    "grass",
    "grasshopper",
    "grease",
    "grill",
    "group",
    "guitar",
    "gum",
    "gym",
    "gymnast",
    "hail",
    "hair",
    "haircut",
    "hall",
    "hamburger",
    "hammer",
    "hamster",
    "hand",
    "handball",
    "handle",
    "hardware",
    "harmonica",
    "harmony",
    "hat",
    "hate",
    "hawk",
    "head",
    "headlight",
    "health",
    "heart",
    "heat",
    "heaven",
    "hedge",
    "height",
    "helicopter",
    "helmet",
    "help",
    "hen",
    "hill",
    "hip",
    "hippopotamus",
    "history",
    "hockey",
    "hole",
    "holiday",
    "home",
    "honey",
    "hood",
    "hook",
    "horn",
    "horse",
    "hose",
    "hospital",
    "hour",
    "house",
    "hurricane",
    "hyena",
    "ice",
    "icicle",
    "idea",
    "ink",
    "insect",
    "instrument",
    "Internet",
    "invention",
    "iron",
    "island",
    "jacket",
    "jaguar",
    "jail",
    "jam",
    "jar",
    "jaw",
    "jeans",
    "jeep",
    "jelly",
    "jellyfish",
    "jet",
    "jewel",
    "joke",
    "journey",
    "judge",
    "judo",
    "juice",
    "jump",
    "jumper",
    "kangaroo",
    "karate",
    "kayak",
    "kettle",
    "key",
    "keyboard",
    "kick",
    "kiss",
    "kitchen",
    "kite",
    "kitten",
    "knee",
    "knife",
    "knight",
    "knot",
    "lace",
    "ladybug",
    "lake",
    "lamb",
    "lamp",
    "land",
    "lasagna",
    "laugh",
    "laundry",
    "leaf",
    "leather",
    "leek",
    "leg",
    "lemonade",
    "leopard",
    "letter",
    "lettuce",
    "library",
    "lift",
    "light",
    "lightning",
    "lily",
    "line",
    "lion",
    "lip",
    "lipstick",
    "liquid",
    "list",
    "litter",
    "lizard",
    "loaf",
    "lobster",
    "lock",
    "locket",
    "locust",
    "look",
    "lotion",
    "love",
    "lunch",
    "lynx",
    "macaroni",
    "machine",
    "magazine",
    "magic",
    "magician",
    "mail",
    "mailbox",
    "mailman",
    "makeup",
    "map",
    "marble",
    "mark",
    "market",
    "mascara",
    "mask",
    "match",
    "meal",
    "meat",
    "mechanic",
    "medicine",
    "memory",
    "men",
    "menu",
    "message",
    "metal",
    "mice",
    "middle",
    "milk",
    "milkshake",
    "mint",
    "minute",
    "mirror",
    "mist",
    "mistake",
    "mitten",
    "Monday",
    "money",
    "monkey",
    "month",
    "moon",
    "morning",
    "mosquito",
    "motorboat",
    "motorcycle",
    "mountain",
    "mouse",
    "moustache",
    "mouth",
    "music",
    "mustard",
    "nail",
    "name",
    "napkin",
    "neck",
    "needle",
    "nest",
    "net",
    "news",
    "night",
    "noise",
    "noodle",
    "nose",
    "note",
    "notebook",
    "number",
    "nut",
    "oak",
    "oatmeal",
    "ocean",
    "octopus",
    "office",
    "oil",
    "olive",
    "onion",
    "orange",
    "orchestra",
    "ostrich",
    "otter",
    "oven",
    "owl",
    "ox",
    "oxygen",
    "oyster",
    "packet",
    "page",
    "pail",
    "pain",
    "paint",
    "pair",
    "pajama",
    "pamphlet",
    "pan",
    "pancake",
    "panda",
    "pansy",
    "panther",
    "pants",
    "paper",
    "parcel",
    "parent",
    "park",
    "parrot",
    "party",
    "pasta",
    "paste",
    "pastry",
    "patch",
    "path",
    "pea",
    "peace",
    "peanut",
    "pear",
    "pedestrian",
    "pelican",
    "pen",
    "pencil",
    "pepper",
    "perfume",
    "person",
    "pest",
    "pet",
    "phone",
    "piano",
    "pickle",
    "picture",
    "pie",
    "pig",
    "pigeon",
    "pillow",
    "pilot",
    "pimple",
    "pin",
    "pipe",
    "pizza",
    "plane",
    "plant",
    "plantation",
    "plastic",
    "plate",
    "playground",
    "plot",
    "pocket",
    "poison",
    "police",
    "policeman",
    "pollution",
    "pond",
    "popcorn",
    "poppy",
    "porcupine",
    "postage",
    "postbox",
    "pot",
    "potato",
    "poultry",
    "powder",
    "power",
    "price",
    "printer",
    "prison",
    "pumpkin",
    "puppy",
    "pyramid",
    "queen",
    "question",
    "quicksand",
    "quill",
    "quilt",
    "rabbit",
    "radio",
    "radish",
    "raft",
    "rail",
    "railway",
    "rain",
    "rainbow",
    "raincoat",
    "rainstorm",
    "rake",
    "rat",
    "ravioli",
    "ray",
    "recorder",
    "rectangle",
    "refrigerator",
    "reindeer",
    "relatives",
    "restaurant",
    "reward",
    "rhinoceros",
    "rice",
    "riddle",
    "ring",
    "river",
    "road",
    "roast",
    "rock",
    "roll",
    "roof",
    "room",
    "rooster",
    "rose",
    "rowboat",
    "rubber",
    "sack",
    "sail",
    "sailboat",
    "sailor",
    "salad",
    "salmon",
    "salt",
    "sand",
    "sandwich",
    "sardine",
    "sauce",
    "sausage",
    "saw",
    "saxophone",
    "scarecrow",
    "scarf",
    "school",
    "scissors",
    "scooter",
    "scorpion",
    "screw",
    "screwdriver",
    "sea",
    "seagull",
    "seal",
    "seaplane",
    "seashore",
    "season",
    "seat",
    "second",
    "seed",
    "sentence",
    "servant",
    "shade",
    "shadow",
    "shallot",
    "shampoo",
    "shark",
    "shears",
    "sheep",
    "sheet",
    "shelf",
    "shell",
    "shield",
    "ship",
    "shirt",
    "shoe",
    "shoemaker",
    "shop",
    "shorts",
    "shoulder",
    "shovel",
    "show",
    "side",
    "sidewalk",
    "sign",
    "signature",
    "silk",
    "silver",
    "singer",
    "sink",
    "sister",
    "skin",
    "skirt",
    "sky",
    "sled",
    "slippers",
    "slope",
    "smoke",
    "snail",
    "snake",
    "sneeze",
    "snow",
    "snowflake",
    "snowman",
    "soap",
    "soccer",
    "sock",
    "sofa",
    "softball",
    "soldier",
    "son",
    "song",
    "sound",
    "soup",
    "soybean",
    "space",
    "spade",
    "spaghetti",
    "spark",
    "sparrow",
    "spear",
    "speedboat",
    "spider",
    "spike",
    "spinach",
    "sponge",
    "spoon",
    "spot",
    "sprout",
    "spy",
    "square",
    "squash",
    "squid",
    "squirrel",
    "stage",
    "staircase",
    "stamp",
    "star",
    "station",
    "steam",
    "steel",
    "stem",
    "step",
    "stew",
    "stick",
    "stitch",
    "stinger",
    "stomach",
    "stone",
    "stool",
    "stopsign",
    "stopwatch",
    "store",
    "storm",
    "story",
    "stove",
    "stranger",
    "straw",
    "stream",
    "string",
    "submarine",
    "sugar",
    "suit",
    "summer",
    "sun",
    "sunshine",
    "sunflower",
    "supermarket",
    "surfboard",
    "surname",
    "surprise",
    "sushi",
    "swallow",
    "swamp",
    "swan",
    "sweater",
    "sweatshirt",
    "sweets",
    "swing",
    "switch",
    "sword",
    "swordfish",
    "syrup",
    "table",
    "tabletop",
    "tadpole",
    "tail",
    "target",
    "tax",
    "taxi",
    "tea",
    "teacher",
    "team",
    "teeth",
    "television",
    "tennis",
    "tent",
    "textbook",
    "theater",
    "thistle",
    "thought",
    "thread",
    "throat",
    "throne",
    "thumb",
    "thunder",
    "thunderstorm",
    "ticket",
    "tie",
    "tiger",
    "tile",
    "time",
    "tire",
    "toad",
    "toast",
    "toe",
    "toilet",
    "tomato",
    "tongue",
    "tooth",
    "toothbrush",
    "toothpaste",
    "top",
    "tornado",
    "tortoise",
    "tower",
    "town",
    "toy",
    "tractor",
    "traffic",
    "trail",
    "train",
    "transport",
    "tray",
    "tree",
    "triangle",
    "trick",
    "trip",
    "trombone",
    "trouble",
    "trousers",
    "truck",
    "trumpet",
    "trunk",
    "t-shirt",
    "tub",
    "tuba",
    "tugboat",
    "tulip",
    "tuna",
    "tune",
    "Turkey",
    "turnip",
    "turtle",
    "TV",
    "twig",
    "twilight",
    "twine",
    "umbrella",
    "valley",
    "van",
    "vase",
    "vegetable",
    "veil",
    "vein",
    "vessel",
    "vest",
    "violin",
    "volcano",
    "volleyball",
    "vulture",
    "wall",
    "wallaby",
    "walrus",
    "washer",
    "wasp",
    "waste",
    "watch",
    "watchmaker",
    "water",
    "waterfall",
    "wave",
    "wax",
    "weapon",
    "weasel",
    "weather",
    "wedge",
    "whale",
    "wheel",
    "whip",
    "whistle",
    "wilderness",
    "willow",
    "wind",
    "window",
    "windscreen",
    "wing",
    "winter",
    "wire",
    "wish",
    "witch",
    "wolf",
    "woman",
    "wood",
    "wool",
    "word",
    "workshop",
    "worm",
    "wound",
    "wren",
    "wrench",
    "wrinkles",
    "wrist",
    "xylophone",
    "yacht",
    "yak",
    "yard",
    "yogurt",
    "zebra",
    "zipper",
    "zoo"
]

def get_random_word():
    word = random.choice(words)
    return word
