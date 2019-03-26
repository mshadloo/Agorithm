class Solution:
    def printParenthesis(self,n):


    def parenthesisCombinations(self,openNo,closeNo,s,combinations):
        if(openNo>closeNo):
            print('bad state')
            return None
        if(closeNo==0):
            combinations.append(s)
        if(openNo<closeNo):
            self.parenthesisCombinations(openNo,closeNo-1,s+')',combinations)
        if(openNo>0):
            self.parenthesisCombinations(openNo-1,closeNo,s+'(',combinations)

