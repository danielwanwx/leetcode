import string
from collections import deque
from typing import List


class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        # Use BFS to find the shortest transformation sequence
        # First, convert the wordList to a set for efficient access
        word_set = set(wordList)

        # If the endWord is not in the wordList, return 0 as no transformation sequence exists
        if endWord not in word_set:
            return 0

        # Use a queue to perform BFS. Each element in the queue is a tuple (current word, current transformation step)
        queue = deque([(beginWord, 1)])

        # Continue the loop until the queue is empty
        while queue:
            # Pop the first element from the queue
            word, step = queue.popleft()

            # If the current word is the endWord, return the number of steps taken
            if word == endWord:
                return step

            # Iterate over all possible next words and add them to the queue
            for next_word in self.get_next_words(word, word_set):
                queue.append((next_word, step + 1))

        # If no transformation sequence is found, return 0
        return 0

    def get_next_words(self, word: str, word_set: set) -> List[str]:
        # Generate all possible next words that are in the word_set
        next_words = []

        # Iterate over each character in the word
        for i in range(len(word)):
            # Replace the i-th character with every letter from a to z
            for ch in string.ascii_lowercase:
                next_word = word[:i] + ch + word[i + 1:]

                # If the generated word is different from the original and is in the word set
                if next_word in word_set and next_word != word:
                    # Add this word to the list of next words
                    next_words.append(next_word)
                    # Remove the word from the set to prevent revisiting
                    word_set.remove(next_word)

        # Return the list of next words
        return next_words
# 思路流程解释：
"""
1. 初始化：将单词列表（wordList）转换为集合（word_set）以提高搜索效率。如果目标单词（endWord）不在集合中，说明无法转换，返回0。

2. 使用队列实现广度优先搜索（BFS）：
   a. 将起始单词（beginWord）及其转换步数（1）作为元组加入队列。
   b. 当队列不为空时，持续进行以下操作：
      i. 从队列中弹出一个元组（当前单词及其步数）。
      ii. 如果当前单词是目标单词，返回当前步数作为结果。
      iii. 否则，计算所有可能的下一个单词并将它们加入队列，步数加1。

3. 计算下一个单词：
   a. 遍历当前单词的每个字符。
   b. 尝试将该字符替换为英文字母表中的其他字母。
   c. 如果得到的新单词在单词集合中并且与原单词不同，将其加入到下一个单词的列表中，并从集合中移除，避免重复访问。

4. 如果队列处理完毕仍未找到目标单词，返回0，表示无法完成转换。
"""