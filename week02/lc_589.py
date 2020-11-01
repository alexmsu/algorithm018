"""
# Definition for a Node.
class Node(object):
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution(object):
    def preorder(self, root):
        """
        :type root: Node
        :rtype: List[int]
        """
        
        def helper(node, res):
            if node:
                res.append(node.val)
                for child in node.children:
                    helper(child, res)
        
        res = []
        helper(root, res)
        return res