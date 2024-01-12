from solution_31 import Solution


def test_next_permutation():
    solution = Solution()

    nums1 = [3, 1, 4]
    solution.nextPermutation(nums1)
    assert nums1 == [3, 4, 1], "Error in test case 1"

    nums2 = [5, 7, 4, 2, 1]
    solution.nextPermutation(nums2)
    assert nums2 == [7, 1, 2, 4, 5], "Error in test case 2"


# 运行测试函数
if __name__ == "__main__":
    test_next_permutation()
    print("All tests for 31 passed!")
