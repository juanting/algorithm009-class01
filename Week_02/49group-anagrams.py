#排序O(nklogk)
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dict_group = {}
        for word in strs:
            key = tuple(sorted(word))
            dict_group[key] = dict_group.get(key, []) + [word]
        return list(dict_group.values()) 

#空间换时间 O(nk)
class Solution:
    def groupAnagrams2(self, strs: List[str]) -> List[List[str]]:
        dict_group = {}
        for word in strs:
            count = [0]*26
            for c in word:
                count[ord(c)-ord('a')] +=1
            dict_group[tuple(count)] = dict_group.get(tuple(count), []) + [word]
        return list(dict_group.values()) 