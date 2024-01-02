import sys
sys.setrecursionlimit(999999)
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def maxDepth(self, root):
        return postorder(root)
    
def postorder(root):
    if root is None:
        return 0
    left_depth = postorder(root.left)
    right_depth = postorder(root.right)
    return max(left_depth, right_depth) + 1
        
