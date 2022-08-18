# Generated from IsiLang.g4 by ANTLR 4.10.1
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
    from typing import TextIO
else:
    from typing.io import TextIO


sys.path.append("../..")
from AnalisadorLexicoPython.datastructures.IsiSymbol import IsiSymbol
from AnalisadorLexicoPython.datastructures.IsiVariable import IsiVariable
from AnalisadorLexicoPython.datastructures.IsiSymbolTable import IsiSymbolTable
from AnalisadorLexicoPython.exceptions.IsiSemanticException import IsiSemanticException
from AnalisadorLexicoPython.ast.IsiProgram import IsiProgram
from AnalisadorLexicoPython.ast.AbstractCommand import AbstractCommand
from AnalisadorLexicoPython.ast.CommandLeitura import CommandLeitura
from AnalisadorLexicoPython.ast.CommandEscrita import CommandEscrita
from AnalisadorLexicoPython.ast.CommandAtribuicao import CommandAtribuicao
from AnalisadorLexicoPython.ast.CommandDecisao import CommandDecisao
from AnalisadorLexicoPython.datastructures.IsiEnumType import IsiEnumType
from AnalisadorLexicoPython.parser.IsiParserHelper import IsiParserHelper


parseHelper = IsiParserHelper()




def serializedATN():
    return [
        4,0,20,145,6,-1,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,
        2,6,7,6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,
        13,7,13,2,14,7,14,2,15,7,15,2,16,7,16,2,17,7,17,2,18,7,18,2,19,7,
        19,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,1,1,1,1,1,1,1,1,1,1,1,1,
        1,1,1,1,1,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,3,1,3,1,3,1,3,1,3,1,3,1,
        4,1,4,1,4,1,4,1,4,1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,6,1,6,1,6,1,
        7,1,7,1,7,1,7,1,7,1,7,1,8,1,8,1,9,1,9,1,10,1,10,1,11,1,11,1,12,1,
        12,1,13,1,13,1,14,1,14,1,15,1,15,1,16,1,16,1,16,1,16,1,16,1,16,1,
        16,1,16,1,16,3,16,120,8,16,1,17,1,17,5,17,124,8,17,10,17,12,17,127,
        9,17,1,18,4,18,130,8,18,11,18,12,18,131,1,18,1,18,4,18,136,8,18,
        11,18,12,18,137,3,18,140,8,18,1,19,1,19,1,19,1,19,0,0,20,1,1,3,2,
        5,3,7,4,9,5,11,6,13,7,15,8,17,9,19,10,21,11,23,12,25,13,27,14,29,
        15,31,16,33,17,35,18,37,19,39,20,1,0,6,3,0,42,43,45,45,47,47,2,0,
        60,60,62,62,1,0,97,122,3,0,48,57,65,90,97,122,1,0,48,57,3,0,9,10,
        13,13,32,32,152,0,1,1,0,0,0,0,3,1,0,0,0,0,5,1,0,0,0,0,7,1,0,0,0,
        0,9,1,0,0,0,0,11,1,0,0,0,0,13,1,0,0,0,0,15,1,0,0,0,0,17,1,0,0,0,
        0,19,1,0,0,0,0,21,1,0,0,0,0,23,1,0,0,0,0,25,1,0,0,0,0,27,1,0,0,0,
        0,29,1,0,0,0,0,31,1,0,0,0,0,33,1,0,0,0,0,35,1,0,0,0,0,37,1,0,0,0,
        0,39,1,0,0,0,1,41,1,0,0,0,3,50,1,0,0,0,5,59,1,0,0,0,7,66,1,0,0,0,
        9,72,1,0,0,0,11,77,1,0,0,0,13,85,1,0,0,0,15,88,1,0,0,0,17,94,1,0,
        0,0,19,96,1,0,0,0,21,98,1,0,0,0,23,100,1,0,0,0,25,102,1,0,0,0,27,
        104,1,0,0,0,29,106,1,0,0,0,31,108,1,0,0,0,33,119,1,0,0,0,35,121,
        1,0,0,0,37,129,1,0,0,0,39,141,1,0,0,0,41,42,5,112,0,0,42,43,5,114,
        0,0,43,44,5,111,0,0,44,45,5,103,0,0,45,46,5,114,0,0,46,47,5,97,0,
        0,47,48,5,109,0,0,48,49,5,97,0,0,49,2,1,0,0,0,50,51,5,102,0,0,51,
        52,5,105,0,0,52,53,5,109,0,0,53,54,5,112,0,0,54,55,5,114,0,0,55,
        56,5,111,0,0,56,57,5,103,0,0,57,58,5,59,0,0,58,4,1,0,0,0,59,60,5,
        110,0,0,60,61,5,117,0,0,61,62,5,109,0,0,62,63,5,101,0,0,63,64,5,
        114,0,0,64,65,5,111,0,0,65,6,1,0,0,0,66,67,5,116,0,0,67,68,5,101,
        0,0,68,69,5,120,0,0,69,70,5,116,0,0,70,71,5,111,0,0,71,8,1,0,0,0,
        72,73,5,108,0,0,73,74,5,101,0,0,74,75,5,105,0,0,75,76,5,97,0,0,76,
        10,1,0,0,0,77,78,5,101,0,0,78,79,5,115,0,0,79,80,5,99,0,0,80,81,
        5,114,0,0,81,82,5,101,0,0,82,83,5,118,0,0,83,84,5,97,0,0,84,12,1,
        0,0,0,85,86,5,115,0,0,86,87,5,101,0,0,87,14,1,0,0,0,88,89,5,115,
        0,0,89,90,5,101,0,0,90,91,5,110,0,0,91,92,5,97,0,0,92,93,5,111,0,
        0,93,16,1,0,0,0,94,95,5,40,0,0,95,18,1,0,0,0,96,97,5,41,0,0,97,20,
        1,0,0,0,98,99,5,59,0,0,99,22,1,0,0,0,100,101,7,0,0,0,101,24,1,0,
        0,0,102,103,5,61,0,0,103,26,1,0,0,0,104,105,5,44,0,0,105,28,1,0,
        0,0,106,107,5,123,0,0,107,30,1,0,0,0,108,109,5,125,0,0,109,32,1,
        0,0,0,110,120,7,1,0,0,111,112,5,62,0,0,112,120,5,61,0,0,113,114,
        5,60,0,0,114,120,5,61,0,0,115,116,5,61,0,0,116,120,5,61,0,0,117,
        118,5,33,0,0,118,120,5,61,0,0,119,110,1,0,0,0,119,111,1,0,0,0,119,
        113,1,0,0,0,119,115,1,0,0,0,119,117,1,0,0,0,120,34,1,0,0,0,121,125,
        7,2,0,0,122,124,7,3,0,0,123,122,1,0,0,0,124,127,1,0,0,0,125,123,
        1,0,0,0,125,126,1,0,0,0,126,36,1,0,0,0,127,125,1,0,0,0,128,130,7,
        4,0,0,129,128,1,0,0,0,130,131,1,0,0,0,131,129,1,0,0,0,131,132,1,
        0,0,0,132,139,1,0,0,0,133,135,5,46,0,0,134,136,7,4,0,0,135,134,1,
        0,0,0,136,137,1,0,0,0,137,135,1,0,0,0,137,138,1,0,0,0,138,140,1,
        0,0,0,139,133,1,0,0,0,139,140,1,0,0,0,140,38,1,0,0,0,141,142,7,5,
        0,0,142,143,1,0,0,0,143,144,6,19,0,0,144,40,1,0,0,0,7,0,119,123,
        125,131,137,139,1,6,0,0
    ]

class IsiLangLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    T__0 = 1
    T__1 = 2
    T__2 = 3
    T__3 = 4
    T__4 = 5
    T__5 = 6
    T__6 = 7
    T__7 = 8
    AP = 9
    FP = 10
    SC = 11
    OP = 12
    ATTR = 13
    VIR = 14
    ACH = 15
    FCH = 16
    OPREL = 17
    ID = 18
    NUMBER = 19
    WS = 20

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'programa'", "'fimprog;'", "'numero'", "'texto'", "'leia'", 
            "'escreva'", "'se'", "'senao'", "'('", "')'", "';'", "'='", 
            "','", "'{'", "'}'" ]

    symbolicNames = [ "<INVALID>",
            "AP", "FP", "SC", "OP", "ATTR", "VIR", "ACH", "FCH", "OPREL", 
            "ID", "NUMBER", "WS" ]

    ruleNames = [ "T__0", "T__1", "T__2", "T__3", "T__4", "T__5", "T__6", 
                  "T__7", "AP", "FP", "SC", "OP", "ATTR", "VIR", "ACH", 
                  "FCH", "OPREL", "ID", "NUMBER", "WS" ]

    grammarFileName = "IsiLang.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.10.1")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None



    def GetIsiParseHelper(self):
        return parseHelper



