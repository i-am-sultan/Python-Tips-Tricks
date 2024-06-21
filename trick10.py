#Absolute value of a number
list1 = [-12, -45, -67, -89, -34, 67, -13]
list2 = []
for num in list1:
    list2.append(abs(num))
print(list2)

print([abs(num) for num in list1])