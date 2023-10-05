"""
A list of tokens that mCmd uses, probably. These aren't finalised I just thought I might need them.
"""

TOKENS = (
    "void",   # doesn't return
    "int",    # returns to a scoreboard value
    "bool",   # returns to a scoreboard value but its just a 0/1, helps with readability prolly
    
    "if",     # execute if
    "at",     # execute at (substitute with @@? could be confused for players however)
)

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