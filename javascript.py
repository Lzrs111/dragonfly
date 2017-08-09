from dragonfly import *
from python import camelCase, camelText



class JavaScriptMain(MappingRule):
    
    mapping = {
        "curly": Text("{}") + Key("left"),
        "this state [<text>]": Text("this.state.%(text)s"),
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
        "strict":   Text("strict"),
        "button|Boston": Text("button"),
        "on click|old click": Text(" onClick"),
        "return": Text("return"),
        "make array|make a ray": Text("[]"),
        "[<text>] plus equals": Text("%(text)s +="),
        'line <n> [<g>] [<q>]':  Key('%(n)d')+Key('%(g)d') +Key('%(q)d')+ Key('G'),
        "this dot": Text("this."),
        "rez|res|ref": Text("ref"),
        "import": Text("import"),
        "export": Text ("export"),
        "default": Text("default"),
        "class name": Text("className = ''") + Key("left"),

        #snippets
        "make [a new] class": Key("c-i"),
        "make [a new] state": Key("c-w"),
        "bind [a new] method": Key("c-e"),
        "set [a new] state": Key("c-r"),
        "make [a new] div": Key("c-j"),
        "make [a new] method": Key("c-g"),
        "make [a new] html": Key("c-h"),
        "make [a new] self closing": Key("c-l"),
        "make [a new] property": Key("c-p"),
        "make if": Key("c-y"),
        "make if else": Key("c-x"),
        "while|wild": Key("c-c"),
        "[make[a new]]arrow function": Key("c-v"),
        "call method": Key("c-b"),
        "log": Key("shift:down,c-q,shift:up"),
        "make [a new] generator": Key("c-n"),
        "make [a new] function": Key("shift:down,c-n,shift:up"),
        "make [a new] for loop": Key("c-m"),

        
        #array and string methods
        "[<text>] push": Text("%(text)s.push()") + Key("left"),
        "[<text>] pop":   Text("%(text)s.pop()") + Key("left"),
        "[<text>] unshift":   Text("%(text)s.unshift()") + Key("left"),
        "[<text>] shift":   Text("%(text)s.shift()") + Key("left"),
        "[<text>] map":     Text("%(text)s.map()") + Key("left"),
        "[<text>] slice":     Text("%(text)s.slice()") + Key("left"),
        "[<text>] splice":     Text("%(text)s.splice()") + Key("left"),
        "[<text>] split":     Text("%(text)s.split()") + Key("left"),
        "[<text>] join":     Text("%(text)s.join()") + Key("left"),
        "[<text>] to string": Text("%(text)s.toString()"),

        "[<text>] length": Text("%(text)s.length"),

        "parse integer": Text("parseInt()") + Key("left"),
        "parse float": Text("parseFloat()") + Key("left"),

        #math
        "math random": Text("Math.random()"),
        "math floor": Text("Math.floor()")


         
        
    }
    extras = [
        Dictation("text"),
        IntegerRef("n",0,1000),
        IntegerRef('g', 0, 1000),
        IntegerRef('q',0,1000)

    ]
    defaults = {
        "text": ""
    }




