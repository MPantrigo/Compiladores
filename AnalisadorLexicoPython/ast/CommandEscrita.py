from AnalisadorLexicoPython.ast.AbstractCommand import AbstractCommand

class CommandEscrita(AbstractCommand):

    def __init__(self, id):
        self.id = id

    def generatePythonCode(self): 
        return "print("+self.id+")\n"

    def generateJavaCode(self): 
        return "System.out.println("+self.id+");\n"

    def __str__(self):
        return "CommandEscrita [id=" + self.id + "]"