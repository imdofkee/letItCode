# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
import collections


class Solution(object):
    def invertTree(self, root):

        if not root:
            return None

        queque = collections.deque([root])

        while queque:
            node = queque.popleft()
            node.left, node.right = node.right, node.left
            if node.left:
                queque.append(node.left)
            if node.right:
                queque.append(node.right)
        return root
            
        