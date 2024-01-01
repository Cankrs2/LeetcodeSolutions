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
        result = []

        while len(que) != 0:
            level=[]
            lenQue = len(que)
            for i in range(lenQue):
                node = que.pop(0)
                if node:
                    level.append(node.val)
                    que.append(node.left)
                    que.append(node.right)
            if level:
                result.append(level)
        return result
                
            