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

      
        #NATO alphabet
	    "upper adam"    : Key("A"),
			"upper Alpha"    : Key("A"),
			"upper bravo"    : Key("B"),
			"upper Charlie"  : Key("C"),
			"upper Callie"   : Key("C"),
			"upper Delta"    : Key("D"),
			"upper echo"     : Key("E"),
			"upper foxtrot"  : Key("F"),
			"upper golf"     : Key("G"),
			"upper gamma"    : Key("G"),
      "upper Juliet"   : Key("J"),
      "upper hotel"    : Key("H"),
      "upper India"    : Key("I"),
      "upper iota"     : Key("I"),
      "upper kilo"     : Key("K"),
      "upper Lima"     : Key("L"),
      "upper Mike"     : Key("M"),
      "upper nancy" : Key("N"),
      "upper November" : Key("N"),
      "upper Oscar"    : Key("O"),
      "upper Papa"     : Key("P"),
      "upper Queen"    : Key("Q"),
      "upper Romeo"    : Key("R"),
      "upper Rico"     : Key("R"),
      "upper soy"      : Key("S"),
      "upper tango"    : Key("T"),
      "upper toy"      : Key("T"),
      "upper uniform"  : Key("U"),
      "upper Victor"   : Key("V"),
      "upper Van"      : Key("V"),
      "upper whiskey"  : Key("W"),
      "upper x-ray"    : Key("X"),
      "upper yellow"   : Key("Y"),
      "upper Zulu"     : Key("Z"),
      "upper zebra"    : Key("Z"),
      "Adam"    : Key("a"),
      "Alpha"    : Key("a"),
      "bravo"    : Key("b"),
      "Charlie"  : Key("c"),
      "Callie"   : Key("c"),
      "Delta"    : Key("d"),
      "echo"     : Key("e"),
      "foxtrot"  : Key("f"),
      "golf"     : Key("g"),
      "gamma"    : Key("g"),
      "Juliet"   : Key("j"),
      "hotel"    : Key("h"),
      "India"    : Key("i"),
      "iota"    : Key("i"),
      "kilo"     : Key("k"),
      "Lima"     : Key("l"),
      "Mike"     : Key("m"),
      "Nancy" : Key("n"),
      "November" : Key("n"),
      "Oscar"    : Key("o"),
      "Papa"     : Key("p"),
      "Queen"    : Key("q"),
      "Romeo"    : Key("r"),
      "Rico"     : Key("r"),
      "Sierra"      : Key("s"),
      "tango"    : Key("t"),
      "toy"      : Key("t"),
      "uniform"  : Key("u"),
      "Victor"   : Key("v"),
      "Van"      : Key("v"),
      "whiskey"  : Key("w"),
      "x-ray"    : Key("x"),
      "yellow"   : Key("y"),
      "Zulu"     : Key("z"),
      "zebra"    : Key("z"),
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
            'Facebook':'www.Facebook.com',
            'github':'www.github.com',
            'express':'https://expressjs.com/',
            'heroku':'www.heroku.com',
            'billing':'https://dashboard.heroku.com/account/billing',
            'mongo lab':'https://mlab.com/',
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





