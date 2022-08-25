# Generated from IsiLang.g4 by ANTLR 4.10.1
# encoding: utf-8
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
from AnalisadorLexicoPython.ast.CommandRepeticao import CommandRepeticao
from AnalisadorLexicoPython.ast.CommandCaso import CommandCaso


parseHelper = IsiParserHelper()



def serializedATN():
    return [
        4,1,27,252,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,13,7,13,
        2,14,7,14,1,0,1,0,1,0,1,0,1,0,1,0,1,1,4,1,38,8,1,11,1,12,1,39,1,
        2,1,2,1,2,1,2,1,2,1,2,5,2,48,8,2,10,2,12,2,51,9,2,1,2,1,2,1,3,1,
        3,1,3,1,3,3,3,59,8,3,1,4,1,4,4,4,63,8,4,11,4,12,4,64,1,5,1,5,1,5,
        1,5,1,5,1,5,3,5,73,8,5,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,7,1,7,1,
        7,1,7,1,7,1,7,3,7,89,8,7,1,7,1,7,1,7,1,7,1,8,1,8,1,8,1,8,1,8,1,8,
        1,8,1,8,1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,3,9,112,8,9,1,9,1,9,
        1,9,1,9,1,9,4,9,119,8,9,11,9,12,9,120,1,9,1,9,1,9,1,9,1,9,1,9,4,
        9,129,8,9,11,9,12,9,130,1,9,1,9,1,9,3,9,136,8,9,1,9,1,9,1,10,1,10,
        1,10,1,10,1,10,1,10,3,10,146,8,10,1,10,1,10,1,10,1,10,1,10,1,10,
        1,10,1,10,3,10,156,8,10,1,10,1,10,1,10,1,10,4,10,162,8,10,11,10,
        12,10,163,1,10,1,10,1,10,1,10,3,10,170,8,10,1,10,1,10,4,10,174,8,
        10,11,10,12,10,175,1,10,1,10,1,10,1,10,4,10,182,8,10,11,10,12,10,
        183,1,10,1,10,3,10,188,8,10,1,10,1,10,1,10,1,11,1,11,1,11,1,11,1,
        11,1,11,1,11,1,11,1,11,3,11,202,8,11,1,11,1,11,1,11,1,11,1,11,4,
        11,209,8,11,11,11,12,11,210,1,11,1,11,1,11,1,12,1,12,1,12,1,12,5,
        12,220,8,12,10,12,12,12,223,9,12,1,12,1,12,1,12,1,12,1,12,1,12,1,
        12,1,12,1,12,3,12,234,8,12,1,13,1,13,1,13,1,13,1,13,1,13,3,13,242,
        8,13,1,14,1,14,1,14,1,14,1,14,1,14,3,14,250,8,14,1,14,0,0,15,0,2,
        4,6,8,10,12,14,16,18,20,22,24,26,28,0,0,266,0,30,1,0,0,0,2,37,1,
        0,0,0,4,41,1,0,0,0,6,58,1,0,0,0,8,60,1,0,0,0,10,72,1,0,0,0,12,74,
        1,0,0,0,14,82,1,0,0,0,16,94,1,0,0,0,18,102,1,0,0,0,20,139,1,0,0,
        0,22,192,1,0,0,0,24,233,1,0,0,0,26,241,1,0,0,0,28,249,1,0,0,0,30,
        31,5,1,0,0,31,32,3,2,1,0,32,33,3,8,4,0,33,34,5,2,0,0,34,35,6,0,-1,
        0,35,1,1,0,0,0,36,38,3,4,2,0,37,36,1,0,0,0,38,39,1,0,0,0,39,37,1,
        0,0,0,39,40,1,0,0,0,40,3,1,0,0,0,41,42,3,6,3,0,42,43,5,23,0,0,43,
        49,6,2,-1,0,44,45,5,19,0,0,45,46,5,23,0,0,46,48,6,2,-1,0,47,44,1,
        0,0,0,48,51,1,0,0,0,49,47,1,0,0,0,49,50,1,0,0,0,50,52,1,0,0,0,51,
        49,1,0,0,0,52,53,5,16,0,0,53,5,1,0,0,0,54,55,5,3,0,0,55,59,6,3,-1,
        0,56,57,5,4,0,0,57,59,6,3,-1,0,58,54,1,0,0,0,58,56,1,0,0,0,59,7,
        1,0,0,0,60,62,6,4,-1,0,61,63,3,10,5,0,62,61,1,0,0,0,63,64,1,0,0,
        0,64,62,1,0,0,0,64,65,1,0,0,0,65,9,1,0,0,0,66,73,3,12,6,0,67,73,
        3,14,7,0,68,73,3,16,8,0,69,73,3,18,9,0,70,73,3,22,11,0,71,73,3,20,
        10,0,72,66,1,0,0,0,72,67,1,0,0,0,72,68,1,0,0,0,72,69,1,0,0,0,72,
        70,1,0,0,0,72,71,1,0,0,0,73,11,1,0,0,0,74,75,5,5,0,0,75,76,5,14,
        0,0,76,77,5,23,0,0,77,78,6,6,-1,0,78,79,5,15,0,0,79,80,5,16,0,0,
        80,81,6,6,-1,0,81,13,1,0,0,0,82,83,5,6,0,0,83,88,5,14,0,0,84,85,
        5,23,0,0,85,89,6,7,-1,0,86,87,5,25,0,0,87,89,6,7,-1,0,88,84,1,0,
        0,0,88,86,1,0,0,0,89,90,1,0,0,0,90,91,5,15,0,0,91,92,5,16,0,0,92,
        93,6,7,-1,0,93,15,1,0,0,0,94,95,5,23,0,0,95,96,6,8,-1,0,96,97,5,
        18,0,0,97,98,6,8,-1,0,98,99,3,24,12,0,99,100,5,16,0,0,100,101,6,
        8,-1,0,101,17,1,0,0,0,102,103,5,7,0,0,103,104,5,14,0,0,104,105,5,
        23,0,0,105,106,6,9,-1,0,106,107,5,22,0,0,107,111,6,9,-1,0,108,109,
        5,23,0,0,109,112,6,9,-1,0,110,112,5,24,0,0,111,108,1,0,0,0,111,110,
        1,0,0,0,112,113,1,0,0,0,113,114,6,9,-1,0,114,115,5,15,0,0,115,116,
        5,20,0,0,116,118,6,9,-1,0,117,119,3,10,5,0,118,117,1,0,0,0,119,120,
        1,0,0,0,120,118,1,0,0,0,120,121,1,0,0,0,121,122,1,0,0,0,122,123,
        5,21,0,0,123,135,6,9,-1,0,124,125,5,8,0,0,125,126,5,20,0,0,126,128,
        6,9,-1,0,127,129,3,10,5,0,128,127,1,0,0,0,129,130,1,0,0,0,130,128,
        1,0,0,0,130,131,1,0,0,0,131,132,1,0,0,0,132,133,5,21,0,0,133,134,
        6,9,-1,0,134,136,1,0,0,0,135,124,1,0,0,0,135,136,1,0,0,0,136,137,
        1,0,0,0,137,138,6,9,-1,0,138,19,1,0,0,0,139,140,5,9,0,0,140,145,
        5,14,0,0,141,142,5,23,0,0,142,146,6,10,-1,0,143,146,5,24,0,0,144,
        146,5,25,0,0,145,141,1,0,0,0,145,143,1,0,0,0,145,144,1,0,0,0,146,
        147,1,0,0,0,147,148,6,10,-1,0,148,149,5,15,0,0,149,173,5,20,0,0,
        150,155,5,10,0,0,151,152,5,23,0,0,152,156,6,10,-1,0,153,156,5,24,
        0,0,154,156,5,25,0,0,155,151,1,0,0,0,155,153,1,0,0,0,155,154,1,0,
        0,0,156,157,1,0,0,0,157,158,6,10,-1,0,158,159,5,27,0,0,159,161,6,
        10,-1,0,160,162,3,10,5,0,161,160,1,0,0,0,162,163,1,0,0,0,163,161,
        1,0,0,0,163,164,1,0,0,0,164,165,1,0,0,0,165,169,6,10,-1,0,166,167,
        5,11,0,0,167,168,6,10,-1,0,168,170,5,16,0,0,169,166,1,0,0,0,169,
        170,1,0,0,0,170,171,1,0,0,0,171,172,6,10,-1,0,172,174,1,0,0,0,173,
        150,1,0,0,0,174,175,1,0,0,0,175,173,1,0,0,0,175,176,1,0,0,0,176,
        187,1,0,0,0,177,178,5,12,0,0,178,179,5,27,0,0,179,181,6,10,-1,0,
        180,182,3,10,5,0,181,180,1,0,0,0,182,183,1,0,0,0,183,181,1,0,0,0,
        183,184,1,0,0,0,184,185,1,0,0,0,185,186,6,10,-1,0,186,188,1,0,0,
        0,187,177,1,0,0,0,187,188,1,0,0,0,188,189,1,0,0,0,189,190,5,21,0,
        0,190,191,6,10,-1,0,191,21,1,0,0,0,192,193,5,13,0,0,193,194,5,14,
        0,0,194,195,5,23,0,0,195,196,6,11,-1,0,196,197,5,22,0,0,197,201,
        6,11,-1,0,198,199,5,23,0,0,199,202,6,11,-1,0,200,202,5,24,0,0,201,
        198,1,0,0,0,201,200,1,0,0,0,202,203,1,0,0,0,203,204,6,11,-1,0,204,
        205,5,15,0,0,205,206,5,20,0,0,206,208,6,11,-1,0,207,209,3,10,5,0,
        208,207,1,0,0,0,209,210,1,0,0,0,210,208,1,0,0,0,210,211,1,0,0,0,
        211,212,1,0,0,0,212,213,5,21,0,0,213,214,6,11,-1,0,214,23,1,0,0,
        0,215,221,3,28,14,0,216,217,5,17,0,0,217,218,6,12,-1,0,218,220,3,
        28,14,0,219,216,1,0,0,0,220,223,1,0,0,0,221,219,1,0,0,0,221,222,
        1,0,0,0,222,224,1,0,0,0,223,221,1,0,0,0,224,225,3,26,13,0,225,234,
        1,0,0,0,226,227,5,14,0,0,227,228,6,12,-1,0,228,229,3,24,12,0,229,
        230,5,15,0,0,230,231,6,12,-1,0,231,232,3,26,13,0,232,234,1,0,0,0,
        233,215,1,0,0,0,233,226,1,0,0,0,234,25,1,0,0,0,235,236,5,17,0,0,
        236,237,6,13,-1,0,237,238,3,24,12,0,238,239,3,26,13,0,239,242,1,
        0,0,0,240,242,1,0,0,0,241,235,1,0,0,0,241,240,1,0,0,0,242,27,1,0,
        0,0,243,244,5,23,0,0,244,250,6,14,-1,0,245,246,5,24,0,0,246,250,
        6,14,-1,0,247,248,5,25,0,0,248,250,6,14,-1,0,249,243,1,0,0,0,249,
        245,1,0,0,0,249,247,1,0,0,0,250,29,1,0,0,0,23,39,49,58,64,72,88,
        111,120,130,135,145,155,163,169,175,183,187,201,210,221,233,241,
        249
    ]

