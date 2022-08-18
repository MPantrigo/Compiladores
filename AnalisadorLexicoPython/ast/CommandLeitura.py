from AnalisadorLexicoPython.ast.AbstractCommand import AbstractCommand
from AnalisadorLexicoPython.datastructures.IsiVariable import IsiVariable
from AnalisadorLexicoPython.datastructures.IsiEnumType import IsiEnumType

class CommandLeitura(AbstractCommand):
    
    def __init__(self, id, var):
        self.id = id
        self.var = var
    

    def generatePythonCode(self):
        code = ""
        if self.var.type==IsiEnumType.NUMBER:
            code = "nextDouble()"
        else:
            code = "nextLine();"
        return  self.id +"= _key." + code