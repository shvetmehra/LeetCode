# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def longestZigZag(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        self.maxLength = 0
        def dfs(node, direction, length):
            if node == None:
                return
            self.maxLength = max(self.maxLength, length)
            if direction == 1:
                dfs(node.left, 0, length+1)
                dfs(node.right, 1, 1)
            else:
                dfs(node.right, 1, length+1)
                dfs(node.left, 0, 1)
        dfs(root.left, 0, 1)
        dfs(root.right, 1,1)
        return self.maxLength 