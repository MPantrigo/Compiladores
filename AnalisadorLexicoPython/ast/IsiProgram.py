

from cgitb import text
import traceback


class IsiProgram:
    def __init__(self, comandos, programName, varTable):
        self.__comandos = comandos
        self.__programName = programName
        self.__varTable = varTable
    
    def generateTarget(self):
        str = "def main(): \n\t"
        for cmd in self.__comandos:
            str += cmd.generatePythonCode() + "\n"

        try:
            text_file = open("mainPython.py", 'w')
            text_file.write(str)
            text_file.close()
        except:
            traceback.print_exc()

    def getVarTable(self):
        return self.__varTable
    
    def setVarTable(self, varTable):
        self.varTable = varTable
    
    def getComandos(self):
        return self.__comandos
    
    def setComandos(self, comandos):
        self.__comandos = comandos
    
    def getProgramName(self):
        return self.__programName

    def setProgramName(self, programName):
        self.__programName = programName