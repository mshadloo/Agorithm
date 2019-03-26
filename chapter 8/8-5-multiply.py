class Solution:
   def multiply(self,a,b):
       smaller=min(a,b)
       bigger=max(a,b)
    def fastMultiply(self,samller,bigger):
        if(samller==0):
            return 0;
        if(samller==1):
            return bigger
        s1=samller>>1 #divided by 2
        m=self.fastMultiply(s1,bigger)
        m=m+m;
        if(smaller % 2==1):
            m +=bigger
        return m;
