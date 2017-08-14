from dragonfly import *

def maker(property):
    text = str(text).lower()
    print(text)
    govno = Key("c-w") + Text("%(text)s") + Key("right:2")
    govno.execute()

class CSSMain(MappingRule):
    mapping = {
        
        #snippets
        "make counter object": Key("c-m"),
        "make counter state": Key("c-w"),
        "set <property>": Key("c-w") + Text("%(property)s") + Key("right") + Pause("20"),

        #general words
        "solid": Text("solid"),
        "<n> pixels": Text("%(n)d")+Text("px"),
        "inline|in line": Text("inline"),
        "absolute|absolutes": Text("absolute"),
        "inline block": Text("inline-block"),
        "block": Text("block"),
        "flex": Text("flex"),
        "<n> percent": Text("%(n)d") + Text("%"),
        "margin [<direction>]": Text("margin")+ Text("%(direction)s"),
        "padding [<direction>]": Text("padding")+ Text("%(direction)s"),
        "keyframes": Text("@keyframes"),
    
    }
    extras = [
        Dictation("text"),
        IntegerRef("n",0,1000),
        IntegerRef('g', 0, 1000),
        IntegerRef('q',0,1000),
        Choice("direction", {
            "left": "-left",
            "right": "-right",
            "top":  "-top",
            "bottom": "-bottom"
        }),
        Choice("property", {
            "width|with": "width",
            "height": "height",
            "border": "border",
            "border radius": "border-radius",
            "background": "background",
            "display": "display",
            "background color": "background-color",
            "position": "position",
            "font family": "font-family",
            "font size": "font-size",
            "font color": "font-color",
            "text align": "text-align"
        })
    ]
    defaults = {
        "text": ""
    }
