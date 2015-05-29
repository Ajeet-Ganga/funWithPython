# https://leetcode.com/problems/maximum-depth-of-binary-tree/

from collections import *
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

'''
    Recursive solution
'''
# class Solution:
#     # @param {TreeNode} root
#     # @return {integer}

#     def maxDepth(self, root):


#         if root is None:
#             return 0
#         return max(1+self.maxDepth(root.left),1+self.maxDepth(root.right))

'''
    Iterative solution
'''
class Solution:
    # @param {TreeNode} root
    # @return {integer}

    def maxDepth(self, root):
        if root is None:
            return 0

        q1 = deque()
        q1.append(root)
        q2 = deque()
        height = 0

        while len(q1) != 0 or len(q2) != 0:
            nonNullItemAdded = False
            if len(q1) != 0:
                for e in [e1 for e1 in q1 if e1 is not None]:
                    nonNullItemAdded = True
                    q2.append(e.left)
                    q2.append(e.right)
                q1 = deque()
            else:
                for e in [e1 for e1 in q2 if e1 is not None]:
                    nonNullItemAdded = True
                    q1.append(e.left)
                    q1.append(e.right)
                q2 = deque()
            if nonNullItemAdded:
                height += 1
        return height






