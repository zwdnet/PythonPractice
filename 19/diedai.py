# coding:utf-8
# 第19课 迭代器和生成器


import os
import psutil
import functools
import time


if __name__ == "__main__":
	# 判断一个对象是否可迭代
	def is_iterable(param):
		try:
			iter(param)
			return True
		except TypeError:
			return False
			
	params = [
		1234,
		'1234',
		[1, 2, 3, 4],
		set([1, 2, 3, 4]),
		{1:1, 2:2, 3:3, 4:4},
		(1, 2, 3, 4)
	]
	for param in params:
		print("{} is iterable? {}".format(param, is_iterable(param)))
		
	# 生成器
	def show_memory_info(hint):
		pid = os.getpid()
		p = psutil.Process(pid)
		
		info = p.memory_full_info()
		memory = info.uss / 1024. /1024
		print("{} memory used: {}MB".format(hint, memory))
		
	def log_execution_time(func):
		@functools.wraps(func)
		def wrapper(*args, **kwargs):
			start = time.perf_counter()
			res = func(*args, **kwargs)
			end = time.perf_counter()
			print("函数{}运行耗时{}秒".format(func.__name__, end-start))
			return res
		return wrapper
		
	@log_execution_time
	def test_iterator():
		show_memory_info("初始化迭代器")
		list1 = [i for i in range(10000000)]
		show_memory_info("初始化迭代器以后")
		print(sum(list1))
		show_memory_info("调用sum以后")
		
	@log_execution_time
	def test_generator():
		show_memory_info("初始化生成器")
		list2 = (i for i in range(10000000))
		show_memory_info("初始化生成器以后")
		print(sum(list2))
		show_memory_info("调用sum以后")
		
	test_iterator()
	test_generator()
	
	# 使用生成器
	def generator(k):
		i = 1
		while True:
			yield i**k
			i += 1
		
	gen_1 = generator(1)
	gen_3 = generator(3)
	
	def get_sum(n):
		sum_1, sum_3 = 0, 0
		for i in range(n):
			next_1 = next(gen_1)
			next_3 = next(gen_3)
			print("next_1={}, next_3={}".format(next_1, next_3))
			sum_1 += next_1
			sum_3 += next_3
		print(sum_1*sum_1, sum_3)
	
	get_sum(8)
	
	# 生成器的另一个例子，找指定元素在列表中的位置
	def index_generator(L, target):
		for i, num in enumerate(L):
			if num == target:
				yield i
				
	print(list(index_generator([1, 6, 2, 4, 5, 2, 8, 6, 3, 2], 2)))
	
	# 给定两个有序序列，判断第一个是不是第二个的子序列
	def is_subsequence(a, b):
		b = iter(b)
		return all(i in b for i in a)
		
	print(is_subsequence([1,3,5], [1,2,3,4,5]))
	print(is_subsequence([1,4,3], [1,2,3,4,5]))
	
	# 将上面的代码复杂化
	def is_subsequence2(a, b):
		b = iter(b)
		print(b)
		
		gen = (i for i in a)
		print(gen)
		
		for i in gen:
			print(i)
			
		gen = ((i in b) for i in a)
		print(gen)
		
		for i in gen:
			print(i)
			
		return all((i in b) for i in a)
		
	print(is_subsequence2([1,3,5], [1,2,3,4,5]))
	print(is_subsequence2([1,4,3], [1,2,3,4,5]))
	
	# 思考题 有限元素生成器无限迭代
	gen = (i for i in range(5))
	for i in range(10):
		print(next(gen))
		
	
	