### 位运算常用操作

异或
x ^ 0 = x x ^ x = 0 x ^ ~0 = ~x x ^ ~x = ~0 a ^ b ^ c = a ^ (b ^ c) = (a ^ b) ^ c

交换 a b 的值
c = a ^ b b = a ^ c a = b ^ c

将 x 最右边的 n 位清零
x & (~0 << n)

获取 x 的第 n 位的值 1 或 0
(x >> n) & 1

获取 x 的第 n 位的值 整数
x & (1 << n)

将 x 的第 n 位置为 1
x | (1 << n)

将 x 的第 n 位置为 0
x & (~(1 << n))

将 x 的最高位至第 n 位（含）都置为 0
x & ((1 << n) - 1)

判断奇偶
x & 1 == 1 -- x % 2 == 1 x & 1 == 0 -- x % 2 == 0

除 2
x >> 1 -- x // 2

将 x 最低位的 1 置为 0
x &= x - 1

得到 x 最低位的 1
x & -x

### 排序算法

#### 一.各排序算法复杂度概述：
![各排序算法复杂度.png](https://upload-images.jianshu.io/upload_images/12950574-b21f96c3156744d0.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)

*备注:* 

稳定：如果a原本在b前面，而a=b，排序之后a仍然在b的前面；
不稳定：如果a原本在b的前面，而a=b，排序之后a可能会出现在b的后面；

内排序：所有排序操作都在内存中完成；
外排序：由于数据太大，因此把数据放在磁盘中，而排序通过磁盘和内存的数据传输才能进行；

时间复杂度： 一个算法执行所耗费的时间。 空间复杂度：运行完一个程序所需内存的大小。

**希尔排序是插入排序的升级版，堆排序是简单选择排序的升级版，快速排序是冒泡排序的升级版**

**1.冒泡排序：**
共遍历n-1趟，每趟相邻两两元素相比，大的or小的后沉。
例：第一趟：相邻两个元素相比，大的往后沉，遍历完后最后一个元素最大；
                      第二趟：相邻两个元素相比，大的后沉，最后一个不用比，以此类推。
  **改进：**如果一趟中遍历完所有元素都没有进行交换顺序，则停止遍历，完成排序。          

代码实现：
```
# 冒泡排序
def bubble_sort(array):
    for i in range(len(array)-1): #外层循环控制遍历次数，共需要n-1次
        count = 0
        for j in range(len(array)-i-1): #控制每次的交换次数，n-1-i次
            if array[j] > array[j+1]:
                array[j],array[j+1] = array[j+1],array[j]
                count += 1
        if count ==0:             # 改进：如果在一次遍历后没有进行交换，说明已经有序
            break
#测试
a=[1,2,5,4,6,9,8,5,6]
bubble_sort(a)
print(a)
#out  [1, 2, 4, 5, 5, 6, 6, 8, 9]
```
**2.选择排序**
每次从待排序的数据元素中选出最小(最大)的元素，放到序列起始的位置直至排完。

代码实现：
```
#选择排序
def select_sort(array):
	for i in range(len(array)-1): #遍历n-1次
		min = i                   #每次遍历中的第一个元素
		for j in range(i+1, len(array)):
			if array[j] < array[min]:
				min = j           #找出当前最小的元素
		array[i], array[min] = array[min], array[i] #将最小的元素放到遍历的第一个元素位置去

a=[1,2,5,4,6,9,8,5,1,10]
#b = bubble_sort(a)
bubble_sort(a)
print(a)
# out [1, 1, 2, 4, 5, 5, 6, 8, 9, 10]
```
备注：选择排序不稳定，即相同两个值的元素排序之后的相对位置有可能会改变，如上述代码中的两个'5'在遍历过程中，第一个 '5'会到原始列表得'1'位置，最终排序后的结果这两个'5'的相对顺序会发生改变，因此说选择排序不稳定。

3.插入排序
列表被分为有序区和无序区，最初有序区只有一个元素，依次从无序区选择一个元素插入到有序区的适当位置，直到无序区变空。(类似于摸牌)

代码实现：
```
# 插入排序
def insert_sort(array):
	for i in range(1,len(array)): # 待摸的牌是从第二个到最后一个
		min = array[i]            # 待插入的数(摸上来的牌)
		j = i - 1				  #从i前面的一个元素开始比较
		while j >= 0 and array[j] > min:  #从有序的最后一个开始和当前min比较，且需要保证索引大于等于0
			array[j+1] = array[j]         # 如果min更小则对应的元素后移一位
			j -= 1                        #元素位置递减
		array[j+1] = min                  #将待排序的数字放到最后一个满足上述条件迭代后的位置(完成排序)
a=[1,2,5,4,6,9,8,5,6,10]
insert_sort(a)
print(a)
# out: [1, 2, 4, 5, 5, 6, 6, 8, 9, 10]
```

4.希尔排序
原理：希尔排序是直接插入排序的改进版本，是一种不稳定的排序方法，Shell排序通过将数据分成不同的组，先对每一组进行排序，然后再对所有的元素进行一次插入排序，以减少数据交换和移动的次数。



代码实现
```
#希尔排序是插入排序的分组形式
def shell_sort(array):
	gap = int(len(array) / 2)
	while gap > 0:
		for i in range(gap,len(array)):
			tmp = array[i]
			j = i- gap
			while j >=0 and array[j]> tmp:
				array[j + gap] = array[j]
				j = j-gap
			array[j+gap] = tmp
		gap = int(gap / 2)

a=[1,2,5,4,6,9,8,5,6,100]
shell_sort(a)
print(a)
# out : [1, 2, 4, 5, 5, 6, 6, 8, 9, 100]
```
5. 快速排序
思想：
找到一个基准值（通常为第一个元素），将其余元素归位，左边列表为小于等于基准值，右边列表为大于基准值，第一次排序之后为【左边列表】+基准值 + 【右边列表】，然后再递归对子列表进行归位排序。

代码实现：(方法二图解链接：[https://blog.csdn.net/yao_guang/article/details/82899355](https://blog.csdn.net/yao_guang/article/details/82899355))
```
#1 思路更加简便，时间复杂度为nlog(n) 但是空间复杂度为O(n)，因为分配了两个临时数组放左右部分
def quick_sort(array):
	if len(array) < 2:
		return array    #基准条件
	else:
		pivot = array[0]  #选取第一个为基准值
		less = [i for i in array[1:] if i <= pivot]    #左列表
		bigger = [i for i in array[1:] if i > pivot]   #右列表
		return quick_sort(less) + [pivot] + quick_sort(bigger)
a=[1,2,5,4,6,9,8,5,6,100]
b =quick_sort(a)
print(b)

#2 不分配临时数组的代码
# 快速排序 -算法导论中思想

def quick_sort_stand(array, left, right):
	if left < right:     #注意结束条件，需要保证左指针小于右指针，否则将会无限递归
		pivot_p = partion(array,left,right)     # 划分区域，pivot_p 左边的元素都小于等于该基准值，右边都大于基准值
		quick_sort_stand(array,left,pivot_p-1)  #对左边区域递归排序
		quick_sort_stand(array,pivot_p+1,right) #对右边元素递归排序


def partion(array,left, right):
	tmp = array[right]            #基准值为最后一个元素
	i = left - 1                  # i 用来标记基准值最终所在的索引位置
	for j in range(left,right):   
		if array[j] <= tmp:       #如果元素小于等于基准值小于基准值的索引位置后移, 并且将大于基准的第一个数和该元素互换位置
			i += 1
			array[i],array[j] = array[j],array[i]
	array[i+1],array[right] = array[right],array[i+1] 
    #遍历完一次之后确定主元的位置，i代表的位置就是小于等于基准值的最大索引，i+1位置应该为基准值的正确位置
	return i+1                   #返回主元的索引

s = [1,3,8,5,4,6,4,9,2]
quick_sort_stand(s,0,len(s)-1)
print(s)
# out [1, 2, 3, 4, 4, 5, 6, 8, 9]

```

6.归并排序
1.思想：
给定待排序的数组 data_list，长度为 n ，设置首尾两个游标 p,q，初始状态，p = 0,q = n，先不纠结是 n 还是 n-1 。
分解: 取中间值 r = (p + q)/2 ，将数组分成左部分 data_list[p,r],右部分 data_list[r+1,q] 。
对上述左右部分递归调用分解。
归并左部分和右部分的结果。
退出条件是 p>=q

2.代码实现
```
#归并排序
#对于递归的理解，首先将一个数组分为左右两边，然后递归一直分组，左边递归完右边递归，到最底层的时候合并一次，这时合并完之后返回上一层的状态，继续进行归并，直到最后整个数组有序。
def merge_sort(array,left,right):
	while left < right:
		mid = int((left+right)/2)  #首先找到中间位置
		merge_sort(array,left,mid) #对左边递归分组
		merge_sort(array,mid+1,right) #对右边递归分组
		merge(array,left,mid,right) #进行合并

def merge(array,left,mid,right):
	tmp = []
	i = left
	j = mid + 1
	while i<= mid and j <=right:
		if array[i]<array[j]:
			tmp.append(array[i])
			i+=1
		else:
			tmp.append(array[j])
			j+=1
	while i<=mid:
		tmp.append(array[i])
		i+=1
	while j<=right:
		tmp.append(array[j])
	array[left:right+1]=tmp

m = [1,8,5,6,4,3]
merge_sort(m,0,len(m)-1)
print(m)
```