class InvalidMacroError(Exception):
    pass

class InvalidSelector(Exception): # for invalid player selectors (not @[spear]) holy shit thats a word
    pass

class SyntaxError(Exception):
    pass

class UndefinedFunction(Exception):
    pass

class ArithmeticError(Exception):
    pass