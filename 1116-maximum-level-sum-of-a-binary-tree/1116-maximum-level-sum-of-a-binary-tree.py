import collections
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def maxLevelSum(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        if not root:
            return 0
        queue = collections.deque([root])

        maxSum = float('-inf')
        currentLevel = 1
        maxLevel = 1

        while queue:
            levelSize = len(queue)
            currentLevelSum =0

            for _ in range(levelSize):
                node = queue.popleft()
                currentLevelSum += node.val

                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            
            if currentLevelSum > maxSum:
                maxSum=currentLevelSum
                maxLevel = currentLevel
            currentLevel+=1
        return maxLevel
        