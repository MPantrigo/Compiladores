# Generated from IsiLang.g4 by ANTLR 4.10.1
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .IsiLangParser import IsiLangParser
else:
    from IsiLangParser import IsiLangParser

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




# This class defines a complete listener for a parse tree produced by IsiLangParser.
class IsiLangListener(ParseTreeListener):

    # Enter a parse tree produced by IsiLangParser#prog.
    def enterProg(self, ctx:IsiLangParser.ProgContext):
        pass

    # Exit a parse tree produced by IsiLangParser#prog.
    def exitProg(self, ctx:IsiLangParser.ProgContext):
        pass


    # Enter a parse tree produced by IsiLangParser#decl.
    def enterDecl(self, ctx:IsiLangParser.DeclContext):
        pass

    # Exit a parse tree produced by IsiLangParser#decl.
    def exitDecl(self, ctx:IsiLangParser.DeclContext):
        pass


    # Enter a parse tree produced by IsiLangParser#declaravar.
    def enterDeclaravar(self, ctx:IsiLangParser.DeclaravarContext):
        pass

    # Exit a parse tree produced by IsiLangParser#declaravar.
    def exitDeclaravar(self, ctx:IsiLangParser.DeclaravarContext):
        pass


    # Enter a parse tree produced by IsiLangParser#tipo.
    def enterTipo(self, ctx:IsiLangParser.TipoContext):
        pass

    # Exit a parse tree produced by IsiLangParser#tipo.
    def exitTipo(self, ctx:IsiLangParser.TipoContext):
        pass


    # Enter a parse tree produced by IsiLangParser#bloco.
    def enterBloco(self, ctx:IsiLangParser.BlocoContext):
        pass

    # Exit a parse tree produced by IsiLangParser#bloco.
    def exitBloco(self, ctx:IsiLangParser.BlocoContext):
        pass


    # Enter a parse tree produced by IsiLangParser#cmd.
    def enterCmd(self, ctx:IsiLangParser.CmdContext):
        pass

    # Exit a parse tree produced by IsiLangParser#cmd.
    def exitCmd(self, ctx:IsiLangParser.CmdContext):
        pass


    # Enter a parse tree produced by IsiLangParser#cmdleitura.
    def enterCmdleitura(self, ctx:IsiLangParser.CmdleituraContext):
        pass

    # Exit a parse tree produced by IsiLangParser#cmdleitura.
    def exitCmdleitura(self, ctx:IsiLangParser.CmdleituraContext):
        pass


    # Enter a parse tree produced by IsiLangParser#cmdescrita.
    def enterCmdescrita(self, ctx:IsiLangParser.CmdescritaContext):
        pass

    # Exit a parse tree produced by IsiLangParser#cmdescrita.
    def exitCmdescrita(self, ctx:IsiLangParser.CmdescritaContext):
        pass


    # Enter a parse tree produced by IsiLangParser#cmdattrib.
    def enterCmdattrib(self, ctx:IsiLangParser.CmdattribContext):
        pass

    # Exit a parse tree produced by IsiLangParser#cmdattrib.
    def exitCmdattrib(self, ctx:IsiLangParser.CmdattribContext):
        pass


    # Enter a parse tree produced by IsiLangParser#cmdselecao.
    def enterCmdselecao(self, ctx:IsiLangParser.CmdselecaoContext):
        pass

    # Exit a parse tree produced by IsiLangParser#cmdselecao.
    def exitCmdselecao(self, ctx:IsiLangParser.CmdselecaoContext):
        pass


    # Enter a parse tree produced by IsiLangParser#cmdcaso.
    def enterCmdcaso(self, ctx:IsiLangParser.CmdcasoContext):
        pass

    # Exit a parse tree produced by IsiLangParser#cmdcaso.
    def exitCmdcaso(self, ctx:IsiLangParser.CmdcasoContext):
        pass


    # Enter a parse tree produced by IsiLangParser#cmdrepeticao.
    def enterCmdrepeticao(self, ctx:IsiLangParser.CmdrepeticaoContext):
        pass

    # Exit a parse tree produced by IsiLangParser#cmdrepeticao.
    def exitCmdrepeticao(self, ctx:IsiLangParser.CmdrepeticaoContext):
        pass


    # Enter a parse tree produced by IsiLangParser#expr.
    def enterExpr(self, ctx:IsiLangParser.ExprContext):
        pass

    # Exit a parse tree produced by IsiLangParser#expr.
    def exitExpr(self, ctx:IsiLangParser.ExprContext):
        pass


    # Enter a parse tree produced by IsiLangParser#termo.
    def enterTermo(self, ctx:IsiLangParser.TermoContext):
        pass

    # Exit a parse tree produced by IsiLangParser#termo.
    def exitTermo(self, ctx:IsiLangParser.TermoContext):
        pass



del IsiLangParser