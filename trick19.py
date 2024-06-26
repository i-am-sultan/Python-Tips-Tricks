#most frequent in a string
import collections

a = 'best of luck buddy'
b = collections.Counter(a).most_common()
print(a)
print(b)