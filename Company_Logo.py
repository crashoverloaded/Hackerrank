s="aabbbccde"
m=set(s)
d={}
for i in m:
	a=len(s)
	s=s.replace(i,"")
	d[i]=a - len(s)

from heapq import nlargest
three_largest = nlargest(3, d, key=d.get)
for  i in three_largest:
	print(i+" "+str(d[i])) 
