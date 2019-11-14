f = open('rosalind_ini6.txt','r')
f_r = f.read()
counts = dict()
for word in f_r.split(' '):
    counts[word] = counts.get(word,0) + 1
for word in counts:
    print(word, counts[word])

# LP Comments
#
# It's more Pythonic to use the `with` idiom, as you've done elsewhere. I'd
# recommend sticking with context management, where possible.
#
# Your other files had a clear statement of the problem as a comment at the
# head of the file, and it's worth always doing this. I know that me in six
# months rarely remembers what the me of today was doing. I had to look up
# the problem on Rosalind to be sure what you were aiming for
#
# The solution is almost exactly how I'd solve the problem.
# 
# There's a wee bit of compression you could do, as you don't need to
# declare `f_r` and hold it in memory. There's nothing wrong with what
# you've done, but as I'm dealing with large files I'm used to processing
# them as efficiently as I can.  To do that, I'd typically write:
#
# for word in f.read().split():
#   [...]
#
# and read the file in without creating a new variable. But there's nothing
# wrong about what you've done.
#
# There is, in Python, a `Counter` object. It's a slightly more advanced
# topic, but you could count words directly using something like [UNTESTED]:
#
# from collections import Counter
#
# ctr = Counter()
# with open("myfile.txt", "r") as ifh:
#   ctr.count(ifh.split())
# for word, count in ctr.items():
#   print(word, count)
#
# You can get more information at https://pymotw.com/2/collections/counter.html -
# it more or less implements what you've written in answer to this problem.
