#NLARGEST AND LSMALLEST

import heapq

results = [12, 34, 67, 98, 90, 68, 55, 54, 64, 35]
print(heapq.nlargest(5,results))
print(heapq.nsmallest(5,results))