from AnalisadorLexicoPython.ast.AbstractCommand import AbstractCommand


class CommandCaso(AbstractCommand):
    def __init__(self, id, dictExpr, lf):
        self.id = id
        self.dictExpr = dictExpr
        self.lf = lf

    def generatePythonCode(self):
        str = "match " + self.id + ":\n"
        for a in self.dictExpr:
            str += self.indent("case "+a+":\n",4)
            for cmd in self.dictExpr[a][0]:
                str += self.indent(cmd.generatePythonCode(),8)
        if len(self.lf) > 0:
            str += self.indent("case default :\n",4)
            for cmd in self.lf:
                str += self.indent(cmd.generatePythonCode(),8)

        return str
    
    def generateJavaCode(self):
        str = "switch (" + self.id + ") {\n"
        for a in self.dictExpr:
            str += self.indent("case "+a+":\n",4)
            for cmd in self.dictExpr[a][0]:
                str += self.indent(cmd.generateJavaCode(),8)
            if self.dictExpr[a][1] == True:
                str += self.indent("break;\n",8)
        if len(self.lf) > 0:
            str += self.indent("case default :\n",4)
            for cmd in self.lf:
                str += self.indent(cmd.generateJavaCode(),8)
        str += "}"
        return str

    def __str__(self):
        strin = "CommandAtribuicao [id=" + self.id + " Casos "
        for a in self.dictExpr:
            strin += a + ": "+ "".join(str(i) for i in self.dictExpr[a]) 
        strin += "Default : " + "".join(str(i) for i in self.lf) + "]"
        return strin