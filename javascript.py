from dragonfly import *
from python import camelCase, camelText

pause = Pause("20")
norm = Key("escape") + pause
    
class JavaScriptMain(MappingRule):
    
    mapping = {
        "lesser variable [<text>]": Text("let %(text)s = "),
        "constant [<text>]": Text("const %(text)s = "),
        "constructor": Text("constructor() {}"),
        "super": Text("super()"),
        "parents": Text("()"),
        "[<text>] equals":  Text(" = "),
        "on click|old click": Text(" onClick"),
        "return": Text("return "),
        "[<text>] plus equals": Text("%(text)s +="),
        'line <n> [<g>] [<q>]':  Key('escape') + pause + Key('%(n)d')+Key('%(g)d') +Key('%(q)d')+ Key('G'),
        "this dot": Text("this."),
        "rez|res|ref": Text("ref"),
        "export": Text ("export "),
        "default": Text("default "),
        "class name": Text(" className = ''") + Key("left"),
        "make string": Text("''")+ pause + Key("left") + pause,
        "logical and": pause + Text("&&") + pause,
        "logical or": pause + Text ("||") + pause,
        'tab':Pause("50")+Key("tab")+Pause("50"),

        #snippets
        'make if':Text("makeif")+Pause("20")+Key("tab"),
        "make else if": pause + Text("makeelsif") + pause + Key("tab"),
        "make else": pause + Text("makeelse!") + pause + Key("tab"),
        "while|wild": Text("makewhile")+pause+Key('tab'),
        "[make[a new]]arrow function": Text("arf")+Pause("20") +Key("tab"),
        "console log":Text("clog") +pause+Key("tab"),
        "make [a new] generator": Key("c-n"),
        "make [a new] function": pause + Text("cfun") + pause + Key("tab"),
        "make [a new] for loop":Text("makefor")+Pause("20")+ Key("tab"),
        'make for in':Text("forin")+Pause("20")+Key("tab"),
        'make for each':Text("foreach")+Pause("20")+Key('tab'),
        "make conditional": Key("c-k"),
        "make curly": Text("curl")+Pause("20")+Key("tab"),
        'make array':Key("shift:down")+Key("c-a"),
        "set timeout": pause + Text("settimeout") + pause + Key("tab"),
        "set interval": pause + Text("setinterval") + pause + Key("tab"),
        "make import": pause + Text("makeimport") + pause + Key("tab"),
        "import see ess ess": pause + Text("importcss") + pause + Key("tab"),
        'make new':Text("new")+Pause("20")+Key("tab"),
        'make require':Text("makerequire")+Pause(" 20")+Key("tab"),
        'make variable':Text("makevar")+Pause(" 20")+Key("tab"),
        'make comparison':Text("makeequals")+Pause(" 20")+Key('tab'),
        'make logical or':Text("makeor")+Pause("20")+Key('tab'),
        'make logical and':Text("makeand")+Pause("20")+Key('tab'),
        'make webpack config':Text("webpackpreset")+Pause("20")+Key('tab'),
        
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




