class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        #bfs
        wordset = set(wordList)
        queue, count = [(beginWord, 1)], 0
        char = "abcdefghijklmnopqrstuvwxyz"
        while queue:
            cur, count = queue.pop(0)
            if cur == endWord: return count
            for i in range(len(cur)):
                for c in char:
                    new = cur[:i]+ c + cur[i+1:]
                    if new in wordset:
                        wordset.remove(new)
                        queue.append((new, count+1))
        return 0