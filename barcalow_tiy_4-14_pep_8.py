# Rule 1 that I want to keep in mind: indents are 4 spaces, and closing
# parentheses or brackets can be indented or not.
example_list_of_things = [
    "thing 1",
    "a separate thing",
    "another thing",
    "PyCharm formats some of this automatically"
]

# Rule 2: Lines of space separate different sections in the code.
if True and (False or True):
    [print(example) for example in example_list_of_things]

# Two lines before and after top-level function and class definitions,
# one line for method definitions within classes.
# Blank lines can also be used between groups of related functions and
# between logical sections.
"""Rule 3: Pick a type of quote mark and stick with it. Use the opposite when
you need to type a single or double quote in a string. Try to avoid using
backslashes to improve readability. Always use double quotes for docstrings.
"""

# Rule 4 (I know we were only supposed to do three, but this one's important):
# Whitespace ALWAYS goes on both sides of these operators:
# =, +=, -=, ==, <, >, <=, >=
# in, not in, is, is not, and, or, not
# BOTH. SIDES. In math equations, whitespace can be placed around the operator
# with the lowest priority (1 + 2*5 - 16/2).