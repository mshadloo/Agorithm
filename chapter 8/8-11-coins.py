class Solution:
    def makeChanges(self, n, coins):
        memo = [[0 for i in range(len(coins))] for i in range(n + 1)]

        for i in range(1, n + 1):
            if(i % coins[0] == 0):
                memo[i][0] = 1

        for j in range(1, len(coins)):
            for i in range(1, n + 1):
                if(i % coins[j] == 0):
                    memo[i][j] = 1
                for k in range(0, i + 1, coins[j]):
                    memo[i][j] += memo[i - k][j - 1]
        return memo[n][2]


solution = Solution()
print(solution.makeChanges(50, [5, 10, 25]))
