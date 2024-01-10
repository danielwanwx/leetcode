from typing import List

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()  # Sort the array to facilitate the two-pointer approach.
        result = []

        for i in range(len(nums) - 2):
            # Skip the same element to avoid duplicate triplets.
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            left, right = i + 1, len(nums) - 1  # Initialize two pointers.
            while left < right:
                sum = nums[i] + nums[left] + nums[right]
                if sum < 0:
                    left += 1  # Move the left pointer to increase the sum.
                elif sum > 0:
                    right -= 1  # Move the right pointer to decrease the sum.
                else:
                    # Found a triplet, add it to the result.
                    result.append([nums[i], nums[left], nums[right]])
                    left += 1
                    right -= 1
                    # Skip duplicate elements.
                    while left < right and nums[left] == nums[left - 1]:
                        left += 1
                    while left < right and nums[right] == nums[right + 1]:
                        right -= 1

        return result

# 中文思路详解
# 这个解决方案中，首先对数组进行排序，目的是为了使用双指针方法寻找三元组。
# 遍历数组中的每一个元素，使用两个指针left和right，分别从当前元素的下一个位置和数组的末尾开始。
# 如果三个数的和小于0，移动左指针以增加总和；如果大于0，移动右指针以减少总和。
# 当找到和为0的三元组时，将其加入结果中，并移动两个指针以继续寻找新的三元组。
# 为了避免重复的三元组，需要在发现重复元素时跳过这些元素。
# 这种方法的时间复杂度为O(n^2)，其中n是数组的长度。
