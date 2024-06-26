#memory size check

import sys
a = ['Love', 'Cold', 'Hot', 'Python']
b = {'Love', 'Cold', 'Hot', 'Python'}
c = ('Love', 'Cold', 'Hot', 'Python')


print(sys.getsizeof(a))
print(sys.getsizeof(b))
print(sys.getsizeof(c))

#conclusion "set" are most optimized(memory wise) data structure

