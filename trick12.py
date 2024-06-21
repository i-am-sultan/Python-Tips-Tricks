#startswith and endswith function in postgresql

list1 = ['lemon','Orange','apple', 'apricot']
new_list = [i for i in list1 if i.startswith('a')]
new_list2 = [i for i in list1 if i.endswith('t')]

print(new_list)
print(new_list2)