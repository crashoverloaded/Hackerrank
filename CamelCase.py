def camelcase(s):
    n=0
    for i in s:
        if i.isupper() == True:
            n+=1
    return n+1
