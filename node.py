from dragonfly import *
from python import camelCase, camelText

pause = Pause("20")
norm = Key("escape") + pause
    
class NodeRules(MappingRule):
    
    mapping = {
        'request response':Text("req,res"),
        'request':Text("req"),
        'response':Text("res"),
        'file system':Text("fs"),
        'url':Text("url"),
        'post':Text("POST"),
        'get':Text("GET"),
        'big request':Text("Request"),
        'fetch':Text(".fetch()"),
        'parse':Text(".parse()"),
        'html':Text("html"),
        'http':Text("http"),
        'require <module>':Text("var %(module)s  = require('%(module)s')"),
        'module exports':Text("module.exports = {}")+Pause("20")+Key("left"),
    }
    extras = [
        Dictation("text"),
        IntegerRef("n",0,1000),
        Choice('module',{
            "file system":"fs",
            'url':"url",
            'http':'http',
        })
    ]
    defaults = {
        "text": ""
    }




