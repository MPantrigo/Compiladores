import sys
from antlr4 import *

sys.path.append("C:/Users/mathe/Documents/GitHub/Compiladores")

from AnalisadorLexicoPython.parser.IsiLangLexer import IsiLangLexer
from AnalisadorLexicoPython.parser.IsiLangParser import IsiLangParser
from AnalisadorLexicoPython.exceptions.IsiSemanticException import IsiSemanticException
from AnalisadorLexicoPython.parser.IsiParserHelper import IsiParserHelper

def main():
    

    try:
        lexer = IsiLangLexer(FileStream("C:/Users/mathe/Documents/GitHub/Compiladores/AnalisadorLexicoPython/main/input.isi"))
        tokenStream = CommonTokenStream(lexer)

        parser = IsiLangParser(tokenStream)

        parser.prog()

        print("Compilation Sucessful")

        isiParser = parser.GetIsiParseHelper()

        isiParser.exibeComandos()

        isiParser.generateCode()

    except IsiSemanticException as e:
        print("Semantic Error" + e.message)
    except Exception as e:
        print("ERROR " + repr(e))

if __name__ == '__main__':
    main()    