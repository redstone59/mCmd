"""
C[ommand Blocks] (mCmd) by redstone59

A compiler thingmabob to make creating large command block contraptions easier.

Feature list (maybe):
- C style formatting
- Scoreboard Variables
- Compiles into schematic or command block minecart trickery
- Comments turn into signs, helping debugging
- Automatically organised into seperate towers
"""

from arguments import *
from tokens import *
from errors import *

import regex as re

program_file = getattr(arguments,"in").read()
compiled_file = getattr(arguments,"out")

# Removing the stuff that the compiler doesn't need

def not_string(expression:str): #makes the regex not apply within a string
    result = []
    split_expression = expression.split('|')
    for x in split_expression:
        result.append(rf"{x}(?<!(?=.*\")\".*)|{x}(?<!(?=.*\')\'.*)")
    return "|".join(result)

program_trimmed = re.sub(not_string(r"//.*|/\*[\s\S]*\*/"),"",program_file) # Removing comments

macros = re.findall(not_string(r"#def.*\n"),program_trimmed) # Find all macro definitions in the program
program_trimmed = re.sub(not_string(r"#def.*\n"),"",program_trimmed) # Remove the macro definitions
for x in macros:
    definition = x.split()[1:] # Split the macro definition into the macro and it's expansion, trimming the #def
    program_trimmed = re.sub(definition[0]," ".join(definition[1:]),program_trimmed) #Replace all instances of the macro with it's expansion

program_trimmed = re.sub(not_string(r"\s*\n\s*"),"",program_trimmed) # Removing new lines and trimming beginning whitespace
program_trimmed = re.sub(not_string(r"\s*,\s*"),",",program_trimmed) # Trimming whitespace around commas


print(program_trimmed)

print("mcmd done")