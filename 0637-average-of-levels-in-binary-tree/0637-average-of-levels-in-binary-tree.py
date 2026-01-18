# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution(object):
    def averageOfLevels(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[float]
        """
        if not root:
            return []

        ans = []
        queue = deque([root])

        while queue:
            levelSize = len(queue)
            currentLevelValue = 0.0

            for _ in range(levelSize):
                node = queue.popleft()
                currentLevelValue += node.val

                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            ans.append(currentLevelValue/levelSize)
        return ans        