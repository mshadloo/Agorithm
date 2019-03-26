class Solution:
    def findDuplicates(self,arr):
        bits= [0 for i in range(1<<10+1)]
        result=set();
        for a in arr:
            c=a/32;
            r=a% 32;
            b=1<<r;
            if (bits[c] & b is not 0):
                result.add(a)
            bits[c] |= b
        return result


solution=Solution()
print(list(solution.findDuplicates([1,2,3,1000,1200,32,64,2,8,1000,64])))
