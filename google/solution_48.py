from typing import List


class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        N = len(matrix)
        for i in range(N):
            for j in range(i):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

        for i in range(N):
            for j in range(N // 2):
                matrix[i][j], matrix[i][N - j - 1] = matrix[i][N - j - 1], matrix[i][j]
'''
这个问题的核心任务是将一个 n×n 的二维矩阵顺时针旋转 90 度。这个任务可以通过两个主要步骤来实现：

矩阵转置：这个步骤涉及将矩阵的行和列互换。在转置过程中，你会将位于第 i 行第 j 列的元素移动到第 j 行第 i 列。这一步完成后，原始矩阵的列变成了新矩阵的行，但元素的顺序还需要调整。

水平翻转每行：在转置之后，矩阵的每一行都是逆序的（即第一个元素应该是最后一个，反之亦然）。为了得到顺时针旋转 90 度的效果，我们需要将每一行的元素顺序翻转。这意味着对于每一行，第一个元素和最后一个元素交换，第二个元素和倒数第二个元素交换，以此类推，直到到达行的中间。

在这个过程中，我们实际上是在两个维度上操作矩阵：首先是通过转置在“对角线”上操作，然后通过水平翻转在“水平中线”上操作。这两步结合在一起，就实现了矩阵的顺时针旋转 90 度。
'''