import math;
def nextPermutation(p):
    n=len(p)
    if(n==1):
        return None

    if(isMaximum(p)):
        return None
    if(n==2):
        switch(p,0,1)
        return p;

    # isDone=False
    # for k in range(n-2,-1,-1):
    #     s=nextPermutation(p[k:n])
    #     if(s is None):

    # for i in range(n-1,-1,-1):
    for k in range(n-2,-1,-1):
        if( isMaximum(p[k:n]) is False):
            break
    for i in range(n-1,k,-1):
        if(p[i]>p[k]):
            break

    switch(p,k,i)
    if(k<n-2):
        p[k+1:n]=reversed(p[k+1:n])


    # i=n-2;
    # j=n-2;
    # while(i>=0 and p[-1]<p[i] ):
    #     i -=1
    # if(i==n-2):
    #     switch(p,i,n-1)
    # else:
    #     s=nextPermutation(p[i+1:-1])
    #     if(s is None):
    #         switch(p,i,n-1)
    #         p[i+1:n]=reversed(p[i+1:n])
    #     else:
    #         p[i+1:-1]=s;
    #         switch(p,n-2,n-1)
    return p
def isMaximum(p):
    n=len(p)
    flag=True;
    for i in range(n-1):
        if(p[i]<p[i+1]):
            flag=False
    return flag
def switch(arr,i,j):
    temp=arr[i]
    arr[i]=arr[j]
    arr[j]=temp

p=[0,1,2,3]
for i in range(math.factorial(len(p))):
    print(nextPermutation(p))

