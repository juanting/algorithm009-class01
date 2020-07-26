class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        '''
        if not strs: return ""
        for i in range(len(strs[0])):
            for j in range(1, len(strs)):
                if i<len(strs[j]) and strs[0][i] == strs[j][i]:
                    pass
                else:
                    return strs[0][:i]
        return strs[0]
        '''
        if not strs: return ""
        str0 = min(strs)
        str1 = max(strs)
        for i in range(len(str0)):
            if str0[i] != str1[i]:
                return str0[:i]
        return str0