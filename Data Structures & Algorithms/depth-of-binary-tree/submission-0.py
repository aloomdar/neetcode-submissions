# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        # DFS
        # I create a stack and initialize it with the root, and the level of the tree we are at
        stack = [[root, 1]]
        res = 0

        # Create a while loop that runs while stack is not empty
        while stack:
            # pop the node in the stack. node, depth will return the child/root and the level
            node, depth = stack.pop()

            # check if the node we are looking at is null or not
            # if the node is null, then it wont run
            if node:
                # if the node is not null, then we can set the res to the max of the res, and the depth
                res = max(res, depth)
                # if the node is not null, then we add the left and right child of the node to the stack
                # I add 1 to the depth because I am going one level lower into the tree
                # append the children as a list so that they stay as pairs
                stack.append([node.left, depth + 1])
                stack.append([node.right, depth + 1])
        
        return res