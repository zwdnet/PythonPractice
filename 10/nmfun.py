# coding:utf-8
# 第10课 简约不简单的匿名函数


if __name__ == "__main__":
	# lambda表达式
	square = lambda x:x**2
	print(square(3))
	
	# 列表内部使用
	l = [(lambda x:x**2)(x) for x in range(10)]
	print(l)
	
	# 用作函数参数
	l = [(1, 20), (3, 0), (9, 10), (2, -1)]
	l.sort(key = lambda x:x[1])
	print(l)
	
	# 让程序简洁
	squares = map(lambda x:x**2, [1,2,3,4,5])
	print(list(squares))
	
	# 函数式编程，将列表元素加倍
	def mutiply_2_pure(l):
		new_list = []
		for item in l:
			new_list.append(item*2)
		return new_list
		
	print(mutiply_2_pure([1,2,3,4]))
	
	# map函数
	l = [1,3,5,6,8]
	new_list = list(map(lambda x:x**2, l))
	print(new_list)
	
	# filter函数，返回列表中所有偶数
	l = [1,2,3,4,5,6,7,8,9]
	new_list = filter(lambda x:x%2 == 0, l)
	print(list(new_list))
	
	# reduce函数 计算阶乘
	from functools import reduce
	product = reduce(lambda x, y:x*y, l)
	print(product)
	
	# 思考题
	# 1 将字典按值从大到小排序
	import operator
	d = {"mike":10, "lucy":2, "ben":30}
	print(d.items())
	sort_d = sorted(d.items(), key=operator.itemgetter(1), reverse=True)
	print(sort_d)
	
