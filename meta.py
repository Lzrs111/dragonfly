from dragonfly import *
from SeriesMappingRule import *

#  the aim of this module is to facilitate creation of dragonfly commands
context = AppContext(executable="code")
grammar = Grammar('dragonfly',context=context)

def filer():
    action = Playback([(["click","file"],3.0)])
    action2 = Playback([(["click",'new','file'],1.0)])
        
    action.execute()
    action2.execute()
    
class DragonflyRules(MappingRule):
    mapping =  {
        'make command': Text('makedragonflycommand')+Pause("20")+ Key("tab"),
        'Dragonfly key':Text('Key("")') + Key('left:2'),
        'dragonfly text': Text('Text("")')+Key('left:2'),
        'dragonfly pause':Text('Pause("")')+Key('left:2'),
        'make a new snippet':Text("makenewsnippet")+Pause("20")+Key("tab"),
        'dragonfly mimic':Text("Mimic("")")+Pause("20")+Key("left:2"),
        ' dragonfly playback':Text("Playback()")+Key("left"),
        'open new file':Function(filer)
    }
    extras = [
        Dictation('text'),
        Integer('n', 0, 2000)
    ]    
    defaults = {
        'n':1
    }

