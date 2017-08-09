import re as re
from dragonfly import (Key, Function, Grammar, Playback,
                       IntegerRef, Dictation, Choice, WaitWindow, MappingRule, Text)
from dragonfluid import ActiveGrammarRule, GlobalRegistry, FluidRule, QuickFluidRules





def camelCase(text):
    text = str(text)
    newstring = text.lower()
    print(newstring)
    wordList = re.split('\W+',newstring)
    newList = []
    for word in wordList:
        if wordList.index(word) == 0:
            newList.append(word)
            pass
        else:
            word =list(word)
            word[0] = word[0].upper()
            word = "".join(word)
            newList.append(word)
    newstring= "".join(newList)
    return newstring

def scoreCase(text):
    text = str(text)
    text = text.lower()
    print(text)
    text = text.replace(" ","_")
    print(text)
    return text

def scoreText(text):
    text = scoreCase(text)
    Text(text, static = True).execute()   

   
def camelText(text):
    string = camelCase(text)
    Text(string,static=True).execute()
    

def forObj(text):    
    text = str(text).lower()
    words = re.split('\W+',text)
    first = words[0]
    words = " ".join(words[1:])
    print(words)
    words = camelCase(words)
    newString= "for " + first + " in " + words +":"
    Text(newString,static = True).execute()


class PythonRules(MappingRule):
    mapping = {
    '(lock Dragon | deactivate)':   Playback([(["go", "to", "sleep"], 0.0)]),    
    "slap [<n>]":                   Key('enter:%(n)d'),
    "tab":                          Key('tab'),
    "slatab":                       Key('enter') + Key('tab'),
    "for <text> <n>":              Text('for %(text)s in range(0,%(n)d):') + Key('enter') + Key('tab'),
    "for <text>":                   Function(forObj),
    "while <text>":                 Text('while %(text)s:') + Key("enter") +  Key("tab"),
    "stringify [<text>]":           Text('str(%(text)s)') + Key('left'),
    "linkin [<text>]":              Text('num(%(text)s))')+ Key('left'),
    #"[<text>]parents":              Text('%(text)s()') + Key('left'),
    "kerr":                         Text('{ }') + Key('left'),
    "brack":                        Text('[]')+ Key('left'),
    "[<text>] equals":              Text('%(text)s = '),
    "true":                         Text('True'),
    "false":                        Text('False'),
    "define <text>":                Text('def ')+ Function(camelText) + Text('():') + Key('left') + Key('left'),
    "power [<text>]":               Text('pow(%(text)s)'),
    "sroot [<text>]":               Text('math.sqrt(%(text)s)'),
    "length [<text>]":              Text("len(%(text)s)")+ Key('left'),
    "class <text>":                 Text('class ') + Function(camelText) + Text("():")+ Key('left')+ Key('left'),
    "new":                          Key('c-n'),
    "string [<text>]":              Text("'%(text)s'"),

    "initial":                      Text('def __init__():'),
    "mash <text>":                Text('self.') + Function(scoreText) + Text(' = '),
    "break":                        Text('break'),
    "ellis":                        Text('elif') + Key('space'),
    "pass":                         Text('pass'),
    "string [<text>]":              Text("'%(text)s'")+ Key('left'),
    "input|inputs":                 Text("input"),
    "said":                         Text("set"),

    
    
    }
    extras = [IntegerRef("n", 1, 10000),
              Dictation("text"),
              IntegerRef("q",1,1000),
             ]
    defaults = { 
               "text": "",
               "n" : 1,
               }





                                        


if __name__ == "__main__":
    import pythoncom, time
    # Ignore this if you're using Dragon
    print("Windows Speech Recognition / Dragonfly Test Running...")
    while True:
        pythoncom.PumpWaitingMessages()  # @UndefinedVariable
        time.sleep(.1)
