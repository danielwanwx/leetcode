from solution_127 import Solution  # Adjust the import statement based on your file name and structure

def test_ladderLength():
    solution = Solution()
    # Assuming your solution.ladderLength method takes beginWord, endWord, and wordList as arguments
    assert solution.ladderLength("hit", "cog", ["hot", "dot", "dog", "lot", "log", "cog"]) == 5, "Error in test case 1"
    assert solution.ladderLength("hit", "cog", ["hot", "dot", "dog", "lot", "log"]) == 0, "Error in test case 2"
    # Add more test cases as needed

# Run the test function
if __name__ == "__main__":
    test_ladderLength()
    print("All tests passed!")

