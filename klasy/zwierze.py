from abc import abstractmethod, ABCMeta
class Zwierze:
    def __init__(self):
        self.typ = 'nieznany'
    @abstractmethod
    def test(self):
        pass