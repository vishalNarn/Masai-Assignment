def f(ans,s,l,r):
    if l<=r+1 and ans!='':
        print(ans)
    for i in range(l,r+1):
        f(ans+s[i],s,i+1,r)
f('','abcd',0,3)