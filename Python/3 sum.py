L=[]
A=[-1,0,1,2,-1,-4]
A.sort()
n=len(A)
def f(A,n):
    for i in range(n):
        j=0; k=n-1
        while j<n and k>=0 and i!=j and j!=k and k!=i:
            s=A[i]+A[j]+A[k]
            if s==0:
                x=[A[i],A[j],A[k]]
                if x not in L:
                    L.append(x)
                    k-=1
                    j+=1
            elif s>0:
                k-=1
            else:
                j+=1
    return L
print(f(A,n))