"""
# Definition for a Node.
class Node(object):
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""
from collections import deque
class Solution(object):
    def levelOrder(self, root):
        """
        :type root: Node
        :rtype: List[List[int]]
        """
        if not root: return []
        res = []
        q = deque()
        
        q.append(root)
        while q:
            n = len(q)
            res.append()
            while n > 0:
                n -= 1
                node = q.popleft()
                res[-1].append(node.val)
                for child in node.children:
                    q.append(child)
        
        return res