from dragonfly import *
from python import camelCase, camelText

pause = Pause("20")
norm = Key("escape") + pause
    
class ReactRule(MappingRule):
    
    mapping = {
        'make react class':Text("reactclass")+pause+Key('tab'),
        'component will mount':Text("cwm")+pause+Key('tab'),
        'bind method':Text("bnd")+pause+Key('tab'),
        "make [a new] method":Text("mmethod")+pause+Key('tab'),
        "make [a new] state":Text("setstt")+pause+Key('tab'), 
        'call method':Text("cmet")+pause+Key('tab'),
        "make [a new] property":Text("makeprop")+pause+Key('tab'),
        "make [a new] div": Text("makediv")+ pause + Key("tab"),
        "make [a new] html":Text("hta")+pause+Key("tab") ,
        "make [a new] self closing":Text("htb")+pause+Key('tab'),
        'set state':Text("setState")+pause+Key("tab"),
    }
    extras = [
        Dictation("text"),
        IntegerRef("n",0,1000),
    ]
    defaults = {
        "text": ""
    }




