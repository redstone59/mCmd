from errors import *
from typing import *

class Token(): # what things could be shared between tokens? consider removing
    pass

class Assignment(Token): # assign value or scoreboard value to another scoreboard value
    def __init__(self, name: str, scoreboard: str, equal_name: str, equal_scoreboard: str): # -> scoreboard players operation name scoreboard = equal_name equal_scoreboard
        self.name = name
        self.scoreboard = scoreboard
        self.value = ScoreboardValue(equal_name, equal_scoreboard)
    
    @overload
    def __init__(self, name: str, scoreboard: str, value: int): # -> scoreboard players set name scoreboard value
        self.name = name
        self.scoreboard = scoreboard
        self.value = value

class Expression(Token):
    pass

class ScoreboardValue(Token):
    def __init__(self, name: str, scoreboard: str, value = 0):
        self.name = name
        self.scoreboard = scoreboard
        self.value = value # is this necessary? seems like an Assignment() thing. consider removing

class Coordinate(Token):
    def __init__(self, coords: list[int], tilde: list[bool], is_caret: bool):
        self.coords = coords
        self.tilde = tilde
        self.is_caret = is_caret
        
        for x in coords:
            if type(x) != int: raise InvalidCoordinate("Coordinates can only consist of integers")
        for x in tilde:
            if type(x) != bool: raise InvalidCoordinate("honestly how did you do this")
        if any(tilde) and is_caret: raise InvalidCoordinate("Caret notation must be used fully.")

class Arithmetic(Expression): # -> scoreboard players operation
    pass

class Comparison(Expression): # -> execute if score x n matches constant OR execute if score x n (equality/inequality) y m
    pass

class Function(Token): # -> command block towers
    def __init__(self, name: str, composition: list[Token]):
        self.name = name
        self.composition = composition

class Conditional(Function): # -> conditional command blocks (WHAT:bangbang:)
    def __init__(self, name: str, condition, composition: list[Token]):
        Function.__init__(self, name, composition)
        self.condition = condition