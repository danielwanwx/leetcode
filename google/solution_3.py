class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        count = {}
        res, j = 0, 0
        for i in range(len(s)):
            ch = s[i]
            count[ch] = count.get(ch, 0) + 1
            while j < len(s) and count[ch] > 1:
                count[s[j]] -= 1
                j += 1
            res = max(res, i - j + 1)

        return res