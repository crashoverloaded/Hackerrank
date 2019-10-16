# Enter your code here. Read input from STDIN. Print output to STDOUT
from itertools import combinations
n=int(input())
a=list(map(str,input().split()))
k=int(input())
b=list(combinations(a,k))
print(b)
new=[]
for i in range(0,k):
    new.append(a[i])
count=0
print(new)
for i in b:
    for j in new:
        if i[0] == j:
            count+=1
print("%.4f" % ((count/2)/len(b)))
