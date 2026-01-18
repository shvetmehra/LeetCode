# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution(object):
    def levelOrderBottom(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[List[int]]
        """
        if not root:
            return []
        
        ans = []
        queue = deque([root])

        while queue:
            levelSize = len(queue)
            currentLevelValue =[]

            for _ in range(levelSize):
                node = queue.popleft()
                currentLevelValue.append(node.val)

                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            ans.append(currentLevelValue)
        ans.reverse()
        return ans
