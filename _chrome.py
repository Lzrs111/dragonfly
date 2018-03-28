from dragonfly import * 
from SeriesMappingRule import SeriesMappingRule

context = AppContext(executable="chrome")
grammar = Grammar("chrome", context=context)
noSpaceNoCaps = Mimic("\\no-caps-on") + Mimic("\\no-space-on")

rules = SeriesMappingRule(
    name = "chrome",
    mapping = {
      'go to start': Key('home'),
      "edit": Key("w-a"),
      "reload|refresh" : Key("f5"),
      "open": Key("escape, o"),
      "jump": Key("f"),
      "new tab":  Key('escape')+Key("t"),
      "console": Key("cs-j"),
      "close this": Key('escape')+Key("c-w"),
      "escape": Key('escape'),
      "new window": Key("c-n"),
      "switch to <choice>": Key("c-%(choice)s"), 
      "quit chrome": Key("shift:down,c-w,shift:up"),
      "open history": Key("c-h"),
      "open downloads": Key("c-j"),
      "focus shift": Key("f6"),
      "focus reshift": Key("s-f6"),
      "find": Key("c-f") + Pause("20"),
      "address bar": Key("c-l"),
      "open <website>": Key('f6')+ Pause('20')+Text("%(website)s") + Key("enter"),
      "show links":   Key('escape') + Key("f"),
      "copy": Key("c-v"),
      "paste": Key("c-p"),
      'copy link':Key("c-l") +  Key('c-c'),
      'previous tab': Key('shift:down,c-tab,shift:up'),
      'next tab': Key('c-tab'),
      'go back':Key('H'),
      'clear input': Key('shift:down,home,shift:up') + Key("backspace"),
      'my e-mail':Text("mario.dragovic@gmail.com"),
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
            "tweeter|twitter|tabtip|tpt": "https://www.twitter.com",
            'notifications':'https://twitter.com/i/notifications',
            "reddit": "https://www.reddit.com",
            'JavaScript':'https://developer.mozilla.org/bm/docs/Web/JavaScript/Reference',
            'Google':' http://www.google.com',
            'Pirate Bay':'https://thepiratebay.org/',
            'twitch':' HTTP://www.twitch.tv',
            'dragonfly key reference':'https://pythonhosted.org/dragonfly/actions.html',
            ' South Park':'http://southpark.cc.com/',
            'Japanese':'www.onejav.com',
            'Facebook':'www.Facebook.com',
            'github':'www.github.com',
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





