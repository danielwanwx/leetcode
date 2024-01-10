from solution_912 import Solution  # Adjust the import based on your file name and structure

def test_sort_array():
    solution = Solution()
    assert solution.sortArray([-1, 0, 1, 2, -1, -4]) == [-4, -1, -1, 0, 1, 2], "Error in test case 1"
    assert solution.sortArray([0, 0, 0]) == [0, 0, 0], "Error in test case 2"
    assert solution.sortArray([]) == [], "Error in test case 3"
    # Add more test cases as needed

# Run the test function
if __name__ == "__main__":
    test_sort_array()
    print("All tests for 1768 passed!")
