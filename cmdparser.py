"""
The thing that parses each individual line
"""

from errors import *

class Token():
    pass

class Assignment(Token): # -> scoreboard players set x n OR scoreboard players operation set x n = y m
    pass

class Expression(Token):
    pass

class Arithmetic(Expression): # -> scoreboard players operation
    pass

class Comparison(Expression): # -> execute if score x n matches constant OR execute if score x n (assignment operator) y m
    pass

class Function(Token): # -> command block towers
    def __init__(self, name: str, composition: list[Token]):
        self.name = name
        self.composition = composition

class Conditional(Function): # -> conditional command blocks (WHAT:bangbang:)
    def __init__(self, name, condition, composition: list[Token]):
        Function.__init__(self, name, composition)
        self.condition = condition