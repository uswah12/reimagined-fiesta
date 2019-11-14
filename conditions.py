#Given: Two positive integers a and b (a<b<10000). Return:The sum of all odd integers from a through b, inclusively.
lst = list()
value = 0
with open('rosalind_ini4.txt') as f:
        line = f.readline()
        a,b = map(int,line.split(" "))
        lst.append(a)
        lst.append(b)

for number in lst:
    if number >= a and number < b-1:
        number = number + 1
        lst.append(number)
    else:
        pass
for number in lst:
    if number % 2 == 1:
        value = value + number
    else:
        pass
print("List:", lst)
print("Sum:", value)

# You have a working solution, which is the point of the exercise. That's good.
#
# There are some features of Python that you might not have got to yet, which
# could help make this solution shorter and more efficient, and also clearer.
# One wee unusual thing with your approach is that the items in your list `lst`
# will not be ordered. They run:
#
# [first, last, second, third, ..., last-but-one]
#
# and that would bug me in my own code ;)
#
# To see how to get to a faster solution, we can think about it like this:
#
# 1. Get limits from the file (your `a` and `b` values)
# 2. Generate a list of values from `a` to `b + 1`
#    2a. Add these values to our output list only if the numbers are even
# 3. Report the list and the sum
#
# You've already got (1), but see my notes in `variables.py` about assignment.
#
# Now, with `a` as the low value, and `b` as the high value, we can create a
# list of numbers from `a` to `b + 1` with Python's range() function:
#
# >>> range(20, 31)
# range(20, 31)
#
# `range()`` returns a `range` object, but it can be converted to a list
# with `list()`, to see what numbers are in it.
#
# >>> list(range(20, 31))
# [20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30]
#
# And we can also use a list comprehension to do this (see `variables.py`):
#
# >>> [_ for _ in range(20, 31)]
# [20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30]
#
# A big advantage of list comprehensions is that we can *filter* them with an
# `if` statement. Here, we'd adapt your test:
#
# if number % 2 == 1: [...]
#
# Noting that in Python, `0` is `False` and `1` is `True`, so:
#
# >>> 20 % 2
# 0
# >>> 20 % 2 == False
# True
# >>> 21 %2
# 1
# >>> 21 % 2 == True
# True
#
# and we can use this as:
#
# >>> [_ for _ in range(20, 31) if _ % 2]
# [21, 23, 25, 27, 29]
#
# which gives us a list of all the odd numbers from `a` to `b`.
#
# You can then shrink your code down to:
#
# with open('rosalind_ini4.txt') as f:
#   a, b = map(int, f.readline().split())      # 1
#   odds = [_ for _ in range(a, b) if _ % 2]   # 2 and 2a
#
# print("List:", odds)                         # 3
# print("Sum:", sum(odds))