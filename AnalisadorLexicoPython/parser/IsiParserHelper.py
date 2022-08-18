from AnalisadorLexicoPython.datastructures.IsiSymbolTable import IsiSymbolTable
from AnalisadorLexicoPython.ast.IsiProgram import IsiProgram
from AnalisadorLexicoPython.exceptions.IsiSemanticException import IsiSemanticException

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
        self.listaFalse = []
        self.listaTrue = []

    def verificaID(self, id):
        if not self.symbolTable.exists(id):
            raise IsiSemanticException("Symbol "+id+" not declared")

    def exibeComandos(self):
        for cmd in self.program.getComandos():
            print(cmd)
	

    def generateCode(self):
        self.program.generateTarget()