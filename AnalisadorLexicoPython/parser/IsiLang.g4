grammar IsiLang;

@header{
sys.path.append("../..")
from AnalisadorLexicoPython.datastructures.IsiSymbol import IsiSymbol
from AnalisadorLexicoPython.datastructures.IsiVariable import IsiVariable
from AnalisadorLexicoPython.datastructures.IsiSymbolTable import IsiSymbolTable
from AnalisadorLexicoPython.exceptions.IsiSemanticException import IsiSemanticException
from AnalisadorLexicoPython.ast.IsiProgram import IsiProgram
from AnalisadorLexicoPython.ast.AbstractCommand import AbstractCommand
from AnalisadorLexicoPython.ast.CommandLeitura import CommandLeitura
from AnalisadorLexicoPython.ast.CommandEscrita import CommandEscrita
from AnalisadorLexicoPython.ast.CommandAtribuicao import CommandAtribuicao
from AnalisadorLexicoPython.ast.CommandDecisao import CommandDecisao
from AnalisadorLexicoPython.datastructures.IsiEnumType import IsiEnumType
from AnalisadorLexicoPython.parser.IsiParserHelper import IsiParserHelper
from AnalisadorLexicoPython.ast.CommandRepeticao import CommandRepeticao
from AnalisadorLexicoPython.ast.CommandCaso import CommandCaso


parseHelper = IsiParserHelper()


}

@members{

def GetIsiParseHelper(self):
    return parseHelper

}

prog	: 'programa' decl bloco  'fimprog;'
           {
parseHelper.program.setVarTable(parseHelper.symbolTable)
parseHelper.verificaVariavelUtilizada()
parseHelper.program.setComandos(parseHelper.stack.pop())       	 
           } 
		;
		
decl    :  (declaravar)+
        ;
        
        
declaravar :  tipo ID  {

parseHelper.varName = self._input.LT(-1).text;
parseHelper.varValue = None;
symbol = IsiVariable(parseHelper.varName, parseHelper.tipo, parseHelper.varValue);
if not parseHelper.symbolTable.exists(parseHelper.varName):
    parseHelper.symbolTable.add(symbol);	
else:
    raise IsiSemanticException("Symbol "+parseHelper.varName+" already declared")
                    } 
              (  VIR 
              	 ID {
parseHelper.varName = self._input.LT(-1).text;
parseHelper.varValue = None;
symbol = IsiVariable(parseHelper.varName, parseHelper.tipo, parseHelper.varValue);
if not parseHelper.symbolTable.exists(parseHelper.varName):
    parseHelper.symbolTable.add(symbol);	
else:
    raise IsiSemanticException("Symbol "+parseHelper.varName+" already declared");
                    }
              )* 
               SC
           ;
           
tipo       : 'numero' {parseHelper.tipo = IsiEnumType.NUMBER;  }
           | 'texto'  {parseHelper.tipo = IsiEnumType.TEXT;  }
           ;
        
bloco	: { 

curThread = [] 
parseHelper.stack.append(curThread);  

          }
          (cmd)+
		;
		

cmd		:  cmdleitura  
 		|  cmdescrita 
 		|  cmdattrib
 		|  cmdselecao
        |  cmdrepeticao  
        |  cmdcaso
		;
		
cmdleitura	: 'leia' AP
                     ID { 

parseHelper.verificaID(self._input.LT(-1).text)
parseHelper.readID = self._input.LT(-1).text

                        } 
                     FP 
                     SC 
                     
              {

var = parseHelper.symbolTable.get(parseHelper.readID)
cmd = CommandLeitura(parseHelper.readID, var)
parseHelper.stack[-1].append(cmd)

              }   
			;
			
cmdescrita	: 'escreva' 
                 AP 
                 (ID { 
parseHelper.verificaID(self._input.LT(-1).text)
parseHelper.writeID = self._input.LT(-1).text
                     } | TEXT )
                 FP 
                 SC
               {
cmd = CommandEscrita(parseHelper.writeID)
parseHelper.stack[-1].append(cmd)
               }
			;
			
cmdattrib	:  ID { 
parseHelper.verificaID(self._input.LT(-1).text)
parseHelper.exprID = self._input.LT(-1).text
                   } 
               ATTR {parseHelper.exprContent = "" } 
               expr 
               SC
               {
cmd = CommandAtribuicao(parseHelper.exprID, parseHelper.exprContent)
parseHelper.stack[-1].append(cmd)
               }
			;
			
			
