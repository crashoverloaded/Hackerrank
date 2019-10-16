# Enter your code here. Read input from STDIN. Print output to STDOUT
from itertools import combinations
string,n=input().split()
a=[]
for i in range(1,int(n)+1):
    a.append(list(combinations(sorted(string),i)))
#a=[''.join(i) for i in a for j in i]
for i in a:
    for j in i:
        print(''.join(j))
