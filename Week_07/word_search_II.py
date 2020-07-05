# 给定一个二维网格 board 和一个字典中的单词列表 words，找出所有同时在二维网格和字典中出现的单词。 
# 
#  单词必须按照字母顺序，通过相邻的单元格内的字母构成，其中“相邻”单元格是那些水平相邻或垂直相邻的单元格。同一个单元格内的字母在一个单词中不允许被重复使用。
#  
# 
#  示例: 
# 
#  输入: 
# words = ["oath","pea","eat","rain"] and board =
# [
#   ['o','a','a','n'],
#   ['e','t','a','e'],
#   ['i','h','k','r'],
#   ['i','f','l','v']
# ]
# 
# 输出: ["eat","oath"] 
# 
#  说明: 
# 你可以假设所有输入都由小写字母 a-z 组成。 
# 
#  提示: 
# 
#  
#  你需要优化回溯算法以通过更大数据量的测试。你能否早点停止回溯？ 
#  如果当前单词不存在于所有单词的前缀中，则可以立即停止回溯。什么样的数据结构可以有效地执行这样的操作？散列表是否可行？为什么？ 前缀树如何？如果你想学习如何
# 实现一个基本的前缀树，请先查看这个问题： 实现Trie（前缀树）。 
#  
#  Related Topics 字典树 回溯算法

from typing import List
class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        if not board or not board[0] or not words: return []
        res, m, n, worddict, end_flag = set(), len(board), len(board[0]), {}, '#'
        dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]
        # 1.构建字典树
        for word in words:
            node = worddict
            for char in word:
                node = node.setdefault(char, {})
            node[end_flag] = '#'

        # 2.dfs遍历
        def _dfs(i, j, cur_word, cur_dic):
            cur_word += board[i][j]
            cur_dic = cur_dic[board[i][j]]
            if end_flag in cur_dic:
                res.add(cur_word)
            tmp, board[i][j] = board[i][j], '@'
            for k in range(4):
                nx, ny = i + dx[k], j + dy[k]
                if 0 <= nx < m and 0 <= ny < n and board[nx][ny] in cur_dic and board[nx][ny] != '@':
                    _dfs(nx, ny, cur_word, cur_dic)
            board[i][j] = tmp

        for i in range(m):
            for j in range(n):
                if board[i][j] in worddict:
                    _dfs(i, j, "", worddict)
        return list(res)