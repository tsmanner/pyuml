import antlr4
import itertools
import json
import os
import re
import subprocess as sp


class GenericListener:
    @staticmethod
    def print_node_context(ctx):
        print(ctx)


class Language:
    def __init__(self, grammar):
        self.name = grammar["name"]
        exec("import antlrpy." + self.name + "Lexer")
        exec("import antlrpy." + self.name + "Parser")
        exec("import antlrpy." + self.name + "Listener")

        # TODO: Make this dynamically generated per language with the function
        # TODO:     associations defined in antlr_config.json
        class AListener(eval("antlrpy." + self.name + "Listener." + self.name + "Listener")):
            def enterClassname(self, ctx):
                GenericListener.print_node_context(ctx)

        self.lexer = eval("antlrpy." + self.name + "Lexer." + self.name + "Lexer")
        self.parser = eval("antlrpy." + self.name + "Parser." + self.name + "Parser")
        self.listener = AListener

    def process(self, filename: str):
        lexer = self.lexer(antlr4.FileStream(filename))
        tokens = antlr4.CommonTokenStream(lexer)
        parser = self.parser(tokens)
        listener = self.listener()
        tree = parser.expression()
        walker = antlr4.ParseTreeWalker()
        walker.walk(listener, tree)

config = json.load(open("antlr_config.json"))

antlr_jar = ''
max_version = '0'
for fl in os.listdir('.'):
    match = re.match('antlr(-)?((\d+\.?)+)?(-\w+)?.jar', fl)
    if match:
        version = match.group(2)
        for tpl in itertools.zip_longest(version.split('.'), max_version.split('.')):
            if tpl[1] is None:
                max_version = version
                antlr_jar = fl
            elif tpl[0] is None:
                continue
            elif int(tpl[0]) > int(tpl[1]):
                max_version = version
                antlr_jar = fl
            else:
                continue
if antlr_jar == '':
    exit("No antlr jar found!")


for grammar in config['grammars']:
    cmd = ' '.join(['java', '-jar', antlr_jar,
                    '-Dlanguage=Python3',
                    '-o', os.path.dirname(grammar['file']),
                    grammar['file']])
#    print(cmd)
    proc = sp.run(cmd, stdout=sp.PIPE)
#    print(proc)
#    print(proc.stdout)
    l = Language(grammar)
    l.process("..\\L2LsuDrvr.h")

#    import parsing.CPP14Lexer
#    import parsing.CPP14Parser
#    import parsing.CPP14Listener

#    lexer = parsing.CPP14Lexer.CPP14Lexer(antlr4.FileStream("..\\L2LsuDrvr.h"))
#    tokens = antlr4.CommonTokenStream(lexer)
#    parser = parsing.CPP14Parser.CPP14Parser(tokens)

#    class ThisListener(parsing.CPP14Listener.CPP14Listener):
#        def enterClassname(self, ctx):
#            GenericListener.print_node_context(ctx)

#    listener = ThisListener()
#    tree = parser.expression()
#    walker = antlr4.ParseTreeWalker()
#    walker.walk(listener, tree)
