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
        4,1,27,230,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,13,7,13,
        1,0,1,0,1,0,1,0,1,0,1,0,1,1,4,1,36,8,1,11,1,12,1,37,1,2,1,2,1,2,
        1,2,1,2,1,2,5,2,46,8,2,10,2,12,2,49,9,2,1,2,1,2,1,3,1,3,1,3,1,3,
        3,3,57,8,3,1,4,1,4,4,4,61,8,4,11,4,12,4,62,1,5,1,5,1,5,1,5,1,5,1,
        5,3,5,71,8,5,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,7,1,7,1,7,1,7,1,7,
        3,7,86,8,7,1,7,1,7,1,7,1,7,1,8,1,8,1,8,1,8,1,8,1,8,1,8,1,8,1,9,1,
        9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,3,9,109,8,9,1,9,1,9,1,9,1,9,1,9,4,
        9,116,8,9,11,9,12,9,117,1,9,1,9,1,9,1,9,1,9,1,9,4,9,126,8,9,11,9,
        12,9,127,1,9,1,9,1,9,3,9,133,8,9,1,9,1,9,1,10,1,10,1,10,1,10,1,10,
        1,10,3,10,143,8,10,1,10,1,10,1,10,1,10,1,10,1,10,1,10,1,10,3,10,
        153,8,10,1,10,1,10,1,10,1,10,4,10,159,8,10,11,10,12,10,160,1,10,
        1,10,1,10,1,10,3,10,167,8,10,1,10,1,10,4,10,171,8,10,11,10,12,10,
        172,1,10,1,10,1,10,1,10,4,10,179,8,10,11,10,12,10,180,1,10,1,10,
        3,10,185,8,10,1,10,1,10,1,10,1,11,1,11,1,11,1,11,1,11,1,11,1,11,
        1,11,1,11,3,11,199,8,11,1,11,1,11,1,11,1,11,1,11,4,11,206,8,11,11,
        11,12,11,207,1,11,1,11,1,11,1,12,1,12,1,12,1,12,5,12,217,8,12,10,
        12,12,12,220,9,12,1,13,1,13,1,13,1,13,1,13,1,13,3,13,228,8,13,1,
        13,0,0,14,0,2,4,6,8,10,12,14,16,18,20,22,24,26,0,0,243,0,28,1,0,
        0,0,2,35,1,0,0,0,4,39,1,0,0,0,6,56,1,0,0,0,8,58,1,0,0,0,10,70,1,
        0,0,0,12,72,1,0,0,0,14,80,1,0,0,0,16,91,1,0,0,0,18,99,1,0,0,0,20,
        136,1,0,0,0,22,189,1,0,0,0,24,212,1,0,0,0,26,227,1,0,0,0,28,29,5,
        1,0,0,29,30,3,2,1,0,30,31,3,8,4,0,31,32,5,2,0,0,32,33,6,0,-1,0,33,
        1,1,0,0,0,34,36,3,4,2,0,35,34,1,0,0,0,36,37,1,0,0,0,37,35,1,0,0,
        0,37,38,1,0,0,0,38,3,1,0,0,0,39,40,3,6,3,0,40,41,5,23,0,0,41,47,
        6,2,-1,0,42,43,5,19,0,0,43,44,5,23,0,0,44,46,6,2,-1,0,45,42,1,0,
        0,0,46,49,1,0,0,0,47,45,1,0,0,0,47,48,1,0,0,0,48,50,1,0,0,0,49,47,
        1,0,0,0,50,51,5,16,0,0,51,5,1,0,0,0,52,53,5,3,0,0,53,57,6,3,-1,0,
        54,55,5,4,0,0,55,57,6,3,-1,0,56,52,1,0,0,0,56,54,1,0,0,0,57,7,1,
        0,0,0,58,60,6,4,-1,0,59,61,3,10,5,0,60,59,1,0,0,0,61,62,1,0,0,0,
        62,60,1,0,0,0,62,63,1,0,0,0,63,9,1,0,0,0,64,71,3,12,6,0,65,71,3,
        14,7,0,66,71,3,16,8,0,67,71,3,18,9,0,68,71,3,22,11,0,69,71,3,20,
        10,0,70,64,1,0,0,0,70,65,1,0,0,0,70,66,1,0,0,0,70,67,1,0,0,0,70,
        68,1,0,0,0,70,69,1,0,0,0,71,11,1,0,0,0,72,73,5,5,0,0,73,74,5,14,
        0,0,74,75,5,23,0,0,75,76,6,6,-1,0,76,77,5,15,0,0,77,78,5,16,0,0,
        78,79,6,6,-1,0,79,13,1,0,0,0,80,81,5,6,0,0,81,85,5,14,0,0,82,83,
        5,23,0,0,83,86,6,7,-1,0,84,86,5,25,0,0,85,82,1,0,0,0,85,84,1,0,0,
        0,86,87,1,0,0,0,87,88,5,15,0,0,88,89,5,16,0,0,89,90,6,7,-1,0,90,
        15,1,0,0,0,91,92,5,23,0,0,92,93,6,8,-1,0,93,94,5,18,0,0,94,95,6,
        8,-1,0,95,96,3,24,12,0,96,97,5,16,0,0,97,98,6,8,-1,0,98,17,1,0,0,
        0,99,100,5,7,0,0,100,101,5,14,0,0,101,102,5,23,0,0,102,103,6,9,-1,
        0,103,104,5,22,0,0,104,108,6,9,-1,0,105,106,5,23,0,0,106,109,6,9,
        -1,0,107,109,5,24,0,0,108,105,1,0,0,0,108,107,1,0,0,0,109,110,1,
        0,0,0,110,111,6,9,-1,0,111,112,5,15,0,0,112,113,5,20,0,0,113,115,
        6,9,-1,0,114,116,3,10,5,0,115,114,1,0,0,0,116,117,1,0,0,0,117,115,
        1,0,0,0,117,118,1,0,0,0,118,119,1,0,0,0,119,120,5,21,0,0,120,132,
        6,9,-1,0,121,122,5,8,0,0,122,123,5,20,0,0,123,125,6,9,-1,0,124,126,
        3,10,5,0,125,124,1,0,0,0,126,127,1,0,0,0,127,125,1,0,0,0,127,128,
        1,0,0,0,128,129,1,0,0,0,129,130,5,21,0,0,130,131,6,9,-1,0,131,133,
        1,0,0,0,132,121,1,0,0,0,132,133,1,0,0,0,133,134,1,0,0,0,134,135,
        6,9,-1,0,135,19,1,0,0,0,136,137,5,9,0,0,137,142,5,14,0,0,138,139,
        5,23,0,0,139,143,6,10,-1,0,140,143,5,24,0,0,141,143,5,25,0,0,142,
        138,1,0,0,0,142,140,1,0,0,0,142,141,1,0,0,0,143,144,1,0,0,0,144,
        145,6,10,-1,0,145,146,5,15,0,0,146,170,5,20,0,0,147,152,5,10,0,0,
        148,149,5,23,0,0,149,153,6,10,-1,0,150,153,5,24,0,0,151,153,5,25,
        0,0,152,148,1,0,0,0,152,150,1,0,0,0,152,151,1,0,0,0,153,154,1,0,
        0,0,154,155,6,10,-1,0,155,156,5,27,0,0,156,158,6,10,-1,0,157,159,
        3,10,5,0,158,157,1,0,0,0,159,160,1,0,0,0,160,158,1,0,0,0,160,161,
        1,0,0,0,161,162,1,0,0,0,162,166,6,10,-1,0,163,164,5,11,0,0,164,165,
        6,10,-1,0,165,167,5,16,0,0,166,163,1,0,0,0,166,167,1,0,0,0,167,168,
        1,0,0,0,168,169,6,10,-1,0,169,171,1,0,0,0,170,147,1,0,0,0,171,172,
        1,0,0,0,172,170,1,0,0,0,172,173,1,0,0,0,173,184,1,0,0,0,174,175,
        5,12,0,0,175,176,5,27,0,0,176,178,6,10,-1,0,177,179,3,10,5,0,178,
        177,1,0,0,0,179,180,1,0,0,0,180,178,1,0,0,0,180,181,1,0,0,0,181,
        182,1,0,0,0,182,183,6,10,-1,0,183,185,1,0,0,0,184,174,1,0,0,0,184,
        185,1,0,0,0,185,186,1,0,0,0,186,187,5,21,0,0,187,188,6,10,-1,0,188,
        21,1,0,0,0,189,190,5,13,0,0,190,191,5,14,0,0,191,192,5,23,0,0,192,
        193,6,11,-1,0,193,194,5,22,0,0,194,198,6,11,-1,0,195,196,5,23,0,
        0,196,199,6,11,-1,0,197,199,5,24,0,0,198,195,1,0,0,0,198,197,1,0,
        0,0,199,200,1,0,0,0,200,201,6,11,-1,0,201,202,5,15,0,0,202,203,5,
        20,0,0,203,205,6,11,-1,0,204,206,3,10,5,0,205,204,1,0,0,0,206,207,
        1,0,0,0,207,205,1,0,0,0,207,208,1,0,0,0,208,209,1,0,0,0,209,210,
        5,21,0,0,210,211,6,11,-1,0,211,23,1,0,0,0,212,218,3,26,13,0,213,
        214,5,17,0,0,214,215,6,12,-1,0,215,217,3,26,13,0,216,213,1,0,0,0,
        217,220,1,0,0,0,218,216,1,0,0,0,218,219,1,0,0,0,219,25,1,0,0,0,220,
        218,1,0,0,0,221,222,5,23,0,0,222,228,6,13,-1,0,223,224,5,24,0,0,
        224,228,6,13,-1,0,225,226,5,25,0,0,226,228,6,13,-1,0,227,221,1,0,
        0,0,227,223,1,0,0,0,227,225,1,0,0,0,228,27,1,0,0,0,21,37,47,56,62,
        70,85,108,117,127,132,142,152,160,166,172,180,184,198,207,218,227
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
    RULE_termo = 13

    ruleNames =  [ "prog", "decl", "declaravar", "tipo", "bloco", "cmd", 
                   "cmdleitura", "cmdescrita", "cmdattrib", "cmdselecao", 
                   "cmdcaso", "cmdrepeticao", "expr", "termo" ]

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
            self.state = 28
            self.match(IsiLangParser.T__0)
            self.state = 29
            self.decl()
            self.state = 30
            self.bloco()
            self.state = 31
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
            self.state = 35 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 34
                self.declaravar()
                self.state = 37 
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
            self.state = 39
            self.tipo()
            self.state = 40
            self.match(IsiLangParser.ID)


            parseHelper.varName = self._input.LT(-1).text;
            parseHelper.varValue = None;
            symbol = IsiVariable(parseHelper.varName, parseHelper.tipo, parseHelper.varValue);
            if not parseHelper.symbolTable.exists(parseHelper.varName):
                parseHelper.symbolTable.add(symbol);	
            else:
                raise IsiSemanticException("Symbol "+parseHelper.varName+" already declared")
                                
            self.state = 47
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==IsiLangParser.VIR:
                self.state = 42
                self.match(IsiLangParser.VIR)
                self.state = 43
                self.match(IsiLangParser.ID)

                parseHelper.varName = self._input.LT(-1).text;
                parseHelper.varValue = None;
                symbol = IsiVariable(parseHelper.varName, parseHelper.tipo, parseHelper.varValue);
                if not parseHelper.symbolTable.exists(parseHelper.varName):
                    parseHelper.symbolTable.add(symbol);	
                else:
                    raise IsiSemanticException("Symbol "+parseHelper.varName+" already declared");
                                    
                self.state = 49
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 50
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
            self.state = 56
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [IsiLangParser.T__2]:
                self.enterOuterAlt(localctx, 1)
                self.state = 52
                self.match(IsiLangParser.T__2)
                parseHelper.tipo = IsiEnumType.NUMBER;  
                pass
            elif token in [IsiLangParser.T__3]:
                self.enterOuterAlt(localctx, 2)
                self.state = 54
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

                      
            self.state = 60 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 59
                self.cmd()
                self.state = 62 
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
            self.state = 70
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [IsiLangParser.T__4]:
                self.enterOuterAlt(localctx, 1)
                self.state = 64
                self.cmdleitura()
                pass
            elif token in [IsiLangParser.T__5]:
                self.enterOuterAlt(localctx, 2)
                self.state = 65
                self.cmdescrita()
                pass
            elif token in [IsiLangParser.ID]:
                self.enterOuterAlt(localctx, 3)
                self.state = 66
                self.cmdattrib()
                pass
            elif token in [IsiLangParser.T__6]:
                self.enterOuterAlt(localctx, 4)
                self.state = 67
                self.cmdselecao()
                pass
            elif token in [IsiLangParser.T__12]:
                self.enterOuterAlt(localctx, 5)
                self.state = 68
                self.cmdrepeticao()
                pass
            elif token in [IsiLangParser.T__8]:
                self.enterOuterAlt(localctx, 6)
                self.state = 69
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
            self.state = 72
            self.match(IsiLangParser.T__4)
            self.state = 73
            self.match(IsiLangParser.AP)
            self.state = 74
            self.match(IsiLangParser.ID)
             

            parseHelper.verificaID(self._input.LT(-1).text)
            parseHelper.readID = self._input.LT(-1).text

                                    
            self.state = 76
            self.match(IsiLangParser.FP)
            self.state = 77
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
            self.state = 80
            self.match(IsiLangParser.T__5)
            self.state = 81
            self.match(IsiLangParser.AP)
            self.state = 85
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [IsiLangParser.ID]:
                self.state = 82
                self.match(IsiLangParser.ID)
                 
                parseHelper.verificaID(self._input.LT(-1).text)
                parseHelper.writeID = self._input.LT(-1).text
                                     
                pass
            elif token in [IsiLangParser.TEXT]:
                self.state = 84
                self.match(IsiLangParser.TEXT)
                pass
            else:
                raise NoViableAltException(self)

            self.state = 87
            self.match(IsiLangParser.FP)
            self.state = 88
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
            self.state = 91
            self.match(IsiLangParser.ID)
             
            parseHelper.verificaID(self._input.LT(-1).text)
            parseHelper.exprID = self._input.LT(-1).text
                               
            self.state = 93
            self.match(IsiLangParser.ATTR)
            parseHelper.exprContent = "" 
            self.state = 95
            self.expr()
            self.state = 96
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
            self.state = 99
            self.match(IsiLangParser.T__6)
            self.state = 100
            self.match(IsiLangParser.AP)
            self.state = 101
            self.match(IsiLangParser.ID)

            parseHelper.exprDecision = self._input.LT(-1).text 
            parseHelper.setUsedVariable(self._input.LT(-1).text)

            self.state = 103
            self.match(IsiLangParser.OPREL)
            parseHelper.exprDecision += self._input.LT(-1).text 
            self.state = 108
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [IsiLangParser.ID]:
                self.state = 105
                self.match(IsiLangParser.ID)
                parseHelper.setUsedVariable(self._input.LT(-1).text)
                pass
            elif token in [IsiLangParser.NUMBER]:
                self.state = 107
                self.match(IsiLangParser.NUMBER)
                pass
            else:
                raise NoViableAltException(self)

            parseHelper.exprDecision += self._input.LT(-1).text 
            self.state = 111
            self.match(IsiLangParser.FP)
            self.state = 112
            self.match(IsiLangParser.ACH)
             
            curThread = []
            parseHelper.stack.append(curThread)
                                
            self.state = 115 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 114
                self.cmd()
                self.state = 117 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << IsiLangParser.T__4) | (1 << IsiLangParser.T__5) | (1 << IsiLangParser.T__6) | (1 << IsiLangParser.T__8) | (1 << IsiLangParser.T__12) | (1 << IsiLangParser.ID))) != 0)):
                    break

            self.state = 119
            self.match(IsiLangParser.FCH)

            parseHelper.listaTrue = parseHelper.stack.pop()
                                
            self.state = 132
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==IsiLangParser.T__7:
                self.state = 121
                self.match(IsiLangParser.T__7)
                self.state = 122
                self.match(IsiLangParser.ACH)

                curThread = []
                parseHelper.stack.append(curThread)
                                   	 

                self.state = 125 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while True:
                    self.state = 124
                    self.cmd()
                    self.state = 127 
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << IsiLangParser.T__4) | (1 << IsiLangParser.T__5) | (1 << IsiLangParser.T__6) | (1 << IsiLangParser.T__8) | (1 << IsiLangParser.T__12) | (1 << IsiLangParser.ID))) != 0)):
                        break

                self.state = 129
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
            self.state = 136
            self.match(IsiLangParser.T__8)
            self.state = 137
            self.match(IsiLangParser.AP)
            self.state = 142
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [IsiLangParser.ID]:
                self.state = 138
                self.match(IsiLangParser.ID)
                parseHelper.setUsedVariable(self._input.LT(-1).text)
                pass
            elif token in [IsiLangParser.NUMBER]:
                self.state = 140
                self.match(IsiLangParser.NUMBER)
                pass
            elif token in [IsiLangParser.TEXT]:
                self.state = 141
                self.match(IsiLangParser.TEXT)
                pass
            else:
                raise NoViableAltException(self)


            parseHelper.exprID = self._input.LT(-1).text 
                                  
            self.state = 145
            self.match(IsiLangParser.FP)
            self.state = 146
            self.match(IsiLangParser.ACH)
            self.state = 170 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 147
                self.match(IsiLangParser.T__9)
                self.state = 152
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [IsiLangParser.ID]:
                    self.state = 148
                    self.match(IsiLangParser.ID)
                    parseHelper.setUsedVariable(self._input.LT(-1).text)
                    pass
                elif token in [IsiLangParser.NUMBER]:
                    self.state = 150
                    self.match(IsiLangParser.NUMBER)
                    pass
                elif token in [IsiLangParser.TEXT]:
                    self.state = 151
                    self.match(IsiLangParser.TEXT)
                    pass
                else:
                    raise NoViableAltException(self)


                parseHelper.exprDecision = self._input.LT(-1).text 
                                    
                self.state = 155
                self.match(IsiLangParser.DP)
                 
                curThread = []
                parseHelper.stack.append(curThread)
                                    
                self.state = 158 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while True:
                    self.state = 157
                    self.cmd()
                    self.state = 160 
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << IsiLangParser.T__4) | (1 << IsiLangParser.T__5) | (1 << IsiLangParser.T__6) | (1 << IsiLangParser.T__8) | (1 << IsiLangParser.T__12) | (1 << IsiLangParser.ID))) != 0)):
                        break


                caseThread = parseHelper.stack.pop()
                varBreak = False
                                    
                self.state = 166
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==IsiLangParser.T__10:
                    self.state = 163
                    self.match(IsiLangParser.T__10)
                    varBreak = True
                    self.state = 165
                    self.match(IsiLangParser.SC)



                parseHelper.CasoDict[parseHelper.exprDecision] = (caseThread, varBreak)                  
                                    
                self.state = 172 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==IsiLangParser.T__9):
                    break

            self.state = 184
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==IsiLangParser.T__11:
                self.state = 174
                self.match(IsiLangParser.T__11)
                self.state = 175
                self.match(IsiLangParser.DP)
                 
                curThread = []
                parseHelper.stack.append(curThread)
                                    
                self.state = 178 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while True:
                    self.state = 177
                    self.cmd()
                    self.state = 180 
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << IsiLangParser.T__4) | (1 << IsiLangParser.T__5) | (1 << IsiLangParser.T__6) | (1 << IsiLangParser.T__8) | (1 << IsiLangParser.T__12) | (1 << IsiLangParser.ID))) != 0)):
                        break


                parseHelper.listaFalse = parseHelper.stack.pop()
                                      


            self.state = 186
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
            self.state = 189
            self.match(IsiLangParser.T__12)
            self.state = 190
            self.match(IsiLangParser.AP)
            self.state = 191
            self.match(IsiLangParser.ID)

            parseHelper.exprDecision = self._input.LT(-1).text
            parseHelper.setUsedVariable(self._input.LT(-1).text)
             
            self.state = 193
            self.match(IsiLangParser.OPREL)
            parseHelper.exprDecision += self._input.LT(-1).text 
            self.state = 198
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [IsiLangParser.ID]:
                self.state = 195
                self.match(IsiLangParser.ID)
                parseHelper.setUsedVariable(self._input.LT(-1).text)
                pass
            elif token in [IsiLangParser.NUMBER]:
                self.state = 197
                self.match(IsiLangParser.NUMBER)
                pass
            else:
                raise NoViableAltException(self)

            parseHelper.exprDecision += self._input.LT(-1).text 
            self.state = 201
            self.match(IsiLangParser.FP)
            self.state = 202
            self.match(IsiLangParser.ACH)
             
            curThread = []
            parseHelper.stack.append(curThread)
                                
            self.state = 205 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 204
                self.cmd()
                self.state = 207 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << IsiLangParser.T__4) | (1 << IsiLangParser.T__5) | (1 << IsiLangParser.T__6) | (1 << IsiLangParser.T__8) | (1 << IsiLangParser.T__12) | (1 << IsiLangParser.ID))) != 0)):
                    break

            self.state = 209
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


        def OP(self, i:int=None):
            if i is None:
                return self.getTokens(IsiLangParser.OP)
            else:
                return self.getToken(IsiLangParser.OP, i)

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
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 212
            self.termo()
            self.state = 218
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==IsiLangParser.OP:
                self.state = 213
                self.match(IsiLangParser.OP)

                parseHelper.isNumber(parseHelper.exprID)
                parseHelper.exprContent += self._input.LT(-1).text

                self.state = 215
                self.termo()
                self.state = 220
                self._errHandler.sync(self)
                _la = self._input.LA(1)

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
        self.enterRule(localctx, 26, self.RULE_termo)
        try:
            self.state = 227
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [IsiLangParser.ID]:
                self.enterOuterAlt(localctx, 1)
                self.state = 221
                self.match(IsiLangParser.ID)
                     
                parseHelper.verificaID(self._input.LT(-1).text)
                parseHelper.verificaTipo(parseHelper.exprID, self._input.LT(-1).text)
                parseHelper.exprContent += self._input.LT(-1).text
                parseHelper.setUsedVariable(self._input.LT(-1).text)
                                 
                pass
            elif token in [IsiLangParser.NUMBER]:
                self.enterOuterAlt(localctx, 2)
                self.state = 223
                self.match(IsiLangParser.NUMBER)

                parseHelper.isNumber(parseHelper.exprID)                
                parseHelper.exprContent += self._input.LT(-1).text
                              
                pass
            elif token in [IsiLangParser.TEXT]:
                self.enterOuterAlt(localctx, 3)
                self.state = 225
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





