from solution_3 import Solution

def test_length_of_longest_substring():
    solution = Solution()
    assert solution.lengthOfLongestSubstring("abcccb") == 3, "Error in test case 1"
    assert solution.lengthOfLongestSubstring("ab") == 2, "Error in test case 2"
    assert solution.lengthOfLongestSubstring("aaaaa") == 1, "Error in test case 3"


# Run the test function
if __name__ == "__main__":
    test_length_of_longest_substring()
    print("All tests for 1768 passed!")
