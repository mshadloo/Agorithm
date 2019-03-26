class solution:
    def getMagicIndex(self,arr):
        return self.magicIndexFinder(arr,0,len(arr)-1)
    def magicIndexFinder(self,arr,i,j):
        mid=(i+j)/2;
        if(arr[mid]=mid):
            return mid
        if(arr[mid]>mid):
            s=self.magicIndexFinder(arr,i,mid-1)
            if(s is None):
                if(arr[mid]<j):
                 return self.magicIndexFinder(arr,arr[mid],j)
             else: return s
        else:
            s=self.magicIndexFinder(arr,mid+1,j)
            if(s is None):
                if(arr[mid]>i):
                 return self.magicIndexFinder(arr,i,arr[mid])
             else: return s
    def magicIndexFinder(self,arr,i,j):
        if(j<i):
            return None
        mid=(j+i)/2;
        if(arr[mid]=mid):
            return mid
        left=min(mid,arr[mid])
        right=max(mid,arr[mid])

