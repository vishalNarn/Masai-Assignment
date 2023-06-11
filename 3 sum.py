def f(A,n):
    L=[]
    for i in range(n):
        j=0; k=n-1
        while j<n and k>=0:
            s=A[i]+A[j]+A[k]
            if s==0:
                x=[A[i],A[j],A[k]]
                x.sort()
                if x not in L:
                    L.append(x)
            elif s>0:
                k-=1
            else:
                j+=1
    return L
A=[-1,0,1,2,-1,-4]
n=len(A)
print(f(A,n))