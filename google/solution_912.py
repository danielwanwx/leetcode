from typing import List

class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        # Start the quicksort process.
        self.sort(nums, 0, len(nums) - 1)
        return nums

    def sort(self, nums, start, end):
        # Base condition to end the recursion.
        if start >= end:
            return

        # Choosing the middle element as the pivot.
        pivot = nums[(start + end) // 2]
        left, right = start, end

        # Partitioning process.
        while left <= right:
            # Move left pointer until an element greater than the pivot is found.
            while nums[left] < pivot:
                left += 1
            # Move right pointer until an element less than the pivot is found.
            while nums[right] > pivot:
                right -= 1

            # Swap elements and move pointers if left pointer is not beyond right pointer.
            if left <= right:
                nums[left], nums[right] = nums[right], nums[left]
                left += 1
                right -= 1

        # Recursive calls to sort the two partitions.
        self.sort(nums, start, right)
        self.sort(nums, left, end)

'''
解决思路：

这段代码实现了快速排序算法，用于对整数数组进行排序。快速排序是一种高效的排序算法，采用了分治法的思想。其核心思路如下：

1. **递归分治**：
   - 快速排序通过递归的方式，将大问题分解为小问题来解决。它选择数组中的一个元素作为基准（pivot），然后将数组分为两个部分：一部分的元素小于基准，另一部分的元素大于基准。

2. **选择基准**：
   - 代码中选择数组中间的元素作为基准。这是为了减少在极端情况下（如已排序或逆序数组）的性能退化。

3. **分区操作**：
   - 算法通过两个指针，从数组的两端开始，向中间移动。左指针寻找大于等于基准的元素，右指针寻找小于等于基准的元素，然后交换这两个元素。这个过程持续进行，直到两个指针相遇。

4. **递归排序子数组**：
   - 一旦完成分区操作，基准左侧的所有元素都小于基准，右侧的所有元素都大于基准。然后对基准左右两侧的子数组递归地重复上述过程。

复杂度分析：
- **时间复杂度**：平均情况下为 `O(n log n)`，最坏情况（极端不平衡的分区）为 `O(n^2)`。但通常情况下，由于分区相对均衡，快速排序的表现接近 `O(n log n)`。
- **空间复杂度**：由于采用递归，空间复杂度取决于递归调用的深度，最坏情况下为 `O(n)`（极端不平衡的分区导致的递归深度），平均情况下为 `O(log n)`。

'''
