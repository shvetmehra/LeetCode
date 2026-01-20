# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def deleteNode(self, root, key):
        """
        :type root: Optional[TreeNode]
        :type key: int
        :rtype: Optional[TreeNode]
        """
        if root == None:
            return None
        #case A when root is greater than key.

        if key<root.val:
            root.left = self.deleteNode(root.left, key)
        #Case B when root is lesser than Key:
        elif key>root.val:
            root.right = self.deleteNode(root.right, key)
        # Case C when root == key:
        else:
            # 1. when left subtree and right subtree as no value.
            if root.left == None and root.right == None:
                return None
            #2. when left Subtree is None:
            elif root.left == None:
                return root.right
            #3 when right Subtree is None:
            elif root.right == None:
                return root.left
            # Most Important = when we have subtree on both the sides: We will go with 'In Order Succession"
            else:
                temp = root.right
                while temp.left != None:
                    temp = temp.left
                root.val = temp.val
                root.right = self.deleteNode(root.right, temp.val)
        return root
        