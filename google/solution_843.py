from collections import deque
from typing import List

class Solution:
    def shortestPathLength(self, graph: List[List[int]]) -> int:
        N = len(graph)  # Number of nodes in the graph
        visited = set()  # Set to track visited (node, state) pairs
        queue = deque()  # Queue for BFS
        final_state = (1 << N) - 1  # Final state where all nodes are visited

        # Initialize: Add each node with its initial state to the queue
        for i in range(N):
            state = 1 << i  # State with only the i-th node visited
            queue.append((i, state))  # Add (node, state) pair to the queue
            visited.add((i, state))  # Mark (node, state) pair as visited

        steps = 0  # Steps counter to track the number of iterations
        while queue:
            size = len(queue)
            # Process nodes level by level
            for _ in range(size):
                node, state = queue.popleft()  # Dequeue a (node, state) pair
                if state == final_state:
                    return steps  # Return steps if all nodes are visited

                # Explore all adjacent nodes
                for next_node in graph[node]:
                    next_state = 1 << next_node | state  # Update the state to include the next_node
                    # Check if the new state is not visited
                    if (next_node, next_state) not in visited:
                        visited.add((next_node, next_state))  # Mark as visited
                        queue.append((next_node, next_state))  # Enqueue the new state

            steps += 1  # Increment steps after processing each level
        return -1  # Return -1 if it's not possible to visit all nodes

'''
给定一个无向图，需要找到访问所有节点的最短路径长度，每个节点至少被访问一次。

解题思路
位掩码表示状态：使用位掩码来跟踪每个节点的访问状态。例如，如果有 N 个节点，则一个长度为 N 的二进制数的每一位可以表示一个节点是否被访问过。

广度优先搜索（BFS）：使用队列实现 BFS。队列中的每个元素包含当前节点和一个表示已访问节点的状态。

状态和节点的组合：在队列中存储 (节点, 状态) 对。状态是一个整数，表示哪些节点已被访问。

避免重复访问：使用集合来记录已访问的 (节点, 状态) 对，以避免重复处理相同状态。

最终状态：当达到状态 finalState（所有节点都被访问过）时，返回当前步数。

每个节点作为起点：初始时，从图中的每个节点开始，因为最短路径可以从任意节点开始。

时间复杂度
时间复杂度为 O(N * 2^N)，其中 N 是节点的数量。每个节点都有 2^N 种不同的状态（因为每个节点可以被访问或未被访问），而对于每个状态，我们需要执行一定数量的操作来遍历所有相邻节点。
空间复杂度
空间复杂度也是 O(N * 2^N)，主要用于存储已访问的状态和节点对。队列和访问集合的大小都由此决定。
这种解法在处理大图时可能会有较高的时间和空间消耗，但它是解决此类问题的有效方法，尤其是当需要考虑图中所有可能的路径时。
'''