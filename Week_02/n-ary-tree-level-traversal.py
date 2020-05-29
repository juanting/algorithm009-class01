"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""
#BFS解决

class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        if not root: return []
        stack, res = [root], []
        while stack:
            cur_len, tmp = len(stack), []
            for i in range(cur_len):
                node = stack.pop(0)
                tmp.append(node.val)
                stack.extend(node.children)
            res.append(tmp)
        return res