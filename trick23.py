#itemgetter module 

from operator import itemgetter

names = [('Ben','Jones'),('Peter','Parker'),
 ('Kelly','Isa')]

#sort name by first name
sorted_names = sorted(names,key=itemgetter(0))
print(sorted_names)

#sort by last name
sorted_names = sorted(names,key=itemgetter(1))
print(sorted_names)