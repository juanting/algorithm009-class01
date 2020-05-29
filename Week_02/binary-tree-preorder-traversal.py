# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        res, stack = [], []
        node = root
        while node or stack:
            while node:
                stack.append(node)
                res.append(node.val)
                node = node.right
            node = stack.pop()
            node = node.left
        return res[::-1]



class Solution:
    def preorderTraversal2(self, root: TreeNode) -> List[int]:
        res, stack = [], []
        node = root
        while node or stack:
            while node:
                stack.append(node)
                res.append(node.val)
                node = node.left
            node = stack.pop()
            node = node.right
        return res