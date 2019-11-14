#Given: A string s of length at most 200 letters and four integers a, b, c and d.
#Return: The slice of this string from indices a through b and c through d (with space in between), inclusively. In other words, we should include elements s[b] and s[d] in our slice.

# below is not my code  however using it for future reference
infile = open('rosalind_ini2.txt')
string1 = infile.readline()
string2 = infile.readline()
string2 = string2.split()
a=int(string2[0])
b=int(string2[1])
c=int(string2[2])
d=int(string2[3])
print(string1[a:b+1], string1[c:d+1])

# LP comments
#
# The above code - even though it works - isn't very elegant. Sometimes solutions
# are more important than elegance. But readbility is always useful and
# important. You'll want to know quickly, in six months time, what your code is
# doing when you come back to it. This code (which isn't yours!) isn't all that
# readable.
#
# The file opening isn't Pythonic. Your own code using the `with` context
# generator is better.
#
# The splitting of line two into four values could have been done in a single
# line:
#
# a, b, c, d = string2.split()
