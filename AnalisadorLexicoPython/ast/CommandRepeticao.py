from AnalisadorLexicoPython.ast.AbstractCommand import AbstractCommand

class CommandRepeticao(AbstractCommand):
    def __init__(self, condition, lc):
        self.condition = condition
        self.lc = lc

    def __str__(self):
        return "CommandRepeticao [condition=" + self.condition + ", listarepeticao =" + "".join(str(i) for i in self.lc) + "]";
        
    def generatePythonCode(self):
        str = "while "+self.condition+":\n"
        for cmd in self.lc:
            str += self.indent(cmd.generatePythonCode(),4)
        return str

    def generateJavaCode(self):
        str = "while ("+self.condition+") {\n"
        for cmd in self.lc:
            str += self.indent(cmd.generateJavaCode(),4)

        str += "}\n"
        return str

