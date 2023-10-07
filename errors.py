class InvalidMacroError(Exception): # for macro in macro definitions, could fix this with a for loop bodge tbh
    pass

class InvalidSelector(Exception): # for invalid player selectors (not @[spear]) holy shit thats a word
    pass

class InvalidCoordinate(Exception): # for coordinates that aren't fully caret notation
    pass

class SyntaxError(Exception):
    pass

class UndefinedFunction(Exception):
    pass

class ArithmeticError(Exception): # when would this ever come up lmao
    pass