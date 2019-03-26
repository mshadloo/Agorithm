class Solution:
    def inserionSort(self,arr):
        for i in range(1,len(arr)):
            j=i-1;
            temp=arr[i]
            while(j>=0 and arr[j]>temp):
                arr[j+1]=arr[j]
                j -=1
            arr[j+1]=temp
    def mergeSort(self,arr):
        return self._mergeSort_(arr,0,len(arr)-1)

    def _mergeSort_(self,arr,start,end):
        if(start==end):
            return [arr[start]]
        mid=(start+end)//2
        left=self._mergeSort_(arr,start,mid)
        right=self._mergeSort_(arr,mid+1,end)
        return self.merge(left,right)


    def merge(self,left,right):
        arr=[]
        i=0
        j=0
        k=0
        while(i<len(left) and j<len(right)):
            if(left[i]<=right[j]):
                arr.append(left[i])
                i += 1
            else:
                arr.append(right[j])
                j += 1

        if(i<len(left)):
            arr.extend(left[i:])

        elif(j<len(right)):
            arr.extend(right[j:])

        return arr;


    def countingSort(self,arr,range_):
        count={e:0 for e in range_}
        index={e:0 for e in range_}
        output=[0]*len(arr)

        for a in arr:
            count[a] += 1
        print(count)
        index[range_[0]] = count[range_[0]]-1
        for i in range(1,len(range_)):
            index[range_[i]] = index[range_[i-1]] + count[range_[i]]
        print(index)
        for i in range(len(arr)-1,-1,-1):
            print(index[arr[i]])
            output[index[arr[i]]]=arr[i]
            index[arr[i]] -=1

        return output


solution=Solution()
arr=[6,1,6,8,9,1,10]
solution.inserionSort(arr);
print(arr)
arr1=[1,4,6,9]
arr2=[2,3,6,8,10]
print(solution.merge(arr1,arr2))
arr=[6,1,6,8,9,1,10]
print(solution.mergeSort(arr))

arr=[6,1,6,8,9,1,10]
print(solution.countingSort(arr,range(1,11)))
