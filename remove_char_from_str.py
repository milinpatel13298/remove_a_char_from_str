def remove(str,k):
    if type(k)==int:
        if k>=0 and k<len(str):
            return str[:k]+str[k+1:]
        else:return str
    else:
        pos=-1
        for i in str:
            pos+=1
            if i==k:
                break
        print(pos)
        if pos==len(str)-1:
            if str[pos]==k:
                print(k)
                return remove(str,pos)
            else:return str
        else:return remove(str,pos)
"""str='string'
str=remove(str,'i')     #removes 'i' from str
print(str)
str=remove(str,1)       #removes str[1] from str
print(str)"""
