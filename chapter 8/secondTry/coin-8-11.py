# find the number of different ways to make change given amount N into 5,10,25 cents

class Solution:
    def change(self,amount,coins):
        coins.sort();
        memo=[[0 for i in range(len(coins))] for j in range(amount+1)]
        for n in range(1,amount+1):
            if(n%coins[0]==0):
                memo[n][0]=1
            for i in range(1,len(coins)):
                if(n%coins[i]==0):
                    memo[n][i]=1
                for k in range(n//coins[i]+1):
                    memo[n][i] += memo[n-k*coins[i]][i-1]
        return memo[amount][len(coins)-1]


coins=[5,10,25]
solution=Solution();
print(solution.change(50,coins))
