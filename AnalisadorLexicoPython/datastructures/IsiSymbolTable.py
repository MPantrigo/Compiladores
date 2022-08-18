class IsiSymbolTable:

    def __init__(self):
        self.__map = {}

    def add(self, symbol):
        self.__map[symbol.name] = symbol

    def exists(self, symbolName):
        return symbolName in self.__map
    
    def get(self, symbolName):
        return self.__map[symbolName]

    def get_all(self):
        return self.__map.values()