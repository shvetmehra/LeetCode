from collections import deque
class Solution(object):
    def ladderLength(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: int
        """
        wordset = set(wordList)
        if endWord not in wordset:
            return 0
        queue = deque()
        queue.append((beginWord, 1))

        while len(queue)!= 0:
            currWord, level = queue.popleft()
            if currWord == endWord:
                return level
            for i in range (0, len(currWord)):
                for c in 'abcdefghijklmnopqrstuvwxyz':
                    if c== currWord[i]:
                        continue
                    newWord = currWord[:i]+c+currWord[i+1:]
                    if newWord in wordset:
                        queue.append((newWord, level+1))
                        wordset.remove(newWord)
        return 0
        