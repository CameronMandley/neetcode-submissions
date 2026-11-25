class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        # let dp[i][j] represent the min number of operations required to make word1[:i] == word2[:j]
        # then dp[i][j] = 1 + min(dp[i-1][j], dp[i][j-1]) if word1[i] != word2[j]
        # first create dp, then cover base case by checking the first letter in word1 and word2 and comparing against eachother, then iterate through both word and set the dp according to above, then return dp[-1][-1]
        m, n = len(word1), len(word2)
        dp = [[0]*(n+1) for _ in range(m+1)]
        # Input: word1 = "monkeys", word2 = "money"
        for i in range(1, m+1):
            dp[i][0] = i
        for i in range(1, n+1):
            dp[0][i] = i
        for i in range(1, m+1):
            for j in range(1, n+1):
                if word1[i-1] != word2[j-1]:
                    dp[i][j] = 1 + min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1])
                else:
                    dp[i][j] = dp[i-1][j-1]
        return dp[-1][-1]

        