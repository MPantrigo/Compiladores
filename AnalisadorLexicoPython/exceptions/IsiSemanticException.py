class IsiSemanticException(Exception):
    def __init__(self, message):
        self.message = message
        super(IsiSemanticException, self).__init__ (message)