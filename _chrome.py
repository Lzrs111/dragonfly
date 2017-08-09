from dragonfly import * 

context = AppContext(executable="chrome")
grammar = Grammar("chrome", context=context)
noSpaceNoCaps = Mimic("\\no-caps-on") + Mimic("\\no-space-on")

rules = MappingRule(
    name = "chrome",
    mapping = {
      "edit": Key("w-a"),
      "reload" : Key("f5"),
      "open": Key("escape, o"),
      "jump": Key("f"),
      "new tab": Key("t"),
      "console": Key("cs-j"),
      "close tab": Key("c-w"),
      "escape": Key('escape'),
      "new window": Key("c-n"),
      "tab <choice>": Key("c-%(choice)s"), 
      "quit chrome": Key("shift:down,c-w,shift:up"),
      "open history": Key("c-h"),
      "open downloads": Key("c-j"),
      "focus shift": Key("f6"),
      "focus reshift": Key("s-f6"),
      "find": Key("c-f") + Pause("20"),
      "address bar": Key("c-l"),
      "open <website>": Key("escape") + Pause("20") + Key("t") + Pause("20") + Text("%(website)s") + Key("enter"),
      "show links": Key("s-f"),

      },
    extras = [
        Dictation("text"),
        Integer("n", 0, 20000),
        Choice("choice",{
            "one": "1",
            "two": "2",
            "three|tree": "3",
            "four": "4",
            "five": "5",
            "six": "6",
            "seven":"7",
            "eight":"8",
        }),
        Choice("website",{
            "you tube": "https://www.youtube.com",
            "gee mail|gmail": "https://mail.google.com",
            "tweeter|twitter": "https://www.twitter.com",
            "plebbit|reddit": "https://www.reddit.com"
        })

      ],
    defaults = {
      "n" : 1
      }
    )

grammar.add_rule(rules)

grammar.load()

def unload():
  global grammar
  if grammar: grammar.unload()
  grammar = None
