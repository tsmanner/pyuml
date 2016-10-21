import antlr4
import importlib
import itertools
import json
import os
import re
import subprocess as sp


"""
Setup some module level information
"""
config = json.load(open("parser_config"))

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


class GenericListener:
    @staticmethod
    def print_node_context(listener, ctx):
        print(ctx)


class Language:
    def __init__(self, grammar_config: dict):
        """
        Take some grammar configuration information and create a language out of it.
            1.  Make sure we have a valid grammar file
            2.  Run ANTLR to generate the lexer, parser, and listener python modules
            3.  Import the ANTLR generated code
            4.  Assign passthroughs from this instance's listener to the generic listener
        """
        assert grammar_config["file"].endswith(".g4")
        gencmd = ' '.join(['java', '-jar', antlr_jar,
                           '-Dlanguage=Python3',
                           '-o', os.path.dirname(__file__) + os.sep + 'antlrpy',
                           grammar_config['file']])
        sp.run(gencmd, stdout=sp.PIPE)
        self.name = os.path.basename(grammar_config["file"])[:-3]
        importlib.invalidate_caches()  # Force new imports each time
        exec("import antlrpy." + self.name + "Lexer")
        exec("import antlrpy." + self.name + "Parser")
        exec("import antlrpy." + self.name + "Listener")

        class Listener(eval("antlrpy." + self.name + "Listener." + self.name + "Listener")):
            pass

        for rule in grammar_config["rules"]:
            entercmd = "Listener.enter" + grammar_config["rules"][rule].capitalize() +\
                       " = lambda x,y: print('enter_" + grammar_config["rules"][rule] + "')"
            print(entercmd)
            exec(entercmd)
            exitcmd = "Listener.exit" + grammar_config["rules"][rule].capitalize() + \
                      " = lambda x,y: print('exit_" + grammar_config["rules"][rule] + "')"
            print(exitcmd)
            exec(exitcmd)

        self.lexer = eval("antlrpy." + self.name + "Lexer." + self.name + "Lexer")
        self.parser = eval("antlrpy." + self.name + "Parser." + self.name + "Parser")
        self.listener = Listener

    def process(self, filename: str):
        lexer = self.lexer(antlr4.FileStream(filename))
        tokens = antlr4.CommonTokenStream(lexer)
        parser = self.parser(tokens)
        # TODO: This is the broken step... Figure out how to tell it which rule to start with
        parser.expression()
#        walker = antlr4.ParseTreeWalker()
#        walker.walk(self.listener(), parser.expression())


for grammar_name in config['grammars']:
    l = Language(config['grammars'][grammar_name])
    l.process("..\\L2LsuDrvr.h")
