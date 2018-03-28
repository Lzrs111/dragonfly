from dragonfly import *
from SeriesMappingRule import SeriesMappingRule

terminalRule = SeriesMappingRule(
    name = "terminal rule",
    mapping = {
        "git <choice>": Text("git %(choice)s"),
        "node start": Text("npm start") + Key("enter"),
        'global':Text(" -g"),
        'save dev':Text(" -save-dev"),
        "make directory": Text("mkdir "),
        "change directory": Text("cd "),
        "open file": "invoke-item",
        "chrome": Text("chrome"),
        "change to desktop": Text("ctd") + Key("enter"),
        "dragon": Text("dragon") + Key("enter"),
        'node <command>':Text("npm %(command)s"),
        'stop this':Key("c-c"),
        'clear':Text("cls"),
        'heroku':Text("heroku "),
        'list directories':Text("ls")+Key("enter"),
        'enter':Key("enter"),
        'master':Text("master "),
    },
    extras = [
        Dictation("text"),
        Choice("choice",{
            "init": "init",
            "push": "push ",
            "pull": "pull ",
            "commit": "commit -m ",
            'add':'add .',

        }),
        #  commands for node
         Choice('command',{
             'in it|init':'init',
             'install':'install',
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