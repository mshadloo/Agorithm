def findCelebrity(know,n):
    for i in range(n):
        isCelebrity=True;
        for j in range(n):
            if(know[i][j]==1 and i!=j):
                isCelebrity=False;
                break
            if(not know[j][i]==1 ):
                isCelebrity=False
                break
        if(isCelebrity):
            return i;

know=((1,0,1,1),(0,1,1,0),(0,0,1,0),(0,1,1,1))
print(findCelebrity(know,4))
