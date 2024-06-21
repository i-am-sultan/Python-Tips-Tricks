#Addding 1000 seperator in a large file

list1 = [-12, -45, -67, -89, -34, 67, -13]
print(list1)
new_list = [f"{num:,}" for num in list1]
print(new_list)