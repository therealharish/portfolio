# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def longestZigZag(self, root: Optional[TreeNode]) -> int:

        def f1(root):
            
            if not root:
                return 0
            return max(f1(root.left), f1(root.right), f2(root, 'L'), f2(root, 'R'))
        
        
        dp = {}
        def f2(node, dir):
            if (node, dir) in dp:
                return dp[(node, dir)]
            if not node:
                return 0
            if dir == "L":
                dp[(node, dir)] = 1 + f2(node.right, "R")
                return dp[(node, dir)]
            else:
                dp[(node, dir)] = 1 + f2(node.left, "L")
                return dp[(node, dir)]

        return f1(root)-1
        
                    

