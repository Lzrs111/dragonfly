from dragonfly import *

class TemporaryCommands(MappingRule):
    mapping = {
        "height": Text("height"),
        "width": Text("width"),
        "cell": Text("cell"),
        "big cell": Text("Cell"),
        "neighbours": Text("neighbours"),
        "alive": Text("alive"),
        "invader": Text("Invader"),
        "ship": Text("ship"),
        "invaders": Text("invaders"),
        "draw": Text("draw")
    }