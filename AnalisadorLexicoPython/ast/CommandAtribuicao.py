
from AnalisadorLexicoPython.ast.AbstractCommand import AbstractCommand


class CommandAtribuicao(AbstractCommand):
    def __init__(self, id, expr):
        self.id = id
        self.expr = expr

    def generatePythonCode(self):
        return self.id + " = " + self.expr+"\n"
    
    def generateJavaCode(self):
        return self.id + " = " + self.expr+";\n"

    def __str__(self):
        return "CommandAtribuicao [id=" + self.id + ", expr=" + self.expr + "]";