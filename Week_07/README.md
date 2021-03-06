# 1.前缀树知识点
Trie树的核心思想是空间换时间，利用字符串的公共前缀来减少无谓的字符串比较以达到提高查询效率的目的。

优点：
1.插入和查询的效率很高，都为O(m)，其中m是待插入/查询的字符串的长度。
	关于查询，会有人说hash表时间复杂度是O(1)O(1)不是更快？但是，哈希搜索的效率通常取决于 hash 函数的好坏，若一个坏的 hash 函数导致很多的冲突，效率并不一定比Trie树高。
2.Trie树中不同的关键字不会产生冲突。
3.Trie树只有在允许一个关键字关联多个值的情况下才有类似hash碰撞发生。
4.Trie树不用求 hash 值，对短字符串有更快的速度。通常，求hash值也是需要遍历字符串的。
5.Trie树可以对关键字按字典序排序。

缺点：
1.当hash函数很好时，Trie树的查找效率会低于哈希搜索。
2.空间消耗比较大。

