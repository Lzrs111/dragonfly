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
        'make new item':Text("New-Item "),
        "chrome": Text("chrome"),
        'code':Text("code "),
        "change to desktop": Text("ctd") + Key("enter"),
        "dragon": Text("dragon") + Key("enter"),
        'node <command>':Text("npm %(command)s"),
        'stop this':Key("c-c"),
        'clear':Text("cls"),
        'heroku <extension>':Text("heroku %(extension)s"),
        'list directories':Text("ls")+Key("enter"),
        'enter':Key("enter"),
        'master':Text(" master "),
        'open current project':Text("code C:/Users/Mario/Desktop/biscel")+Key("enter"),
        'open macros':Text("code C:/NatLink/NatLink/MacroSystem"),
        'node install [<module>]':Text("npm install %(module)s"),
        'rerun':Key("up")+Key('enter'),
        '.js|dot jay ess':Text(".js"),
        'node':Text("node "),
        'git ignore':Text(".gitignore"),
        'Babel RC':Text(".babelrc"),
        'webpack watch':Text('webpack-dev-server --watch-content-base'),
        'webpack config':Text("webpack.config.js"),
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
         }),
          Choice('extension',{
              'create scheduler':'addons:create scheduler:standard',
              'run scheduler':'addons:open scheduler',
              'logs':"logs",
          }),
          Choice('module',{
              'mongo':"mongodb",
              'mongoose':'mongoose',
              'react':'react react-dom',
              'webpack':'webpack webpack-dev-server webpack-cli --save-dev',
              'Babel':'--save-dev babel-cli babel-preset-env',
              'no demon':"nodemon --save-dev",
              'express':'express',

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