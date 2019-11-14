#Given: A DNA string s of length at most 1000 nt.
#Return: Four integers (separated by spaces) counting the respective number of times that the symbols 'A', 'C', 'G', and 'T' occur in s.
DNA = open('rosalind_dna.txt','r')
s = DNA.read()
count = dict()
for n in s:
    count[n] = count.get(n, 0) + 1
print(count['A'],count['G'],count['C'],count['T'])

# LP comments
#
# Your solution is good, and follows on from the dictionary example. This is
# such a common requirement that Python actually gives you an even easier way
# to achieve the same goal.
#
# Having read in your file contents to the variable `s` as a string, you can
# use the string *method* `s.count()` to count occurrences of each character.
#
# An alternative solution using this would be:
#
# [...]
# s = DNA.read()
# print(s.count("A"), s.count("C"), s.count("G"), s.count("T"))