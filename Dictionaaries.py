#!/usr/bin/python3

d={}
for i in range(0,int(input())):
    a,b=list(map(str,input().split()))
    d[a]=b
for i in range(0,len(d)):
    a=input()
    if a in d:
        print(a+"="+d[a])
    else:
        print("Not found")

