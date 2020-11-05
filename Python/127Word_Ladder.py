from typing import List
from collections import deque

class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        word_set = set(wordList)

        if endWord not in word_set:
            return 0
        if beginWord in word_set:
            word_set.remove(beginWord)

        queue = deque()  # BFS need
        queue.append(beginWord)

        visited = set()  # record visited words

        word_len = len(beginWord)
        step = 1  # include beginWord

        while queue:
            current_size = len(queue)
            for i in range(current_size):
                word = queue.popleft()

                word_list = list(word)

                for j in range(word_len):
                    origin_char = word_list[j]

                    for k in range(26):
                        word_list[j] = chr(ord('a') + k)

                        next_word = str(word_list)

                        if next_word in word_set:
                            if next_word == endWord:
                                return step+1

                            if next_word not in visited:
                                queue.append(next_word)
                                visited.add(next_word)
                    word_list[j] = origin_char
            step += 1
        return 0
