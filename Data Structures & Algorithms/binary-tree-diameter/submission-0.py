# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        # For each tree recursively called on,
        # determine the max between right and left length 
        # add right and left length to get diameter, and store it in a class member
        # return the max betwee L and R length.
        self.diam = 0
        curr = root
        def recurs(tree):
            if tree==None:
                return 0
            left=recurs(tree.left)
            right=recurs(tree.right)
            if left+right > self.diam:
                self.diam = left+right
            return max(left, right)+1
        recurs(curr)
        return self.diam
