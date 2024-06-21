#how to find the index of the biggest number
x = [12, 45, 67, 89, 34, 67, 13]
y = x.copy()
x.sort(reverse='true')
print(y.index(x[0]))

#using max and enumerate function

max_number = max(enumerate(y,start=0),key=lambda y:y[1])
min_number = min(enumerate(y,start=0),key=lambda y:y[1])
print(max_number)
print(min_number)