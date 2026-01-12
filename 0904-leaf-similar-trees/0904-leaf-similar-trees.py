# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def leafSimilar(self, root1, root2):
        """
        :type root1: Optional[TreeNode]
        :type root2: Optional[TreeNode]
        :rtype: bool
        """
        leaf1=[]
        leaf2=[]
        def getleaf(root, result):
            if root.left == None and root.right == None:
                result.append(root.val)
                result
            if root.left:
                getleaf(root.left, result)
            if root.right:
                getleaf(root.right, result)
            return
        getleaf(root1, leaf1)
        getleaf(root2, leaf2)
        return leaf1==leaf2