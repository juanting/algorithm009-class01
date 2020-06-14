## 1.深度优先遍历以及广度优先遍历
深度优先遍历（DFS）是深度优先，其模板如下：用递归实现
```
visited = set() 
def dfs(node, visited):
    if node in visited: # terminator
    	# already visited 
    	return 
	visited.add(node)   #在图中十分重要！！
	# process current node here. 
	...
	for next_node in node.children(): 
		if next_node not in visited:
			#drill down 
			dfs(next_node, visited)  
```

广度优先遍历在计算图的最小距离中使用广泛，需要额外注意要标记已经访问过的节点，广度优先的模板如下：
```
# Python
def BFS(graph, start, end):
    visited = set()  #记录访问过的节点
	queue = [] 
	queue.append([start]) 
	while queue: 
		node = queue.pop() 
		visited.add(node)
		process(node) 
		nodes = generate_related_nodes(node) 
		queue.push(nodes)
	# other processing work 
	...
```
## 2.贪心算法
如果可以运用贪心算法，那么一般都是最优解，重点在于分析题目是否可以使用贪心算法，其特点为局部最优解的集合可以得到全局最优解，经典的题目有柠檬水找零、买卖股票、种花问题以及分发饼干等。

## 3.二分查找
可用二分查找的三大条件：单调、有边界、可以通过索引获取值。
二分查找的模板：
```

left, right = 0, len(array) - 1 
while left <= right: 
	  mid = (left + right) / 2 
	  if array[mid] == target: 
		    # find the target!! 
		    break or return result 
	  elif array[mid] < target: 
		    left = mid + 1    #当mid以及left不是整数时，直接赋值为mid
	  else: 
		    right = mid - 1
```

### 二分查找经典题目
使用二分查找，寻找一个半有序数组 [4, 5, 6, 7, 0, 1, 2] 中间无序的地方
解题思路：这道题目需要使用二分查找法，将条件稍微变化一下即可，当nums[mid] > nums[l], 说明无序的地方在mid+1到r之间，因此将左边界l向后移动为mid+1，否则说明无序在l到mid之间，将l赋值为mid，具体的实现代码如下：
``` python
class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums)-1
        while l<r:
            mid = (l+r)//2
            if nums[mid] > nums[r]:  #无序在后面
                l = mid+1
            else:
                r = mid
        return nums[r]
```
