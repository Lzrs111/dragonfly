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
            "macro|macros": "C:\NatLink\NatLink\MacroSystem",
            "notepad": "C:\Windows\\notepad.exe"
            
        }),
        Dictation("text")
        
    ]
    defaults = {
        "text": ""
    }


grammar = Grammar("bring me")
grammar.add_rule(BringMeRules())
grammar.load()
print("loaded bring me!")
   
def unload():
    global grammar
    if grammar: grammar.unload()
    grammar = None