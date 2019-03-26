class Solution:
    def getPermutations1(self,s):


        if(len(s)==1):

            return [list(s)]
        hash2=dict();
        p_list=[];
        for i in range(len(s)):
            c=s[i]
            if(hash2.get(c) is None):
                hash2[c]=c;
                p=self.getPermutations(s[0:i]+s[i+1:])
                for l in p:

                    l.append(c)
                p_list.extend(p)
        return p_list


        #without dubs
    def permutationsFinder(self,s1,s2,permuations):
        if(len(s2)==1):
            permuations.append(s1+s2)
            return
        for i in range(len(s2)):
            c=s2[i];
            self.permutationsFinder(s1+c,s2[0:i]+s2[i+1:],permuations)

       #with dubs
    def permutationsFinder2(self,s1,s2,permuations):
        if(len(s2)==0):
            perin('bad state')
            return
        if(len(s2)==1):
            permuations.append(s1+s2)
            return
        hash2=dict();
        for i in range(len(s2)):
            c=s2[i];
            if(hash2.get(c) is None):

                hash2[c]=c;
                self.permutationsFinder2(s1+c,s2[0:i]+s2[i+1:],permuations)

solution1=Solution();
# l=solution1.getPermutations1('aaccd')
per=[];
solution1.permutationsFinder('','abc',per)
per2=[]
solution1.permutationsFinder2('','aabcc',per2)
print(per)
print(per2)
print(len(per2))
