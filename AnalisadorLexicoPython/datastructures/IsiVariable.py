from AnalisadorLexicoPython.datastructures.IsiSymbol import IsiSymbol
from AnalisadorLexicoPython.datastructures.IsiEnumType import IsiEnumType

class IsiVariable(IsiSymbol):

    def __init__(self, name, type, value, used=0):
        super().__init__(name)
        self.value = value
        self.type = type
        self.used = used

    def __str__(self):
        return "IsiVariable [name=" + str.name + ", type=" + type + ", value=" + str.value + "]";

    def getType(self):
        return self.type;

    def generatePythonCode(self):
        if self.type == IsiEnumType.NUMBER:
            str = "double"
        else:
            str = "String"
        return str + " "+super.name