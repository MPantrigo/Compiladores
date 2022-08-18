from abc import abstractmethod


class AbstractCommand:

    @abstractmethod
    def generatePythonCode():
        pass