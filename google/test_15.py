from solution_15 import Solution

def test_three_sum():
    solution = Solution()

    # Test cases
    assert sorted(solution.threeSum([-1, 0, 1, 2, -1, -4])) == sorted([[-1, -1, 2], [-1, 0, 1]]), "Test case 1 failed"
    assert sorted(solution.threeSum([])) == [], "Test case 2 failed"
    assert sorted(solution.threeSum([0])) == [], "Test case 3 failed"


# Run the test function
if __name__ == "__main__":
    test_three_sum()
    print("All tests for LeetCode 15 passed!")
