from tokens import *
from parsimonious import *

OPERATORS = (
    ">",      # matches (x+1)..
    ">=",     # matches x..
    "==",     # matches x
    "<=",     # matches ..x
    "<",      # matches ..(x-1)
    "within", # matches x..y (substitute with x <= thing <= y ? but i could use the square and round bracket notation)
    
    "&&",     # simply combine the execute stuffs
    "||",     # two seperate command blocks?
    "^",      # i have no idea how to implement this lmao
    "!",      # execute unless instead of execute if
    
    # scoreboard players operation
    "+",
    "-",
    "*",
    "/",
)

grammar = Grammar(
    r"""
    function    = ("void" / "int" / "bool") w* name w* arguments w* composition
    conditional = ("if" / "else" / "elif") w* arguments w* composition
    expression  = value w* (operator w* value)+
    
    arguments   = "(" text ")"
    composition = "{" text "}"
    
    string      = ('"' text '"') / ("'" text "'")
    verbatim    = "<" text ">"
    nbt         = "[" text "]"
    player      = "@" ~r"spear" ("[" text "]")?
    
    assignment  = scoreboard w* "=" w* value
    value       = scoreboard / constant
    scoreboard  = name w+ name
    coordinate  = "{" w* constant "," w* constant "," w* constant "}"
    constant    = ~r"\d*"
    
    operator    = w* (""" + "'" + "' / '".join(OPERATORS) + "'" + """) w*
    
    name        = ~r"\w*"
    text        = ~r"[\s\S]*"
    w           = ~r"\s*"
    """
)

grammar.parse("5+ 2")