class IsiLangParser ( Parser ):

    grammarFileName = "IsiLang.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'programa'", "'fimprog;'", "'numero'", 
                     "'texto'", "'leia'", "'escreva'", "'se'", "'senao'", 
                     "'escolha'", "'caso'", "'break'", "'default'", "'enquanto'", 
                     "'('", "')'", "';'", "<INVALID>", "'='", "','", "'{'", 
                     "'}'", "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "':'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "AP", "FP", "SC", "OP", 
                      "ATTR", "VIR", "ACH", "FCH", "OPREL", "ID", "NUMBER", 
                      "TEXT", "WS", "DP" ]

    RULE_prog = 0
    RULE_decl = 1
    RULE_declaravar = 2
    RULE_tipo = 3
    RULE_bloco = 4
    RULE_cmd = 5
    RULE_cmdleitura = 6
    RULE_cmdescrita = 7
    RULE_cmdattrib = 8
    RULE_cmdselecao = 9
    RULE_cmdcaso = 10
    RULE_cmdrepeticao = 11
    RULE_expr = 12
    RULE_exprL = 13
    RULE_termo = 14

    ruleNames =  [ "prog", "decl", "declaravar", "tipo", "bloco", "cmd", 
                   "cmdleitura", "cmdescrita", "cmdattrib", "cmdselecao", 
                   "cmdcaso", "cmdrepeticao", "expr", "exprL", "termo" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    T__3=4
    T__4=5
    T__5=6
    T__6=7
    T__7=8
    T__8=9
    T__9=10
    T__10=11
    T__11=12
    T__12=13
    AP=14
    FP=15
    SC=16
    OP=17
    ATTR=18
    VIR=19
    ACH=20
    FCH=21
    OPREL=22
    ID=23
    NUMBER=24
    TEXT=25
    WS=26
    DP=27

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.10.1")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    def GetIsiParseHelper(self):
        return parseHelper




    class ProgContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def decl(self):
            return self.getTypedRuleContext(IsiLangParser.DeclContext,0)


        def bloco(self):
            return self.getTypedRuleContext(IsiLangParser.BlocoContext,0)


        def getRuleIndex(self):
            return IsiLangParser.RULE_prog

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterProg" ):
                listener.enterProg(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitProg" ):
                listener.exitProg(self)




    def prog(self):

        localctx = IsiLangParser.ProgContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_prog)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 30
            self.match(IsiLangParser.T__0)
            self.state = 31
            self.decl()
            self.state = 32
            self.bloco()
            self.state = 33
            self.match(IsiLangParser.T__1)

            parseHelper.program.setVarTable(parseHelper.symbolTable)
            parseHelper.verificaVariavelUtilizada()
            parseHelper.program.setComandos(parseHelper.stack.pop())       	 
                       
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DeclContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def declaravar(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(IsiLangParser.DeclaravarContext)
            else:
                return self.getTypedRuleContext(IsiLangParser.DeclaravarContext,i)


        def getRuleIndex(self):
            return IsiLangParser.RULE_decl

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDecl" ):
                listener.enterDecl(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDecl" ):
                listener.exitDecl(self)




    def decl(self):

        localctx = IsiLangParser.DeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_decl)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 37 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 36
                self.declaravar()
                self.state = 39 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==IsiLangParser.T__2 or _la==IsiLangParser.T__3):
                    break

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DeclaravarContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def tipo(self):
            return self.getTypedRuleContext(IsiLangParser.TipoContext,0)


        def ID(self, i:int=None):
            if i is None:
                return self.getTokens(IsiLangParser.ID)
            else:
                return self.getToken(IsiLangParser.ID, i)

        def SC(self):
            return self.getToken(IsiLangParser.SC, 0)

        def VIR(self, i:int=None):
            if i is None:
                return self.getTokens(IsiLangParser.VIR)
            else:
                return self.getToken(IsiLangParser.VIR, i)

        def getRuleIndex(self):
            return IsiLangParser.RULE_declaravar

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDeclaravar" ):
                listener.enterDeclaravar(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDeclaravar" ):
                listener.exitDeclaravar(self)




    def declaravar(self):

        localctx = IsiLangParser.DeclaravarContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_declaravar)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 41
            self.tipo()
            self.state = 42
            self.match(IsiLangParser.ID)


            parseHelper.varName = self._input.LT(-1).text;
            parseHelper.varValue = None;
            symbol = IsiVariable(parseHelper.varName, parseHelper.tipo, parseHelper.varValue);
            if not parseHelper.symbolTable.exists(parseHelper.varName):
                parseHelper.symbolTable.add(symbol);	
            else:
                raise IsiSemanticException("Symbol "+parseHelper.varName+" already declared")
                                
            self.state = 49
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==IsiLangParser.VIR:
                self.state = 44
                self.match(IsiLangParser.VIR)
                self.state = 45
                self.match(IsiLangParser.ID)

                parseHelper.varName = self._input.LT(-1).text;
                parseHelper.varValue = None;
                symbol = IsiVariable(parseHelper.varName, parseHelper.tipo, parseHelper.varValue);
                if not parseHelper.symbolTable.exists(parseHelper.varName):
                    parseHelper.symbolTable.add(symbol);	
                else:
                    raise IsiSemanticException("Symbol "+parseHelper.varName+" already declared");
                                    
                self.state = 51
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 52
            self.match(IsiLangParser.SC)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class TipoContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return IsiLangParser.RULE_tipo

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTipo" ):
                listener.enterTipo(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTipo" ):
                listener.exitTipo(self)




    def tipo(self):

        localctx = IsiLangParser.TipoContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_tipo)
        try:
            self.state = 58
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [IsiLangParser.T__2]:
                self.enterOuterAlt(localctx, 1)
                self.state = 54
                self.match(IsiLangParser.T__2)
                parseHelper.tipo = IsiEnumType.NUMBER;  
                pass
            elif token in [IsiLangParser.T__3]:
                self.enterOuterAlt(localctx, 2)
                self.state = 56
                self.match(IsiLangParser.T__3)
                parseHelper.tipo = IsiEnumType.TEXT;  
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class BlocoContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def cmd(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(IsiLangParser.CmdContext)
            else:
                return self.getTypedRuleContext(IsiLangParser.CmdContext,i)


        def getRuleIndex(self):
            return IsiLangParser.RULE_bloco

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBloco" ):
                listener.enterBloco(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBloco" ):
                listener.exitBloco(self)




    def bloco(self):

        localctx = IsiLangParser.BlocoContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_bloco)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
             

            curThread = [] 
            parseHelper.stack.append(curThread);  

                      
            self.state = 62 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 61
                self.cmd()
                self.state = 64 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << IsiLangParser.T__4) | (1 << IsiLangParser.T__5) | (1 << IsiLangParser.T__6) | (1 << IsiLangParser.T__8) | (1 << IsiLangParser.T__12) | (1 << IsiLangParser.ID))) != 0)):
                    break

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class CmdContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def cmdleitura(self):
            return self.getTypedRuleContext(IsiLangParser.CmdleituraContext,0)


        def cmdescrita(self):
            return self.getTypedRuleContext(IsiLangParser.CmdescritaContext,0)


        def cmdattrib(self):
            return self.getTypedRuleContext(IsiLangParser.CmdattribContext,0)


        def cmdselecao(self):
            return self.getTypedRuleContext(IsiLangParser.CmdselecaoContext,0)


        def cmdrepeticao(self):
            return self.getTypedRuleContext(IsiLangParser.CmdrepeticaoContext,0)


        def cmdcaso(self):
            return self.getTypedRuleContext(IsiLangParser.CmdcasoContext,0)


        def getRuleIndex(self):
            return IsiLangParser.RULE_cmd

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCmd" ):
                listener.enterCmd(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCmd" ):
                listener.exitCmd(self)




    def cmd(self):

        localctx = IsiLangParser.CmdContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_cmd)
        try:
            self.state = 72
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [IsiLangParser.T__4]:
                self.enterOuterAlt(localctx, 1)
                self.state = 66
                self.cmdleitura()
                pass
            elif token in [IsiLangParser.T__5]:
                self.enterOuterAlt(localctx, 2)
                self.state = 67
                self.cmdescrita()
                pass
            elif token in [IsiLangParser.ID]:
                self.enterOuterAlt(localctx, 3)
                self.state = 68
                self.cmdattrib()
                pass
            elif token in [IsiLangParser.T__6]:
                self.enterOuterAlt(localctx, 4)
                self.state = 69
                self.cmdselecao()
                pass
            elif token in [IsiLangParser.T__12]:
                self.enterOuterAlt(localctx, 5)
                self.state = 70
                self.cmdrepeticao()
                pass
            elif token in [IsiLangParser.T__8]:
                self.enterOuterAlt(localctx, 6)
                self.state = 71
                self.cmdcaso()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class CmdleituraContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def AP(self):
            return self.getToken(IsiLangParser.AP, 0)

        def ID(self):
            return self.getToken(IsiLangParser.ID, 0)

        def FP(self):
            return self.getToken(IsiLangParser.FP, 0)

        def SC(self):
            return self.getToken(IsiLangParser.SC, 0)

        def getRuleIndex(self):
            return IsiLangParser.RULE_cmdleitura

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCmdleitura" ):
                listener.enterCmdleitura(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCmdleitura" ):
                listener.exitCmdleitura(self)




    def cmdleitura(self):

        localctx = IsiLangParser.CmdleituraContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_cmdleitura)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 74
            self.match(IsiLangParser.T__4)
            self.state = 75
            self.match(IsiLangParser.AP)
            self.state = 76
            self.match(IsiLangParser.ID)
             

            parseHelper.verificaID(self._input.LT(-1).text)
            parseHelper.readID = self._input.LT(-1).text

                                    
            self.state = 78
            self.match(IsiLangParser.FP)
            self.state = 79
            self.match(IsiLangParser.SC)


            var = parseHelper.symbolTable.get(parseHelper.readID)
            cmd = CommandLeitura(parseHelper.readID, var)
            parseHelper.stack[-1].append(cmd)

                          
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class CmdescritaContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def AP(self):
            return self.getToken(IsiLangParser.AP, 0)

        def FP(self):
            return self.getToken(IsiLangParser.FP, 0)

        def SC(self):
            return self.getToken(IsiLangParser.SC, 0)

        def ID(self):
            return self.getToken(IsiLangParser.ID, 0)

        def TEXT(self):
            return self.getToken(IsiLangParser.TEXT, 0)

        def getRuleIndex(self):
            return IsiLangParser.RULE_cmdescrita

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCmdescrita" ):
                listener.enterCmdescrita(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCmdescrita" ):
                listener.exitCmdescrita(self)




    def cmdescrita(self):

        localctx = IsiLangParser.CmdescritaContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_cmdescrita)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 82
            self.match(IsiLangParser.T__5)
            self.state = 83
            self.match(IsiLangParser.AP)
            self.state = 88
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [IsiLangParser.ID]:
                self.state = 84
                self.match(IsiLangParser.ID)
                 
                parseHelper.verificaID(self._input.LT(-1).text)
                parseHelper.writeID = self._input.LT(-1).text
                parseHelper.setUsedVariable(parseHelper.writeID)
                                     
                pass
            elif token in [IsiLangParser.TEXT]:
                self.state = 86
                self.match(IsiLangParser.TEXT)
                parseHelper.writeID = self._input.LT(-1).text
                pass
            else:
                raise NoViableAltException(self)

            self.state = 90
            self.match(IsiLangParser.FP)
            self.state = 91
            self.match(IsiLangParser.SC)

            cmd = CommandEscrita(parseHelper.writeID)
            parseHelper.stack[-1].append(cmd)
                           
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class CmdattribContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(IsiLangParser.ID, 0)

        def ATTR(self):
            return self.getToken(IsiLangParser.ATTR, 0)

        def expr(self):
            return self.getTypedRuleContext(IsiLangParser.ExprContext,0)


        def SC(self):
            return self.getToken(IsiLangParser.SC, 0)

        def getRuleIndex(self):
            return IsiLangParser.RULE_cmdattrib

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCmdattrib" ):
                listener.enterCmdattrib(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCmdattrib" ):
                listener.exitCmdattrib(self)




    def cmdattrib(self):

        localctx = IsiLangParser.CmdattribContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_cmdattrib)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 94
            self.match(IsiLangParser.ID)
             
            parseHelper.verificaID(self._input.LT(-1).text)
            parseHelper.exprID = self._input.LT(-1).text
            parseHelper.setUsedVariable(parseHelper.exprID)
                               
            self.state = 96
            self.match(IsiLangParser.ATTR)
            parseHelper.exprContent = "" 
            self.state = 98
            self.expr()
            self.state = 99
            self.match(IsiLangParser.SC)

            cmd = CommandAtribuicao(parseHelper.exprID, parseHelper.exprContent)
            parseHelper.stack[-1].append(cmd)
                           
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class CmdselecaoContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def AP(self):
            return self.getToken(IsiLangParser.AP, 0)

        def ID(self, i:int=None):
            if i is None:
                return self.getTokens(IsiLangParser.ID)
            else:
                return self.getToken(IsiLangParser.ID, i)

        def OPREL(self):
            return self.getToken(IsiLangParser.OPREL, 0)

        def FP(self):
            return self.getToken(IsiLangParser.FP, 0)

        def ACH(self, i:int=None):
            if i is None:
                return self.getTokens(IsiLangParser.ACH)
            else:
                return self.getToken(IsiLangParser.ACH, i)

        def FCH(self, i:int=None):
            if i is None:
                return self.getTokens(IsiLangParser.FCH)
            else:
                return self.getToken(IsiLangParser.FCH, i)

        def NUMBER(self):
            return self.getToken(IsiLangParser.NUMBER, 0)

        def cmd(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(IsiLangParser.CmdContext)
            else:
                return self.getTypedRuleContext(IsiLangParser.CmdContext,i)


        def getRuleIndex(self):
            return IsiLangParser.RULE_cmdselecao

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCmdselecao" ):
                listener.enterCmdselecao(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCmdselecao" ):
                listener.exitCmdselecao(self)




    def cmdselecao(self):

        localctx = IsiLangParser.CmdselecaoContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_cmdselecao)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 102
            self.match(IsiLangParser.T__6)
            self.state = 103
            self.match(IsiLangParser.AP)
            self.state = 104
            self.match(IsiLangParser.ID)

            parseHelper.exprDecision = self._input.LT(-1).text 
            parseHelper.setUsedVariable(self._input.LT(-1).text)

            self.state = 106
            self.match(IsiLangParser.OPREL)
            parseHelper.exprDecision += self._input.LT(-1).text 
            self.state = 111
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [IsiLangParser.ID]:
                self.state = 108
                self.match(IsiLangParser.ID)
                parseHelper.setUsedVariable(self._input.LT(-1).text)
                pass
            elif token in [IsiLangParser.NUMBER]:
                self.state = 110
                self.match(IsiLangParser.NUMBER)
                pass
            else:
                raise NoViableAltException(self)

            parseHelper.exprDecision += self._input.LT(-1).text 
            self.state = 114
            self.match(IsiLangParser.FP)
            self.state = 115
            self.match(IsiLangParser.ACH)
             
            curThread = []
            parseHelper.stack.append(curThread)
                                
            self.state = 118 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 117
                self.cmd()
                self.state = 120 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << IsiLangParser.T__4) | (1 << IsiLangParser.T__5) | (1 << IsiLangParser.T__6) | (1 << IsiLangParser.T__8) | (1 << IsiLangParser.T__12) | (1 << IsiLangParser.ID))) != 0)):
                    break

            self.state = 122
            self.match(IsiLangParser.FCH)

            parseHelper.listaTrue = parseHelper.stack.pop()
                                
            self.state = 135
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==IsiLangParser.T__7:
                self.state = 124
                self.match(IsiLangParser.T__7)
                self.state = 125
                self.match(IsiLangParser.ACH)

                curThread = []
                parseHelper.stack.append(curThread)
                                   	 

                self.state = 128 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while True:
                    self.state = 127
                    self.cmd()
                    self.state = 130 
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << IsiLangParser.T__4) | (1 << IsiLangParser.T__5) | (1 << IsiLangParser.T__6) | (1 << IsiLangParser.T__8) | (1 << IsiLangParser.T__12) | (1 << IsiLangParser.ID))) != 0)):
                        break

                self.state = 132
                self.match(IsiLangParser.FCH)

                parseHelper.listaFalse = parseHelper.stack.pop()
                                   	



            cmd = CommandDecisao(parseHelper.exprDecision, parseHelper.listaTrue, parseHelper.listaFalse)
            parseHelper.stack[-1].append(cmd)
                               
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class CmdcasoContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def AP(self):
            return self.getToken(IsiLangParser.AP, 0)

        def FP(self):
            return self.getToken(IsiLangParser.FP, 0)

        def ACH(self):
            return self.getToken(IsiLangParser.ACH, 0)

        def FCH(self):
            return self.getToken(IsiLangParser.FCH, 0)

        def ID(self, i:int=None):
            if i is None:
                return self.getTokens(IsiLangParser.ID)
            else:
                return self.getToken(IsiLangParser.ID, i)

        def NUMBER(self, i:int=None):
            if i is None:
                return self.getTokens(IsiLangParser.NUMBER)
            else:
                return self.getToken(IsiLangParser.NUMBER, i)

        def TEXT(self, i:int=None):
            if i is None:
                return self.getTokens(IsiLangParser.TEXT)
            else:
                return self.getToken(IsiLangParser.TEXT, i)

        def DP(self, i:int=None):
            if i is None:
                return self.getTokens(IsiLangParser.DP)
            else:
                return self.getToken(IsiLangParser.DP, i)

        def cmd(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(IsiLangParser.CmdContext)
            else:
                return self.getTypedRuleContext(IsiLangParser.CmdContext,i)


        def SC(self, i:int=None):
            if i is None:
                return self.getTokens(IsiLangParser.SC)
            else:
                return self.getToken(IsiLangParser.SC, i)

        def getRuleIndex(self):
            return IsiLangParser.RULE_cmdcaso

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCmdcaso" ):
                listener.enterCmdcaso(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCmdcaso" ):
                listener.exitCmdcaso(self)




    def cmdcaso(self):

        localctx = IsiLangParser.CmdcasoContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_cmdcaso)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 139
            self.match(IsiLangParser.T__8)
            self.state = 140
            self.match(IsiLangParser.AP)
            self.state = 145
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [IsiLangParser.ID]:
                self.state = 141
                self.match(IsiLangParser.ID)
                parseHelper.setUsedVariable(self._input.LT(-1).text)
                pass
            elif token in [IsiLangParser.NUMBER]:
                self.state = 143
                self.match(IsiLangParser.NUMBER)
                pass
            elif token in [IsiLangParser.TEXT]:
                self.state = 144
                self.match(IsiLangParser.TEXT)
                pass
            else:
                raise NoViableAltException(self)


            parseHelper.exprID = self._input.LT(-1).text 
                                  
            self.state = 148
            self.match(IsiLangParser.FP)
            self.state = 149
            self.match(IsiLangParser.ACH)
            self.state = 173 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 150
                self.match(IsiLangParser.T__9)
                self.state = 155
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [IsiLangParser.ID]:
                    self.state = 151
                    self.match(IsiLangParser.ID)
                    parseHelper.setUsedVariable(self._input.LT(-1).text)
                    pass
                elif token in [IsiLangParser.NUMBER]:
                    self.state = 153
                    self.match(IsiLangParser.NUMBER)
                    pass
                elif token in [IsiLangParser.TEXT]:
                    self.state = 154
                    self.match(IsiLangParser.TEXT)
                    pass
                else:
                    raise NoViableAltException(self)


                parseHelper.exprDecision = self._input.LT(-1).text 
                                    
                self.state = 158
                self.match(IsiLangParser.DP)
                 
                curThread = []
                parseHelper.stack.append(curThread)
                                    
                self.state = 161 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while True:
                    self.state = 160
                    self.cmd()
                    self.state = 163 
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << IsiLangParser.T__4) | (1 << IsiLangParser.T__5) | (1 << IsiLangParser.T__6) | (1 << IsiLangParser.T__8) | (1 << IsiLangParser.T__12) | (1 << IsiLangParser.ID))) != 0)):
                        break


                caseThread = parseHelper.stack.pop()
                varBreak = False
                                    
                self.state = 169
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==IsiLangParser.T__10:
                    self.state = 166
                    self.match(IsiLangParser.T__10)
                    varBreak = True
                    self.state = 168
                    self.match(IsiLangParser.SC)



                parseHelper.CasoDict[parseHelper.exprDecision] = (caseThread, varBreak)                  
                                    
                self.state = 175 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==IsiLangParser.T__9):
                    break

            self.state = 187
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==IsiLangParser.T__11:
                self.state = 177
                self.match(IsiLangParser.T__11)
                self.state = 178
                self.match(IsiLangParser.DP)
                 
                curThread = []
                parseHelper.stack.append(curThread)
                                    
                self.state = 181 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while True:
                    self.state = 180
                    self.cmd()
                    self.state = 183 
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << IsiLangParser.T__4) | (1 << IsiLangParser.T__5) | (1 << IsiLangParser.T__6) | (1 << IsiLangParser.T__8) | (1 << IsiLangParser.T__12) | (1 << IsiLangParser.ID))) != 0)):
                        break


                parseHelper.listaFalse = parseHelper.stack.pop()
                                      


            self.state = 189
            self.match(IsiLangParser.FCH)

            cmd = CommandCaso(parseHelper.exprID, parseHelper.CasoDict, parseHelper.listaFalse)
            parseHelper.stack[-1].append(cmd)
                                 
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class CmdrepeticaoContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def AP(self):
            return self.getToken(IsiLangParser.AP, 0)

        def ID(self, i:int=None):
            if i is None:
                return self.getTokens(IsiLangParser.ID)
            else:
                return self.getToken(IsiLangParser.ID, i)

        def OPREL(self):
            return self.getToken(IsiLangParser.OPREL, 0)

        def FP(self):
            return self.getToken(IsiLangParser.FP, 0)

        def ACH(self):
            return self.getToken(IsiLangParser.ACH, 0)

        def FCH(self):
            return self.getToken(IsiLangParser.FCH, 0)

        def NUMBER(self):
            return self.getToken(IsiLangParser.NUMBER, 0)

        def cmd(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(IsiLangParser.CmdContext)
            else:
                return self.getTypedRuleContext(IsiLangParser.CmdContext,i)


        def getRuleIndex(self):
            return IsiLangParser.RULE_cmdrepeticao

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCmdrepeticao" ):
                listener.enterCmdrepeticao(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCmdrepeticao" ):
                listener.exitCmdrepeticao(self)




    def cmdrepeticao(self):

        localctx = IsiLangParser.CmdrepeticaoContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_cmdrepeticao)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 192
            self.match(IsiLangParser.T__12)
            self.state = 193
            self.match(IsiLangParser.AP)
            self.state = 194
            self.match(IsiLangParser.ID)

            parseHelper.exprDecision = self._input.LT(-1).text
            parseHelper.setUsedVariable(self._input.LT(-1).text)
             
            self.state = 196
            self.match(IsiLangParser.OPREL)
            parseHelper.exprDecision += self._input.LT(-1).text 
            self.state = 201
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [IsiLangParser.ID]:
                self.state = 198
                self.match(IsiLangParser.ID)
                parseHelper.setUsedVariable(self._input.LT(-1).text)
                pass
            elif token in [IsiLangParser.NUMBER]:
                self.state = 200
                self.match(IsiLangParser.NUMBER)
                pass
            else:
                raise NoViableAltException(self)

            parseHelper.exprDecision += self._input.LT(-1).text 
            self.state = 204
            self.match(IsiLangParser.FP)
            self.state = 205
            self.match(IsiLangParser.ACH)
             
            curThread = []
            parseHelper.stack.append(curThread)
                                
            self.state = 208 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 207
                self.cmd()
                self.state = 210 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << IsiLangParser.T__4) | (1 << IsiLangParser.T__5) | (1 << IsiLangParser.T__6) | (1 << IsiLangParser.T__8) | (1 << IsiLangParser.T__12) | (1 << IsiLangParser.ID))) != 0)):
                    break

            self.state = 212
            self.match(IsiLangParser.FCH)

            parseHelper.listarepeticao = parseHelper.stack.pop()
            cmd = CommandRepeticao(parseHelper.exprDecision, parseHelper.listarepeticao)
            parseHelper.stack[-1].append(cmd)
                                
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def termo(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(IsiLangParser.TermoContext)
            else:
                return self.getTypedRuleContext(IsiLangParser.TermoContext,i)


        def exprL(self):
            return self.getTypedRuleContext(IsiLangParser.ExprLContext,0)


        def OP(self, i:int=None):
            if i is None:
                return self.getTokens(IsiLangParser.OP)
            else:
                return self.getToken(IsiLangParser.OP, i)

        def AP(self):
            return self.getToken(IsiLangParser.AP, 0)

        def expr(self):
            return self.getTypedRuleContext(IsiLangParser.ExprContext,0)


        def FP(self):
            return self.getToken(IsiLangParser.FP, 0)

        def getRuleIndex(self):
            return IsiLangParser.RULE_expr

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExpr" ):
                listener.enterExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExpr" ):
                listener.exitExpr(self)




    def expr(self):

        localctx = IsiLangParser.ExprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_expr)
        try:
            self.state = 233
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [IsiLangParser.ID, IsiLangParser.NUMBER, IsiLangParser.TEXT]:
                self.enterOuterAlt(localctx, 1)
                self.state = 215
                self.termo()
                self.state = 221
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,19,self._ctx)
                while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                    if _alt==1:
                        self.state = 216
                        self.match(IsiLangParser.OP)

                        parseHelper.isNumber(parseHelper.exprID)
                        parseHelper.exprContent += self._input.LT(-1).text

                        self.state = 218
                        self.termo() 
                    self.state = 223
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,19,self._ctx)

                self.state = 224
                self.exprL()
                pass
            elif token in [IsiLangParser.AP]:
                self.enterOuterAlt(localctx, 2)
                self.state = 226
                self.match(IsiLangParser.AP)
                parseHelper.exprContent += self._input.LT(-1).text
                self.state = 228
                self.expr()
                self.state = 229
                self.match(IsiLangParser.FP)
                parseHelper.exprContent += self._input.LT(-1).text
                self.state = 231
                self.exprL()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExprLContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def OP(self):
            return self.getToken(IsiLangParser.OP, 0)

        def expr(self):
            return self.getTypedRuleContext(IsiLangParser.ExprContext,0)


        def exprL(self):
            return self.getTypedRuleContext(IsiLangParser.ExprLContext,0)


        def getRuleIndex(self):
            return IsiLangParser.RULE_exprL

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExprL" ):
                listener.enterExprL(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExprL" ):
                listener.exitExprL(self)




    def exprL(self):

        localctx = IsiLangParser.ExprLContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_exprL)
        try:
            self.state = 241
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,21,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 235
                self.match(IsiLangParser.OP)
                parseHelper.exprContent += self._input.LT(-1).text
                self.state = 237
                self.expr()
                self.state = 238
                self.exprL()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)

                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class TermoContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(IsiLangParser.ID, 0)

        def NUMBER(self):
            return self.getToken(IsiLangParser.NUMBER, 0)

        def TEXT(self):
            return self.getToken(IsiLangParser.TEXT, 0)

        def getRuleIndex(self):
            return IsiLangParser.RULE_termo

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTermo" ):
                listener.enterTermo(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTermo" ):
                listener.exitTermo(self)




    def termo(self):

        localctx = IsiLangParser.TermoContext(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_termo)
        try:
            self.state = 249
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [IsiLangParser.ID]:
                self.enterOuterAlt(localctx, 1)
                self.state = 243
                self.match(IsiLangParser.ID)
                     
                parseHelper.verificaID(self._input.LT(-1).text)
                parseHelper.verificaTipo(parseHelper.exprID, self._input.LT(-1).text)
                parseHelper.exprContent += self._input.LT(-1).text
                parseHelper.setUsedVariable(self._input.LT(-1).text)
                                 
                pass
            elif token in [IsiLangParser.NUMBER]:
                self.enterOuterAlt(localctx, 2)
                self.state = 245
                self.match(IsiLangParser.NUMBER)

                parseHelper.isNumber(parseHelper.exprID)                
                parseHelper.exprContent += self._input.LT(-1).text
                              
                pass
            elif token in [IsiLangParser.TEXT]:
                self.enterOuterAlt(localctx, 3)
                self.state = 247
                self.match(IsiLangParser.TEXT)

                parseHelper.exprContent += self._input.LT(-1).text  
                              
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





