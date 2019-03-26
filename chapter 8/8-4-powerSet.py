class Solution:
    def getPowerSet(self,s):
        if(s is None):
             return None
        if(len(s)==1):
            return[[],s];
        subSets=self.getPowerSet(s[1:len(s)])
        n=len(subSets)
        for i in range(n):
            l=list(subSets[i]);
            l.append(s[0])
            subSets.append(l)
        return subSets
    def getPowerSet2(self,s):
        if(s is None):
            return None
        if(len(s)==1):
            return[[],s];
        sets_num=1<<len(s);
        subSets=[];
        for i in range(sets_num):
            subSets.append(self.intToSubSet(s,i))
        return subSets


    def intToSubSet(self,s,n):
        subset=[];
        for i in range(len(s)):
            if(n&1==1):
                subset.append(s[i]);
            n >>= 1
            if(n==0):
                break
        return subset
solution1=Solution()
s=[1,2,3]
print(solution1.getPowerSet(s))
print(solution1.getPowerSet2(s))



