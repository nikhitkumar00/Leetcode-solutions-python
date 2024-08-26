"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def postorder(self, root: 'Node') -> List[int]:
        out = []

        def dfs(node):
            if node:
                for i in node.children:
                    dfs(i)
                out.append(node.val)
        
        dfs(root)
        return out