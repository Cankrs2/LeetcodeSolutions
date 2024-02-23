# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        que = []
        que.append(root)
        len_que=0
        result = []
        
        while len(que) != 0:
            level = []
            len_que = len(que)
            for i in range(len_que):
                node = que.pop(0)
                if node:
                    level.append(node.val)
                    que.append(node.left)
                    que.append(node.right)
            if level:
                result.append(level)    
        return result
            