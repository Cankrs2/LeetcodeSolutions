# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if root == None: return []
        queue = []
        result = []
        queue.insert(0,root)
        while queue != []:
            level_size = len(queue)
            for i in range(level_size):
                p = queue.pop(-1)
                if i == level_size -1:
                    result.append(p.val)
                if p.left:
                    queue.insert(0,p.left)
                if p.right:
                    queue.insert(0,p.right)
        return result