from dragonfly import *



def bringer(app):
    newText = str(app).lower()
    print(newText)
    action = BringApp(newText)
    action.execute()


class BringMeRules(MappingRule):
    mapping = {
        "bring me <app>": Function(bringer),
    }

    extras = [
        Choice("app",{
            "code": "C:\Program Files (x86)\Microsoft VS Code\Code.exe",
            "chrome": "C:\Program Files (x86)\Google\Chrome\Application\chrome.exe"
        }),
        Dictation("text")
        
    ]
    defaults = {
        "text": ""
    }

   
