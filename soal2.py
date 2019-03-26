def findFirstMissedPositive(arr):
    firstPos=-1
    for i  in range(len(arr)):
        if(arr[i]>0):
            firstPos=i;
            break
    if(firstPos==-1):

        return 'There is no positive number in the given array'
    if(arr[firstPos]!=1):
        return 1;
    for i in range(firstPos,len(arr),1):
        if(arr[i]-1> i-firstPos):
            return arr[i]-1
    return 'There is no missing positive number in the given array'


arr=[-4,-3,-2,2,3,5]
print(findFirstMissedPositive(arr))
