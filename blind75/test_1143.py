# Importing the Solution class from the solution_1143 file
from solution_1143 import Solution

def test_longest_common_subsequence():
    solution = Solution()

    # Test case 1
    text1 = "abcde"
    text2 = "ace"
    assert solution.longestCommonSubsequence(text1, text2) == 3, "Test case 1 failed"

    # Test case 2
    text1 = "abc"
    text2 = "def"
    assert solution.longestCommonSubsequence(text1, text2) == 0, "Test case 2 failed"

    print("All tests passed!")

if __name__ == "__main__":
    test_longest_common_subsequence()
