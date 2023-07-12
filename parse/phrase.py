from abc import ABC, abstractmethod
from typing import Optional


class Phrase(ABC):
    @abstractmethod
    def get_value(self):
        ...


class Composite(Phrase):

    def __init__(self, left_phrase, right_phrase, operator):
        self.left_phrase: Optional[Phrase] = left_phrase
        self.right_phrase: Optional[Phrase] = right_phrase
        self.operator = operator

    def get_value(self):
        return self.operator(self.left_phrase.get_value(), self.right_phrase.get_value())


class Leaf(Phrase):
    def __init__(self, value:float):
        self.value: float = value

    def get_value(self):
        return self.value
