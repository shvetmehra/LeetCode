# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def goodNodes(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.good = 0
        def dfs(node, check):
            if not node:
                return 
            if node.val >= check:
                self.good +=1
                check = node.val
            dfs(node.left, check)
            dfs(node.right, check)
        dfs(root, root.val)
        return self.good