#iterable or not

arr = ['i', 'love', 'working', 'with', 'Python']

try:
    iter_check = iter(arr)
except:
    print('Object is not iterable')
else:
    print('Object is iterable')