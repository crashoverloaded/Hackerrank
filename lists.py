#!/bin/python3
a=[]
for i in range(1,int(input())+1):
    pair_list=list(map(str,input().split()))
    if pair_list[0]== 'insert':
        a.insert(int(pair_list[1]),int(pair_list[2]))
    elif pair_list[0]== 'print':
        print(a)
    elif pair_list[0]== 'remove':
        a.remove(int(pair_list[1]))
    elif pair_list[0]== 'append':
        a.append(int(pair_list[1]))
    elif pair_list[0]== 'sort':
        a.sort()
    elif pair_list[0]== 'pop':
        a.pop()
    elif pair_list[0]== 'reverse':
        a.reverse()
    
