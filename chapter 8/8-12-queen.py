class Solution:
    def putQueens(self):
        queens = [-1 for i in range(8)]
        ways = []
        self.putQueen(queens, 0, ways)
        return ways

    def putQueen(self, queens, queenNo, ways):
        possibleCols = self.getPossibleCols(queens, queenNo)
        if(queenNo == 8):
            ways.append(queens[:])
        else:
            for c in possibleCols:
                queens[queenNo] = c
                self.putQueen(queens, queenNo + 1, ways)

    def getPossibleCols(self, queens, queenNo):
        cols = [1] * 8
        for i in range(queenNo):
            if(queens[i] is not -1):
                cols[queens[i]] = 0
                if(queens[i] + (queenNo - i) < 8):
                    cols[queens[i] + (queenNo - i)] = 0
                if(queens[i] >= (queenNo - i)):
                    cols[queens[i] - (queenNo - i)] = 0
        possibleCols = []
        for i in range(8):
            if(cols[i] == 1):
                possibleCols.append(i)
        return possibleCols


sol = Solution()
print(sol.putQueens())
