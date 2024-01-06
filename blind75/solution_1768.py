class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        n, m = len(word1), len(word2)
        res = []
        i, j = 0, 0

        while i < n and j < m:
            res.append(word1[i])
            res.append(word2[j])
            i += 1
            j += 1
        while i < n:
            res.append(word1[i])
            i += 1
        while j < m:
            res.append(word2[j])
            j += 1
        return ''.join(res)
