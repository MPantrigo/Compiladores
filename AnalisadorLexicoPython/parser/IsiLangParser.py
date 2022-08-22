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


parseHelper = IsiParserHelper()



def serializedATN():
    return [
        4,1,21,169,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,1,0,1,0,
        1,0,1,0,1,0,1,0,1,1,4,1,34,8,1,11,1,12,1,35,1,2,1,2,1,2,1,2,1,2,
        1,2,5,2,44,8,2,10,2,12,2,47,9,2,1,2,1,2,1,3,1,3,1,3,1,3,3,3,55,8,
        3,1,4,1,4,4,4,59,8,4,11,4,12,4,60,1,5,1,5,1,5,1,5,1,5,3,5,68,8,5,
        1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,7,1,7,1,7,1,7,1,7,1,7,1,7,1,7,
        1,8,1,8,1,8,1,8,1,8,1,8,1,8,1,8,1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,
        1,9,3,9,103,8,9,1,9,1,9,1,9,1,9,1,9,4,9,110,8,9,11,9,12,9,111,1,
        9,1,9,1,9,1,9,1,9,1,9,4,9,120,8,9,11,9,12,9,121,1,9,1,9,1,9,3,9,
        127,8,9,1,9,1,9,1,10,1,10,1,10,1,10,1,10,1,10,1,10,1,10,1,10,3,10,
        140,8,10,1,10,1,10,1,10,1,10,1,10,4,10,147,8,10,11,10,12,10,148,
        1,10,1,10,1,10,1,11,1,11,1,11,1,11,5,11,158,8,11,10,11,12,11,161,
        9,11,1,12,1,12,1,12,1,12,3,12,167,8,12,1,12,0,0,13,0,2,4,6,8,10,
        12,14,16,18,20,22,24,0,0,171,0,26,1,0,0,0,2,33,1,0,0,0,4,37,1,0,
        0,0,6,54,1,0,0,0,8,56,1,0,0,0,10,67,1,0,0,0,12,69,1,0,0,0,14,77,
        1,0,0,0,16,85,1,0,0,0,18,93,1,0,0,0,20,130,1,0,0,0,22,153,1,0,0,
        0,24,166,1,0,0,0,26,27,5,1,0,0,27,28,3,2,1,0,28,29,3,8,4,0,29,30,
        5,2,0,0,30,31,6,0,-1,0,31,1,1,0,0,0,32,34,3,4,2,0,33,32,1,0,0,0,
        34,35,1,0,0,0,35,33,1,0,0,0,35,36,1,0,0,0,36,3,1,0,0,0,37,38,3,6,
        3,0,38,39,5,19,0,0,39,45,6,2,-1,0,40,41,5,15,0,0,41,42,5,19,0,0,
        42,44,6,2,-1,0,43,40,1,0,0,0,44,47,1,0,0,0,45,43,1,0,0,0,45,46,1,
        0,0,0,46,48,1,0,0,0,47,45,1,0,0,0,48,49,5,12,0,0,49,5,1,0,0,0,50,
        51,5,3,0,0,51,55,6,3,-1,0,52,53,5,4,0,0,53,55,6,3,-1,0,54,50,1,0,
        0,0,54,52,1,0,0,0,55,7,1,0,0,0,56,58,6,4,-1,0,57,59,3,10,5,0,58,
        57,1,0,0,0,59,60,1,0,0,0,60,58,1,0,0,0,60,61,1,0,0,0,61,9,1,0,0,
        0,62,68,3,12,6,0,63,68,3,14,7,0,64,68,3,16,8,0,65,68,3,18,9,0,66,
        68,3,20,10,0,67,62,1,0,0,0,67,63,1,0,0,0,67,64,1,0,0,0,67,65,1,0,
        0,0,67,66,1,0,0,0,68,11,1,0,0,0,69,70,5,5,0,0,70,71,5,10,0,0,71,
        72,5,19,0,0,72,73,6,6,-1,0,73,74,5,11,0,0,74,75,5,12,0,0,75,76,6,
        6,-1,0,76,13,1,0,0,0,77,78,5,6,0,0,78,79,5,10,0,0,79,80,5,19,0,0,
        80,81,6,7,-1,0,81,82,5,11,0,0,82,83,5,12,0,0,83,84,6,7,-1,0,84,15,
        1,0,0,0,85,86,5,19,0,0,86,87,6,8,-1,0,87,88,5,14,0,0,88,89,6,8,-1,
        0,89,90,3,22,11,0,90,91,5,12,0,0,91,92,6,8,-1,0,92,17,1,0,0,0,93,
        94,5,7,0,0,94,95,5,10,0,0,95,96,5,19,0,0,96,97,6,9,-1,0,97,98,5,
        18,0,0,98,102,6,9,-1,0,99,100,5,19,0,0,100,103,6,9,-1,0,101,103,
        5,20,0,0,102,99,1,0,0,0,102,101,1,0,0,0,103,104,1,0,0,0,104,105,
        6,9,-1,0,105,106,5,11,0,0,106,107,5,16,0,0,107,109,6,9,-1,0,108,
        110,3,10,5,0,109,108,1,0,0,0,110,111,1,0,0,0,111,109,1,0,0,0,111,
        112,1,0,0,0,112,113,1,0,0,0,113,114,5,17,0,0,114,126,6,9,-1,0,115,
        116,5,8,0,0,116,117,5,16,0,0,117,119,6,9,-1,0,118,120,3,10,5,0,119,
        118,1,0,0,0,120,121,1,0,0,0,121,119,1,0,0,0,121,122,1,0,0,0,122,
        123,1,0,0,0,123,124,5,17,0,0,124,125,6,9,-1,0,125,127,1,0,0,0,126,
        115,1,0,0,0,126,127,1,0,0,0,127,128,1,0,0,0,128,129,6,9,-1,0,129,
        19,1,0,0,0,130,131,5,9,0,0,131,132,5,10,0,0,132,133,5,19,0,0,133,
        134,6,10,-1,0,134,135,5,18,0,0,135,139,6,10,-1,0,136,137,5,19,0,
        0,137,140,6,10,-1,0,138,140,5,20,0,0,139,136,1,0,0,0,139,138,1,0,
        0,0,140,141,1,0,0,0,141,142,6,10,-1,0,142,143,5,11,0,0,143,144,5,
        16,0,0,144,146,6,10,-1,0,145,147,3,10,5,0,146,145,1,0,0,0,147,148,
        1,0,0,0,148,146,1,0,0,0,148,149,1,0,0,0,149,150,1,0,0,0,150,151,
        5,17,0,0,151,152,6,10,-1,0,152,21,1,0,0,0,153,159,3,24,12,0,154,
        155,5,13,0,0,155,156,6,11,-1,0,156,158,3,24,12,0,157,154,1,0,0,0,
        158,161,1,0,0,0,159,157,1,0,0,0,159,160,1,0,0,0,160,23,1,0,0,0,161,
        159,1,0,0,0,162,163,5,19,0,0,163,167,6,12,-1,0,164,165,5,20,0,0,
        165,167,6,12,-1,0,166,162,1,0,0,0,166,164,1,0,0,0,167,25,1,0,0,0,
        13,35,45,54,60,67,102,111,121,126,139,148,159,166
    ]

