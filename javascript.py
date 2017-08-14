from dragonfly import *
from python import camelCase, camelText

pause = Pause("20")
    
class JavaScriptMain(MappingRule):
    
    mapping = {
        "variable":    Text("var"),
        "variable [<text>]": Text("var %(text)s = "),
        "lesser variable [<text>]": Text("let %(text)s = "),
        "constant [<text>]": Text("const %(text)s = "),
        "constructor": Text("constructor() {}"),
        "super": Text("super()"),
        "parents": Text("()"),
        "[<text>] equals":  Text(" = "),
        "colon|colin|collin": Text(":"),
        "falls|false": Text("false"),
        "true|troo|tru": Text("true"),
        "on click|old click": Text(" onClick"),
        "return": Text("return "),
        "[<text>] plus equals": Text("%(text)s +="),
        'line <n> [<g>] [<q>]':  Key('%(n)d')+Key('%(g)d') +Key('%(q)d')+ Key('G'),
        "this dot": Text("this."),
        "rez|res|ref": Text("ref"),
        "export": Text ("export "),
        "default": Text("default "),
        "class name": Text(" className = ''") + Key("left"),
        "make string": Text("''")+ pause + Key("left") + pause,
        "logical and": pause + Text("&&") + pause,
        "logical or": pause + Text ("||") + pause,

        #snippets
        "make [a new] class": Key("c-i"),
        "make [a new] state": Key("c-w"),
        "this state": Key("shift:down,c-p,shift:up"),
        "bind [a new] method": Key("c-e"),
        "set [a new] state": Key("c-r"),
        "make [a new] div": Key("c-j"),
        "make [a new] method": Key("c-g"),
        "make [a new] html": Key("c-h"),
        "make [a new] self closing": Key("c-l"),
        "make [a new] property": Key("c-p"),
        "make if": Key("c-y"),
        "make if else": Key("c-x"),
        "make else if": pause + Text("makeelsif") + pause + Key("tab"),
        "make else": pause + Text("makeelse!") + pause + Key("tab"),
        "while|wild": Key("c-c"),
        "[make[a new]]arrow function": Key("c-v"),
        "call method": Key("c-b"),
        "log": Key("shift:down,c-q,shift:up"),
        "make [a new] generator": Key("c-n"),
        "make [a new] function": pause + Text("cfun") + pause + Key("tab"),
        "make [a new] for loop": Key("c-m"),
        "make conditional": Key("c-k"),
        "curly": pause + Key("shift:down,c-c,shift:up") + pause,
        "make array": pause + Key("shift:down,c-a,shift:up") + pause,
        "set timeout": pause + Text("settimeout") + pause + Key("tab"),
        "set interval": pause + Text("setinterval") + pause + Key("tab"),
        "make import": pause + Text("makeimport") + pause + Key("tab"),
        "import see ess ess": pause + Text("importcss") + pause + Key("tab"),

        
        #array and string methods
        "[<text>] <method>": Text("%(text)s") + Pause("20") + Text("%(method)s")+ Pause("20") + Text("()") + Pause("20") + Key("left")+ Pause("20"),
        "[<text>] length": Text("%(text)s.length"),

        "parse integer": Text("parseInt()") + Key("left"),
        "parse float": Text("parseFloat()") + Key("left"),

        #math
        "math random": Text("Math.random()"),
        "math floor": Text("Math.floor()"),

        #javascript CSS
        "background color": Text("backgroundColor"),
        "border [<direction>]": Text("border%(direction)s"),

        # JavaScript events
        "key down": Text("'keydown'"),
        "key up": Text("'keyup'"),
        "event keycode": Text("event.keyCode"),
        "event type": Text("event.type")

         
        
    }
    extras = [
        Dictation("text"),
        IntegerRef("n",0,1000),
        IntegerRef('g', 0, 1000),
        IntegerRef('q',0,1000),
        Choice("method",{
            "push": ".push",
            "pop": ".pop",
            "shift": ".shift",
            "unshift": ".unshift",
            "to string": ".toString",
            "index of": ".indexOf",
            "slice":     ".slice",
            "split":    ".split",
            "join": ".join",
            "splice": ".splice",
            "map": ".map",
            "clear interval": "clearInterval",
            "type of": "typeof",
            "has own property": ".hasOwnProperty"
        }),
        Choice("direction",{
            "top": "Top",
            "bottom": "Bottom",
            "left": "Left",
            "right": "Right"
        })

    ]
    defaults = {
        "text": ""
    }




