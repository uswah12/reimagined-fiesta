#Gven a file with 2 random numbers. Meant to generate the sum of their squares.
with open('rosalind_ini2.txt') as f:
        line = f.readline()
        a,b = map(int,line.split(" "))
        print(a**2 + b**2)

# LP comments
#
# Using the `with open() as` idiom is very Pythonic. This is good style!
#
# Using `map()` to apply a function to an iterable is good. It's not an
# approach I often use (it's a *functional* programming style, and I
# don't think that way, so much), but it's a nice approach. Alternatives
# (they're not better, just different) could be:
#
# a, b = [int(val) for val in line.split()]
#
# (note the space after the comma, which is Python style)
# This is a list comprehension, and does exactly what you've done already
# with map(). I'm including it for illustration only.
#
# line.split() will split on *any* whitespace (tab, space, newline, etc.)
# by default, so it doesn't need to be specified.
#
# There's another trick you can use with list comprehensions, which is:
#
# a, b = [int(_) for _ in line.split()]
#
# The `_` (underscore) character is a temporary stand-in variable that
# doesn't require an explicit name. This can save memory in larger
# applications