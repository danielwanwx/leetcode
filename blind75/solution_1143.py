class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        # Get the lengths of the two input strings
        m, n = len(text1), len(text2)

        # Initialize a 2D array (dp) with zeros. The dimensions of the array
        # are (m+1) x (n+1) because we include the empty substring case for both strings.
        dp = [[0] * (n + 1) for _ in range(m + 1)]

        # Iterate over each character of both strings
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                # If the current characters of both strings match
                if text1[i - 1] == text2[j - 1]:
                    # The length of the LCS is 1 plus the length of the LCS
                    # up to the previous characters of both strings
                    dp[i][j] = dp[i - 1][j - 1] + 1
                else:
                    # If the current characters do not match, the length of the LCS
                    # is the maximum length of the LCS when either
                    # the current character of text1 or text2 is not included
                    dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

        # The value in dp[m][n] is the length of the LCS of text1 and text2
        return dp[m][n]
