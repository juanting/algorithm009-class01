## 本周要点
本周主要学习的内容有哈希表、树、堆。树的内容中主要是前中后序遍历内容；堆在面试中可以解决最大k个元素等问题，可以调用heapq模块进行实现。接下来着重对树的三个遍历的栈实现进行总结。
### 二叉树的前中后序遍历（栈的方式实现）
二叉树因其特殊结构，一般用递归实现遍历会十分方便，但是为了更加全面完整的理解二叉树的遍历，对前中后序用一个模板实现栈的维护来遍历。

#### 前序遍历
前序遍历即在遍历根节点时第一次遇到就将其压入栈中并输出节点的值，然后所有左子树依次进栈，直到最底端左子树遍历完，将最后一个节点弹出并遍历其右子树。代码实现如下：
```
class Solution:
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        res, stack = [], []
        node = root
        while node or stack:
            while node:
                res.append(node.val)
                stack.append(node)
                node = node.left
            node = stack.pop()
            node = node.right
        return res
```

#### 中序遍历
中序遍历与前序遍历类似，只是在遇到根节点时第一次遇到压入栈中，第二次遇到弹出并打印只需要修改前序遍历的打印节点位置即可。
```
class Solution:
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        res, stack = [], []
        node = root
        while node or stack:
            while node:
                stack.append(node)
                node = node.left
            node = stack.pop()
            res.append(node.val)
            node = node.right
        return res
```

#### 后序遍历
后序遍历的与上述模板一致的写法为，将前序遍历的代码稍作改动，需要每次将右子树全部入栈，然后再把左子树全部入栈，得出遍历的结果为根-右-左的顺序，然后再将这个遍历的结果翻转即可得到左-右-根的遍历序列。

```
class Solution:
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        res, stack = [], []
        node = root
        while node or stack:
            while node:
                res.append(node.val)
                stack.append(node)
                node = node.left
            node = stack.pop()
            node = node.right
        return res[::-1]
```

上述遍历只是将遍历的序列翻转，不够正规，后续遍历的正宗的写法为维护两个栈其中一个弹出顺序是根右左，第二个栈的弹出顺序是左右根，然后得到序列。
```
class Solution:
    def postorderTraversal(self, root: TreeNode) -> List[int]:
        if not root: return []
        stack1, stack2, res = [root], [], []
        while stack1:
            node = stack1.pop()
            stack2.append(node)
            if node.left:
                stack1.append(node.left)
            if node.right:
                stack1.append(node.right)
        while(stack2):
            res.append(stack2.pop().val)
        return res

```