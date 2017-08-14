from dragonfly import *
from SeriesMappingRule import SeriesMappingRule

terminalRule = SeriesMappingRule(
    name = "terminal rule",
    mapping = {
        "git <choice>": Text("git %(choice)s"),
        "node start": Text("npm start") + Key("enter"),
        "make directory": Text("mkdir "),
        "change directory": Text("cd "),
        "new file": "new-item ",
        "open file": "invoke-item",
        "chrome": "chrome",
        "code": "code",
        "change to desktop": Text("ctd") + Key("enter"),
        "dragon": Text("dragon") + Key("enter")
    },
    extras = [
        Dictation("text"),
        Choice("choice",{
            "init": "init",
            "push": "push",
            "pull": "pull",
            "commit": "commit -m",

        })
    ],
    defaults = {
        "text" : ""
    }
)

grammar = Grammar("terminal grammar")
grammar.add_rule(terminalRule)
grammar.load()


def unload():
  global grammar
  if grammar: grammar.unload()
  grammar = None