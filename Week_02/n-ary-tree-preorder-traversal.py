"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def preorder(self, root: 'Node') -> List[int]:
        if not root: return []
        stack, res = [root], []
        while stack:
            node = stack.pop()
            res.append(node.val)
            stack.extend(node.children[::-1])
        return res


#递归
class Solution:
    def preorder(self, root: 'Node') -> List[int]:
        if not root: return []
        res = []
        def helper(root):
            res.append(root.val)
            for child in root.children:
                helper(child)
        helper(root)
        return res