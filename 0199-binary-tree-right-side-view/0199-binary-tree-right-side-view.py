# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def rightSideView(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[int]
        """
        if not root:
            return []
        ans = []
        queue = deque([root])

        while queue:
            levelSize = len(queue)
            currentLevelValue = []

            for _ in range (levelSize):
                node = queue.popleft()
                currentLevelValue.append(node.val)

                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            ans.append(currentLevelValue[-1])
        return ans

        
        