from dragonfly import *



def bringer(app):
    newText = str(app).lower()
    print(newText)
    action = BringApp(newText)
    action.execute()


class BringMeRules(MappingRule):
    mapping = {
        "open <app>": Function(bringer),
    }

    extras = [
        Choice("app",{
            "code": "C:\Program Files (x86)\Microsoft VS Code\Code.exe",
            "chrome": "C:\Program Files (x86)\Google\Chrome\Application\chrome.exe",
            "notepad": "C:\Windows\\notepad.exe",
            'video player':"C:\Program Files (x86)\Webteh\BSPlayer/bsplayer.exe",
        }),
       Dictation("text")
    ]
    defaults = {
        "text": ""
    }


grammar = Grammar("bring me")
grammar.add_rule(BringMeRules())
grammar.load()
   
def unload():
    global grammar
    if grammar: grammar.unload()
    grammar = None