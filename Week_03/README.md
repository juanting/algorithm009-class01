### 学习笔记-递归、回溯、分治
代码重点：在递归时，当在用回溯时，即在改变了参数的值，在递归之后又要撤销选择，这个时候添加的路径要进行复制，即用tmp[:]，否则python默认传值引用，会在tmp改变的过程中将结果改变；
如果时在下沉时直接改变传入的参数，则不需要[:] ！
 
本质上来说递归、回溯、分治是同一个套路，在递归中需要注意的是递归四件套：终止条件、处理当前层、下沉以及恢复现场。泛型递归模板代码如下：
```
def recursion(level, param1, param2, ...): 
    # recursion terminator 
    if level > MAX_LEVEL: 
	   process_result 
	   return 

    # process logic in current level 
    process(level, data...) 

    # drill down 
    self.recursion(level + 1, p1, ...) 

    # reverse the current level status if needed
```

回溯的思想是在做错选择时可以恢复到上一层，然后继续选择，在递归的基础上，回溯的模板如下：
```
result = []
def backtrack(路径, 选择列表):
    if 满足结束条件:
        result.add(路径)
        return
    
    for 选择 in 选择列表:
        做选择
        backtrack(路径, 选择列表)
        撤销选择
```
分治则时在处理当前节点时需要将问题划分为若干个子问题，然后再合并。分治的模板如下：
```Python
def divide_conquer(problem, param1, param2, ...):
  # recursion terminator 
  if problem is None: 
	print_result 
	return 
  # prepare data 
  data = prepare_data(problem) 
  subproblems = split_problem(problem, data) 
  # conquer subproblems 
  subresult1 = self.divide_conquer(subproblems[0], p1, ...) 
  subresult2 = self.divide_conquer(subproblems[1], p1, ...) 
  subresult3 = self.divide_conquer(subproblems[2], p1, ...) 
  …
  # process and generate the final result 
  result = process_result(subresult1, subresult2, subresult3, …)
	
  # revert the current level states

```