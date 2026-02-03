# from collections import deque
# class Solution(object):
#     def findLadders(self, beginWord, endWord, wordList):
#         """
#         :type beginWord: str
#         :type endWord: str
#         :type wordList: List[str]
#         :rtype: List[List[str]]
#         """
#         wordset = set(wordList)
#         if endWord not in wordset:
#             return []
#         result = []
#         queue = deque()
#         queue.append([beginWord])

#         while len(queue)!=0:
#             levelSize = len(queue)
#             chosenWord = set()

#             for _ in range(levelSize):
#                 sequence = queue.popleft()
#                 lastWord = sequence[-1]
#                 if lastWord == endWord:
#                     result.append(sequence)
#                     found = True
#                     continue
#                 for i in range (len(lastWord)):
#                     for ch in 'abcdefghijklmnopqrstuvwxyz':
#                         if ch == lastWord[i]:
#                             continue
#                         newWord = lastWord[:i]+ch+lastWord[i+1:]
#                         if newWord in wordset:
#                             newSeq = sequence + [newWord]
#                             queue.append(newSeq)
#                             chosenWord.add(newWord)
#             for word in chosenWord:
#                 wordset.remove(word)
#         return result
from collections import deque, defaultdict
import string

class Solution(object):
    def findLadders(self, beginWord, endWord, wordList):
        wordset = set(wordList)
        if endWord not in wordset:
            return []
        
        # word -> [list of parents that reach it in the shortest steps]
        preds = defaultdict(list)
        # word -> shortest distance from beginWord
        dist = {beginWord: 0}
        queue = deque([beginWord])
        found = False
        
        while queue and not found:
            level_visited = {}
            for _ in range(len(queue)):
                curr = queue.popleft()
                
                for i in range(len(curr)):
                    for ch in string.ascii_lowercase:
                        if ch == curr[i]: continue
                        next_word = curr[:i] + ch + curr[i+1:]
                        
                        if next_word in wordset:
                            # If we haven't seen this word or it's at the same level
                            if next_word not in dist or dist[next_word] == dist[curr] + 1:
                                if next_word not in dist:
                                    dist[next_word] = dist[curr] + 1
                                    queue.append(next_word)
                                preds[next_word].append(curr)
                                if next_word == endWord:
                                    found = True
            
        # Backtracking to build paths from endWord to beginWord
        results = []
        def backtrack(curr_word, path):
            if curr_word == beginWord:
                results.append(path[::-1])
                return
            for p in preds[curr_word]:
                backtrack(p, path + [p])
                
        if found:
            backtrack(endWord, [endWord])
        return results