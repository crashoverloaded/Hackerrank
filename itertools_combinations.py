from itertools import combinations
string,n=input().split()
for i in sorted(string):
    print(i)
a=list(combinations(sorted(string),int(n)))
a=[''.join(i) for i in a]
for i in a:
    print(i)
