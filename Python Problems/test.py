# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minCameraCover(self, root: Optional[TreeNode]) -> int:
        d1, d2, d3 = {}, {}, {}
        def f1(root):
            if root == None:
                return 0
            if not root.right and not root.left:
                return 1
            withCamera = 1 + f2(root.left) + f2(root.right)
            # now for the without camera case we check if both left and right are covered
            withLeft, withRight = float('inf'), float('inf')
            if root.left:
                withLeft = f3(root.left) + f1(root.right)
            if root.right:
                withRight = f3(root.right) + f1(root.left)
            withoutCamera = min(withLeft, withRight)
            return min(withCamera, withoutCamera)
    
        def f2(root):
            if not root:
                return 0
            if not root.right and not root.left:
                return 0
            withCamera = 1 + f2(root.left) + f2(root.right)
            # now for the without camera case we check if both left and right are covered
            withLeft, withRight = float('inf'), float('inf')
            if root.left:
                withLeft = f3(root.left)
            if root.right:
                withRight = f3(root.right)
            withoutCamera = min(withLeft, withRight)
            return min(withCamera, withoutCamera)
    
        def f3(root):
            return 1 + f2(root.left) + f2(root.right)
        
        return f1(root)