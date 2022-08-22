from genericpath import exists
import warnings
from AnalisadorLexicoPython.datastructures.IsiSymbolTable import IsiSymbolTable
from AnalisadorLexicoPython.ast.IsiProgram import IsiProgram
from AnalisadorLexicoPython.exceptions.IsiSemanticException import IsiSemanticException
from AnalisadorLexicoPython.datastructures.IsiEnumType import IsiEnumType

class IsiParserHelper:
    def __init__(self):
        self.symbolTable = IsiSymbolTable()
        self.program = IsiProgram([], "main", [])
        self.varName = ""
        self.tipo = 0
        self.varValue = None
        self.writeID = ""
        self.readID = ""
        self.stack = []
        self.exprDecision = ""
        self.exprContent = ""
        self.exprContentWithValues = ""
        self.listaFalse = []
        self.listaTrue = []
        self.listaRepeticao = []

    def verificaID(self, id):
        if not self.symbolTable.exists(id):
            raise IsiSemanticException(" Symbol "+id+" not declared")

    def exibeComandos(self):
        for cmd in self.program.getComandos():
            print(cmd)
	
    def verificaTipo(self, exprID, termID):
        varExpr = self.symbolTable.get(exprID)
        varTerm = self.symbolTable.get(termID)
        if varExpr.type != varTerm.type:
            raise IsiSemanticException(" Symbol "+ exprID + " does not have the same type as " + termID + " attibution fails!")

    def isNumber(self, exprID):
        varExpr = self.symbolTable.get(exprID)
        if varExpr.type != IsiEnumType.NUMBER:
            raise IsiSemanticException(" Symbol "+ exprID + " is not a number, attibution fails!")

    def generateCode(self):
        self.program.generateTarget()

    def verificaVariavelUtilizada(self):
        for var in self.program.varTable.get_all():
            if var.used == 0:
                warnings.warn("Variavel "+ var.name + " not utilized!", stacklevel=2)
                
    def setUsedVariable(self, id):
        var = self.symbolTable.get(id)
        var.used = 1
        self.symbolTable.add(var)
