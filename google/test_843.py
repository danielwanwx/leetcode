from solution_843 import Solution

def test_shortest_path_length():
    solution = Solution()

    # Test cases for the shortest path length problem
    assert solution.shortestPathLength([[1,2,3],[0],[0],[0]]) == 4, "Error in test case 1"
    assert solution.shortestPathLength([[1],[0,2,4],[1,3,4],[2],[1,2]]) == 4, "Error in test case 2"

# Run the test function
if __name__ == "__main__":
    test_shortest_path_length()
    print("All tests for shortest path length passed!")
