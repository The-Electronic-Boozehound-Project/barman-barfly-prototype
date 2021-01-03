# Read a file and reflow it to screen

import textwrap
import os

# Set up textwrappers and printers:

narrow = textwrap.TextWrapper(width = 40)

def line_printer(l):
    """Prints a list of lines, line by line."""
    


# Open file

with open('example_file.fly', 'r') as reader:
     x = reader.readlines()

# reflow
l = narrow.wrap(x)

#output
for el in l:
    print(el)
