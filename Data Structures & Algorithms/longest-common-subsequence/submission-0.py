class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        # dp[i][j] represents the longest common subsequence between boths strings at index i and j respectively
        # dp[-1][-1] = the longest common subsequence between the entirety of both strings
        # Input: text1 = "cat", text2 = "crabt" 
        # dp = [[1, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0]]
        # i = 1, j = 1: text1[i] = a != text2[j] = r
        # i = 1, j = 2: text1[i] = a == text2[j] == a --> dp[i][j] = 1 + max(dp[i-1][j], dp[i][j-1]) = 1 + 
        dp = [[0]*len(text2) for _ in range(len(text1))]
        for i in range(len(text2)):
            if text1[0] == text2[i]:
                dp[0][i] = 1
            elif i > 0:
                dp[0][i] = dp[0][i-1]
        for i in range(len(text1)):
            if text1[i] == text2[0]:
                dp[i][0] = 1
            elif i > 0:
                dp[i][0] = dp[i-1][0]
        for i in range(1, len(text1)):
            for j in range(1, len(text2)):
                if text1[i] == text2[j]:
                    dp[i][j] = 1 + dp[i-1][j-1]
                else:
                    dp[i][j] = max(dp[i-1][j], dp[i][j-1], dp[i-1][j-1])
        return dp[-1][-1]
