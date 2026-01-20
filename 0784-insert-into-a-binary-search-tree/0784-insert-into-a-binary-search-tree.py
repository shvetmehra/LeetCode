# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def insertIntoBST(self, root, val):
        """
        :type root: Optional[TreeNode]
        :type val: int
        :rtype: Optional[TreeNode]
        """
    
        if root == None:
            return TreeNode(val)

        curr = root
        while root:
            
            if val<curr.val:
                if curr.left!=None:
                    curr = curr.left
                else:
                    curr.left = TreeNode(val)
                    break
            else:
                if curr.right!=None:
                    curr = curr.right
                else:
                    curr.right = TreeNode(val)
                    break
        return root