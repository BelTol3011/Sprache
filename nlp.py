from base import *


class Clause:
    def __init__(self, text: str):
        self.text = text

    def __str__(self):
        return self.text


class MainClause(Clause):
    def __init__(self, text: str):
        super().__init__(text)


class SubordinateClause(Clause):
    def __init__(self, text: str):
        super().__init__(text)


class Sentence:
    def __init__(self, clauses: list[Clause]):
        pass