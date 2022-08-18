from abc import abstractmethod


class IsiSymbol:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return "IsiSymbol [name=" + self.name + "]";
    
    @abstractmethod
    def generatePythonCode():
        pass
