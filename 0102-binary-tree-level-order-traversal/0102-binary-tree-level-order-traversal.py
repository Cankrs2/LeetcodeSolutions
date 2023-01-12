# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root is None:
            return []
        que = [root]
        next_que = []
        level = []
        result = []
        while que != []:
            for root in que:
                level.append(root.val)
                if root.left is not None:
                    next_que.append(root.left)
                if root.right is not None:
                    next_que.append(root.right)
            result.append(level)
            que = next_que
            next_que = []
            level = []
        return result