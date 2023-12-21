# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        
        def diameter(root):
            if not root:
                return 0
            left_height = height(root.left)
            right_height = height(root.right)
            left_diameter = diameter(root.left)
            right_diameter = diameter(root.right)
            return max(left_height+right_height, max(left_diameter,right_diameter))

        def height(root):
            if root is None:
                return 0
            return max(height(root.left), height(root.right))+1
        return diameter(root)