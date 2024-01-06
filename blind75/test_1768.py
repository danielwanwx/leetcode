from solution_1768 import Solution  # Adjust the import based on your file name and structure

def test_merge_alternately():
    solution = Solution()
    assert solution.mergeAlternately("abc", "pqr") == "apbqcr", "Error in test case 1"
    assert solution.mergeAlternately("ab", "pqrs") == "apbqrs", "Error in test case 2"
    assert solution.mergeAlternately("abcd", "p") == "apbcd", "Error in test case 3"
    # Add more test cases as needed

# Run the test function
if __name__ == "__main__":
    test_merge_alternately()
    print("All tests for 1768 passed!")
