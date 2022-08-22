from abc import abstractmethod
import textwrap


class AbstractCommand:

    @abstractmethod
    def generatePythonCode():
        pass

    @abstractmethod
    def generateJavaCode():
        pass

    def indent(self, text, amount, ch=' '):
        return textwrap.indent(text, amount * ch)