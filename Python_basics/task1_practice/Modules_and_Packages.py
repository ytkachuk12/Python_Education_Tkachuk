'''In this exercise, you will need to print an alphabetically sorted list of all functions in the re module,
which contain the word find.'''

import re

# Your code goes here
list_of_funk = [item for item in dir(re) if "find" in item]
print(sorted(list_of_funk))
