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

import regex as re
import parsimonious
import time

START_TIME = time.time()

program_file = getattr(arguments,"in").read()
compiled_file = getattr(arguments,"out")

# Removing the stuff that the compiler doesn't need, preprocessing
print("Preprocessing...")

def check_character_position(check:int, positions):
    for x in positions:
        if x[0] <= check <= x[1]: return False
    return True

def substitute_unless(pattern:str, unless:str, replacement:str, string:str):
    quotes = re.findall(unless, string)
    string = re.sub(unless, "%s", string)
    string = re.sub(pattern, replacement, string)
    string %= tuple(quotes)
    return string

def sub_not_string(pattern:str, replacement:str, string:str):
    return substitute_unless(pattern,r"\".*?\"|\'.*?\'",replacement,string)

program_trimmed = sub_not_string(r"//.*|/\*[\s\S]*?\*/","",program_file) # Removing comments

macros = re.findall(r"#def.*\n",program_trimmed) # Find all macro definitions in the program
program_trimmed = sub_not_string(r"#def.*\n","",program_trimmed) # Remove the macro definitions
for i in range (10): # Allow for macro in macro up to 10 macros deep (this is so a bodge of something)
    for x in macros:
        definition = x.split()[1:] # Split the macro definition into the macro and it's expansion, trimming the #def
        program_trimmed = sub_not_string(definition[0]," ".join(definition[1:]),program_trimmed) #Replace all instances of the macro with it's expansion

program_trimmed = sub_not_string(r"\s*\n\s*","",program_trimmed) # Removing new lines and trimming beginning whitespace
program_trimmed = sub_not_string(r"\s*,\s*",",",program_trimmed) # Trimming whitespace around commas

# Parsing what is left



print(program_trimmed)

print(f"mCmd successfully compiled {getattr(arguments,'in').name} in {(time.time() - START_TIME) // 0.001 * 0.001}s.") # such a silly way to round a number to 2dp
