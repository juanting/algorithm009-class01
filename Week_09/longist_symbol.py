class Solution:
    def longestValidParentheses(self, s: str) -> int:
        res, stack = 0, [-1]
        for i in range(len(s)):
            if s[i] =='(':
                stack.append(i)
            else:
                if len(stack)>1:
                    stack.pop()
                    res = max(res, i-stack[-1])
                else:
                    stack[0] = i
        return res