# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def max_height(root):
            if not root:
                return 0
        
            left_depth = max_height(root.left)
            right_depth = max_height(root.right)

            if abs(left_depth - right_depth) > 1:
                return -1

            return max(left_depth, right_depth) + 1
            
        return max_height(root) != -1