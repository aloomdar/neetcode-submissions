# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        # I check the root to see if it exists, if it doesn't then return None
        if not root:
            return None

        # I store the left child in a temp variable
        # Then I set the left child to the right child and 
        # the right to the left which is stored in temp
        temp = root.left
        root.left = root.right
        root.right = temp

        # Once I'm done swapping the roots, I recursively call the function on both children and return root
        self.invertTree(root.left)
        self.invertTree(root.right)
        return root
        