from typing import List


class Solution:
    def canJump(self, nums: List[int]) -> bool:
        max_reach = 0  # 初始化最远可达的位置为0
        for i, jump in enumerate(nums):  # 遍历数组，i是索引，jump是当前位置的跳跃能力
            if i > max_reach:  # 如果当前位置超过了之前能达到的最远位置，返回False
                return False
            max_reach = max(max_reach, i + jump)  # 更新最远可达的位置
        return max_reach >= len(nums) - 1  # 如果最远可达位置大于等于数组最后一个元素的位置，则返回True

'''
首先，函数canJump接受一个整数列表nums作为参数。
max_reach变量用来记录在遍历数组过程中所能达到的最远位置。
在循环中，enumerate(nums)用于获取每个元素及其索引。
如果当前索引i大于max_reach，意味着无法到达当前位置，因此返回False。
使用max(max_reach, i + jump)更新max_reach。这里i + jump表示如果从当前位置跳跃，能到达的最远位置。
最后，如果max_reach大于等于数组的最后一个位置，则表示可以跳到最后，返回True。
'''