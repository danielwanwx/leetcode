from typing import List

class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        本函数不返回任何内容，而是直接在原地修改数组 nums。
        """
        # 初始化两个指针 i 和 j，都指向数组的最后一个元素
        i = j = len(nums) - 1

        # 从数组的倒数第二个元素开始向前遍历，直到找到一个元素比其前一个元素小
        while i > 0 and nums[i] <= nums[i - 1]:
            i -= 1

        # 如果遍历完都没有找到，即整个数组都是降序排列的，
        # 这时候我们只需要将整个数组反转成升序排列即可
        if i == 0:
            nums.reverse()
            return

        # 再次使用 j 指针，从数组的最后一个元素向前遍历，
        # 直到找到一个元素大于 nums[i - 1] 的元素
        while nums[j] <= nums[i - 1]:
            j -= 1

        # 交换 nums[i - 1] 和 nums[j]
        nums[i - 1], nums[j] = nums[j], nums[i - 1]

        # 将 nums[i:] 进行反转，使其成为升序排列
        nums[i:] = nums[i:][::-1]

# 具体思路：
# 1. 从后向前查找第一个相邻元素对 (i-1, i)，满足 nums[i] > nums[i-1]。
#    这样 nums[i:] 必定是降序排列。
# 2. 如果找不到这样的相邻元素对，说明整个数组已经是完全降序排列，
#    直接将整个数组反转成升序排列。
# 3. 如果找到了这样的相邻元素对，再从数组末尾开始向前找到第一个大于 nums[i-1] 的元素 nums[j]。
# 4. 交换 nums[i-1] 和 nums[j]，然后将 nums[i:] 反转成升序排列。
# 5. 这样得到的新排列就是比原排列大的下一个排列。
