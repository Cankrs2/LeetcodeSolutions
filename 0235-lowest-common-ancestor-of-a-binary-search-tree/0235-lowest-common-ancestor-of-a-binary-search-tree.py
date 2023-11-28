# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        counter1 = 0
        counter2 = 0
        current = root
        stack1=[]
        stack2=[]
        while current != None:
            stack1.append(current)
            counter1+=1
            if p.val > current.val:
                current = current.right
            elif p.val < current.val:
                current= current.left
            else: 
                break
        current = root
        while current != None:
            stack2.append(current)
            counter2 +=1
            if q.val > current.val:
                current = current.right
            elif q.val < current.val:
                current= current.left
            else: 
                break
        while(counter2 != counter1):
            if counter2 >counter1:
                stack2.pop()
                counter2 -=1
            else: 
                stack1.pop()
                counter1-=1
        while(stack1 !=[]):
            x,y=stack1.pop(),stack2.pop()
            if x.val==y.val:
                return x
            