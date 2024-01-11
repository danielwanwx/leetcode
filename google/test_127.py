from solution_127 import Solution

def test_ladderLength():
    solution = Solution()

    assert solution.ladderLength("hit", "cog", ["hot", "dot", "dog", "lot", "log", "cog"]) == 5, "Error in test case 1"
    assert solution.ladderLength("hit", "cog", ["hot", "dot", "dog", "lot", "log"]) == 0, "Error in test case 2"


# Run the test function
if __name__ == "__main__":
    test_ladderLength()
    print("All tests passed!")

