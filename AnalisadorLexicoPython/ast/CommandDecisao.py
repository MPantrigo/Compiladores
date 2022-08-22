from AnalisadorLexicoPython.ast.AbstractCommand import AbstractCommand

class CommandDecisao(AbstractCommand):
    def __init__(self, condition, lt, lf):
        self.condition = condition
        self.lt = lt
        self.lf = lf

    def __str__(self):
        return "CommandDecisao [condition=" + self.condition + ", listaTrue=" + "".join(str(i) for i in self.lt) + ", listaFalse=" + "".join(str(i) for i in self.lf)+ "]";

    def generateJavaCode(self):
        str = "if ("+self.condition+") {\n"
        for cmd in self.lt:
            str += self.indent(cmd.generateJavaCode(),4)

        str += "}\n"

        if len(self.lf) > 0:
            str += "else {\n"
            for cmd in self.lf:
                str += self.indent(cmd.generateJavaCode(),4)
            str += "}\n"
        return str 

    def generatePythonCode(self):
        str = "if "+self.condition+":\n"
        for cmd in self.lt:
            str += self.indent(cmd.generatePythonCode(),4)

        if len(self.lf) > 0:
            str += "else: \n"
            for cmd in self.lf:
                str += self.indent(cmd.generatePythonCode(),4)
        return str
    

