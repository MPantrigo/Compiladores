from AnalisadorLexicoPython.ast.AbstractCommand import AbstractCommand
from AnalisadorLexicoPython.datastructures.IsiVariable import IsiVariable
from AnalisadorLexicoPython.datastructures.IsiEnumType import IsiEnumType

class CommandLeitura(AbstractCommand):
    
    def __init__(self, id, var):
        self.id = id
        self.var = var
    

    def generateJavaCode(self):
        code = ""
        if self.var.type==IsiEnumType.NUMBER:
            code = "nextDouble();\n"
        else:
            code = "nextLine();\n"
        return  self.id +"= _key." + code
    
    def generatePythonCode(self):
        code = ""
        if self.var.type==IsiEnumType.NUMBER:
            code = "input()\n"+self.id+" = float("+self.id+")"
        else:
            code = "input()"
        return  self.id +" = " + code