class IsiLangParser ( Parser ):

    grammarFileName = "IsiLang.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'programa'", "'fimprog;'", "'numero'", 
                     "'texto'", "'leia'", "'escreva'", "'se'", "'senao'", 
                     "'enquanto'", "'('", "')'", "';'", "<INVALID>", "'='", 
                     "','", "'{'", "'}'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "AP", "FP", "SC", "OP", 
                      "ATTR", "VIR", "ACH", "FCH", "OPREL", "ID", "NUMBER", 
                      "WS" ]

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
    RULE_cmdrepeticao = 10
    RULE_expr = 11
    RULE_termo = 12

    ruleNames =  [ "prog", "decl", "declaravar", "tipo", "bloco", "cmd", 
                   "cmdleitura", "cmdescrita", "cmdattrib", "cmdselecao", 
                   "cmdrepeticao", "expr", "termo" ]

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
    AP=10
    FP=11
    SC=12
    OP=13
    ATTR=14
    VIR=15
    ACH=16
    FCH=17
    OPREL=18
    ID=19
    NUMBER=20
    WS=21

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
            self.state = 26
            self.match(IsiLangParser.T__0)
            self.state = 27
            self.decl()
            self.state = 28
            self.bloco()
            self.state = 29
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
            self.state = 33 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 32
                self.declaravar()
                self.state = 35 
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
            self.state = 37
            self.tipo()
            self.state = 38
            self.match(IsiLangParser.ID)


            parseHelper.varName = self._input.LT(-1).text;
            parseHelper.varValue = None;
            symbol = IsiVariable(parseHelper.varName, parseHelper.tipo, parseHelper.varValue);
            if not parseHelper.symbolTable.exists(parseHelper.varName):
                parseHelper.symbolTable.add(symbol);	
            else:
                raise IsiSemanticException("Symbol "+parseHelper.varName+" already declared")
                                
            self.state = 45
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==IsiLangParser.VIR:
                self.state = 40
                self.match(IsiLangParser.VIR)
                self.state = 41
                self.match(IsiLangParser.ID)

                parseHelper.varName = self._input.LT(-1).text;
                parseHelper.varValue = None;
                symbol = IsiVariable(parseHelper.varName, parseHelper.tipo, parseHelper.varValue);
                if not parseHelper.symbolTable.exists(parseHelper.varName):
                    parseHelper.symbolTable.add(symbol);	
                else:
                    raise IsiSemanticException("Symbol "+parseHelper.varName+" already declared");
                                    
                self.state = 47
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 48
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
            self.state = 54
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [IsiLangParser.T__2]:
                self.enterOuterAlt(localctx, 1)
                self.state = 50
                self.match(IsiLangParser.T__2)
                parseHelper.tipo = IsiEnumType.NUMBER;  
                pass
            elif token in [IsiLangParser.T__3]:
                self.enterOuterAlt(localctx, 2)
                self.state = 52
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

                      
            self.state = 58 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 57
                self.cmd()
                self.state = 60 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << IsiLangParser.T__4) | (1 << IsiLangParser.T__5) | (1 << IsiLangParser.T__6) | (1 << IsiLangParser.T__8) | (1 << IsiLangParser.ID))) != 0)):
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
            self.state = 67
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [IsiLangParser.T__4]:
                self.enterOuterAlt(localctx, 1)
                self.state = 62
                self.cmdleitura()
                pass
            elif token in [IsiLangParser.T__5]:
                self.enterOuterAlt(localctx, 2)
                self.state = 63
                self.cmdescrita()
                pass
            elif token in [IsiLangParser.ID]:
                self.enterOuterAlt(localctx, 3)
                self.state = 64
                self.cmdattrib()
                pass
            elif token in [IsiLangParser.T__6]:
                self.enterOuterAlt(localctx, 4)
                self.state = 65
                self.cmdselecao()
                pass
            elif token in [IsiLangParser.T__8]:
                self.enterOuterAlt(localctx, 5)
                self.state = 66
                self.cmdrepeticao()
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
            self.state = 69
            self.match(IsiLangParser.T__4)
            self.state = 70
            self.match(IsiLangParser.AP)
            self.state = 71
            self.match(IsiLangParser.ID)
             

            parseHelper.verificaID(self._input.LT(-1).text)
            parseHelper.readID = self._input.LT(-1).text

                                    
            self.state = 73
            self.match(IsiLangParser.FP)
            self.state = 74
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

        def ID(self):
            return self.getToken(IsiLangParser.ID, 0)

        def FP(self):
            return self.getToken(IsiLangParser.FP, 0)

        def SC(self):
            return self.getToken(IsiLangParser.SC, 0)

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
            self.state = 77
            self.match(IsiLangParser.T__5)
            self.state = 78
            self.match(IsiLangParser.AP)
            self.state = 79
            self.match(IsiLangParser.ID)
             
            parseHelper.verificaID(self._input.LT(-1).text)
            parseHelper.writeID = self._input.LT(-1).text
                                 
            self.state = 81
            self.match(IsiLangParser.FP)
            self.state = 82
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
            self.state = 85
            self.match(IsiLangParser.ID)
             
            parseHelper.verificaID(self._input.LT(-1).text)
            parseHelper.exprID = self._input.LT(-1).text
                               
            self.state = 87
            self.match(IsiLangParser.ATTR)
            parseHelper.exprContent = "" 
            self.state = 89
            self.expr()
            self.state = 90
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
            self.state = 93
            self.match(IsiLangParser.T__6)
            self.state = 94
            self.match(IsiLangParser.AP)
            self.state = 95
            self.match(IsiLangParser.ID)

            parseHelper.exprDecision = self._input.LT(-1).text 
            parseHelper.setUsedVariable(self._input.LT(-1).text)

            self.state = 97
            self.match(IsiLangParser.OPREL)
            parseHelper.exprDecision += self._input.LT(-1).text 
            self.state = 102
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [IsiLangParser.ID]:
                self.state = 99
                self.match(IsiLangParser.ID)
                parseHelper.setUsedVariable(self._input.LT(-1).text)
                pass
            elif token in [IsiLangParser.NUMBER]:
                self.state = 101
                self.match(IsiLangParser.NUMBER)
                pass
            else:
                raise NoViableAltException(self)

            parseHelper.exprDecision += self._input.LT(-1).text 
            self.state = 105
            self.match(IsiLangParser.FP)
            self.state = 106
            self.match(IsiLangParser.ACH)
             
            curThread = []
            parseHelper.stack.append(curThread)
                                
            self.state = 109 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 108
                self.cmd()
                self.state = 111 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << IsiLangParser.T__4) | (1 << IsiLangParser.T__5) | (1 << IsiLangParser.T__6) | (1 << IsiLangParser.T__8) | (1 << IsiLangParser.ID))) != 0)):
                    break

            self.state = 113
            self.match(IsiLangParser.FCH)

            parseHelper.listaTrue = parseHelper.stack.pop()
                                
            self.state = 126
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==IsiLangParser.T__7:
                self.state = 115
                self.match(IsiLangParser.T__7)
                self.state = 116
                self.match(IsiLangParser.ACH)

                curThread = []
                parseHelper.stack.append(curThread)
                                   	 

                self.state = 119 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while True:
                    self.state = 118
                    self.cmd()
                    self.state = 121 
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << IsiLangParser.T__4) | (1 << IsiLangParser.T__5) | (1 << IsiLangParser.T__6) | (1 << IsiLangParser.T__8) | (1 << IsiLangParser.ID))) != 0)):
                        break

                self.state = 123
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
        self.enterRule(localctx, 20, self.RULE_cmdrepeticao)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 130
            self.match(IsiLangParser.T__8)
            self.state = 131
            self.match(IsiLangParser.AP)
            self.state = 132
            self.match(IsiLangParser.ID)

            parseHelper.exprDecision = self._input.LT(-1).text
            parseHelper.setUsedVariable(self._input.LT(-1).text)
             
            self.state = 134
            self.match(IsiLangParser.OPREL)
            parseHelper.exprDecision += self._input.LT(-1).text 
            self.state = 139
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [IsiLangParser.ID]:
                self.state = 136
                self.match(IsiLangParser.ID)
                parseHelper.setUsedVariable(self._input.LT(-1).text)
                pass
            elif token in [IsiLangParser.NUMBER]:
                self.state = 138
                self.match(IsiLangParser.NUMBER)
                pass
            else:
                raise NoViableAltException(self)

            parseHelper.exprDecision += self._input.LT(-1).text 
            self.state = 142
            self.match(IsiLangParser.FP)
            self.state = 143
            self.match(IsiLangParser.ACH)
             
            curThread = []
            parseHelper.stack.append(curThread)
                                
            self.state = 146 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 145
                self.cmd()
                self.state = 148 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << IsiLangParser.T__4) | (1 << IsiLangParser.T__5) | (1 << IsiLangParser.T__6) | (1 << IsiLangParser.T__8) | (1 << IsiLangParser.ID))) != 0)):
                    break

            self.state = 150
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
        self.enterRule(localctx, 22, self.RULE_expr)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 153
            self.termo()
            self.state = 159
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==IsiLangParser.OP:
                self.state = 154
                self.match(IsiLangParser.OP)

                parseHelper.exprContent += self._input.LT(-1).text

                self.state = 156
                self.termo()
                self.state = 161
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
        self.enterRule(localctx, 24, self.RULE_termo)
        try:
            self.state = 166
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [IsiLangParser.ID]:
                self.enterOuterAlt(localctx, 1)
                self.state = 162
                self.match(IsiLangParser.ID)
                     
                parseHelper.verificaID(self._input.LT(-1).text)
                parseHelper.verificaTipo(parseHelper.exprID, self._input.LT(-1).text)
                parseHelper.exprContent += self._input.LT(-1).text
                parseHelper.setUsedVariable(self._input.LT(-1).text)
                                 
                pass
            elif token in [IsiLangParser.NUMBER]:
                self.enterOuterAlt(localctx, 2)
                self.state = 164
                self.match(IsiLangParser.NUMBER)

                parseHelper.isNumber(parseHelper.exprID)                
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