cmdselecao  :  'se' AP
                    ID    {
parseHelper.exprDecision = self._input.LT(-1).text 
parseHelper.setUsedVariable(self._input.LT(-1).text)
}
                    OPREL {parseHelper.exprDecision += self._input.LT(-1).text }
                    (ID {parseHelper.setUsedVariable(self._input.LT(-1).text)}| NUMBER) {parseHelper.exprDecision += self._input.LT(-1).text }
                    FP 
                    ACH 
                    { 
curThread = []
parseHelper.stack.append(curThread)
                    }
                    (cmd)+ 
                    
                    FCH 
                    {
parseHelper.listaTrue = parseHelper.stack.pop()
                    } 
                   ('senao' 
                   	 ACH
                   	 {
curThread = []
parseHelper.stack.append(curThread)
                   	 } 
                   	(cmd+) 
                   	FCH
                   	{
parseHelper.listaFalse = parseHelper.stack.pop()
                   	}
                   )?
                   {
cmd = CommandDecisao(parseHelper.exprDecision, parseHelper.listaTrue, parseHelper.listaFalse)
parseHelper.stack[-1].append(cmd)
                   }
            ;

cmdcaso  :  'escolha' AP
                      (ID {parseHelper.setUsedVariable(self._input.LT(-1).text)}| NUMBER | TEXT)    
                      {
parseHelper.exprID = self._input.LT(-1).text 
                      }
                      FP
                      ACH
                      (
                    'caso' (ID {parseHelper.setUsedVariable(self._input.LT(-1).text)}| NUMBER | TEXT) 
                    {
parseHelper.exprDecision = self._input.LT(-1).text 
                    }
                    DP 
                    { 
curThread = []
parseHelper.stack.append(curThread)
                    }
                    (cmd)+ 
                    {
caseThread = parseHelper.stack.pop()
varBreak = False
                    }
                    ('break' {varBreak = True} SC)?
                    {
parseHelper.CasoDict[parseHelper.exprDecision] = (caseThread, varBreak)                  
                    })+
                      (
                    'default' 
                    DP
                    { 
curThread = []
parseHelper.stack.append(curThread)
                    }
                    (cmd)+ 
                    {
parseHelper.listaFalse = parseHelper.stack.pop()
                      }
                      )?
                      FCH
                     {
cmd = CommandCaso(parseHelper.exprID, parseHelper.CasoDict, parseHelper.listaFalse)
parseHelper.stack[-1].append(cmd)
                     }
            ;




cmdrepeticao  :  'enquanto' AP
                    ID    {
parseHelper.exprDecision = self._input.LT(-1).text
parseHelper.setUsedVariable(self._input.LT(-1).text)
 }
                    OPREL {parseHelper.exprDecision += self._input.LT(-1).text }
                    (ID {parseHelper.setUsedVariable(self._input.LT(-1).text)}| NUMBER) {parseHelper.exprDecision += self._input.LT(-1).text }
                    FP 
                    ACH 
                    { 
curThread = []
parseHelper.stack.append(curThread)
                    }
                    (cmd)+ 
                    
                    FCH 
                    {
parseHelper.listarepeticao = parseHelper.stack.pop()
cmd = CommandRepeticao(parseHelper.exprDecision, parseHelper.listarepeticao)
parseHelper.stack[-1].append(cmd)
                    } 
            ;
			
expr		: termo ( 
	             OP  {
parseHelper.isNumber(parseHelper.exprID)
parseHelper.exprContent += self._input.LT(-1).text
}
	            termo
	            )*
			;

			
termo		: ID {     
parseHelper.verificaID(self._input.LT(-1).text)
parseHelper.verificaTipo(parseHelper.exprID, self._input.LT(-1).text)
parseHelper.exprContent += self._input.LT(-1).text
parseHelper.setUsedVariable(self._input.LT(-1).text)
                 } 
            | 
              NUMBER
              {
parseHelper.isNumber(parseHelper.exprID)                
parseHelper.exprContent += self._input.LT(-1).text
              }
            |
              TEXT
              {
parseHelper.exprContent += self._input.LT(-1).text  
              }
			;
			
	
AP	: '('
	;
	
FP	: ')'
	;
	
SC	: ';'
	;
	
OP	: '+' | '-' | '*' | '/'
	;
	
ATTR : '='
	 ;
	 
VIR  : ','
     ;
     
ACH  : '{'
     ;
     
FCH  : '}'
     ;
	 
	 
OPREL : '>' | '<' | '>=' | '<=' | '==' | '!='
      ;
      
ID	: [a-z] ([a-z] | [A-Z] | [0-9])*
	;
	
NUMBER	: [0-9]+ ('.' [0-9]+)?
		;

TEXT    : '"'.*?'"'
        ;
		
WS	: (' ' | '\t' | '\n' | '\r') -> skip;

DP      :   ':'
        ;
