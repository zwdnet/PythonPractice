# cofing:utf-8
# 第九课 不可或缺的自定义函数

# 调用另一个函数
def func(message):
	my_func(message)

def my_func(message):
	print("收到一个消息:{}".format(message))



if __name__ == "__main__":
	my_func("hello world!")
	
	# 函数嵌套
	def my_sum(a, b):
		return a+b
		
	result = my_sum(3, 5)
	print(result)
	
	def find_largest_element(l):
		if not isinstance(l, list):
			print("输入数据不是列表")
			return
		if len(l) == 0:
			print("列表为空")
			return
		largest_element = l[0]
		for item in l:
			if item > largest_element:
				largest_element = item
		print("列表中最大元素为:{}".format(largest_element))
		
	find_largest_element([3, -5, 6, 8, 2, 1])
	
	func("你好，python")
	
	# 参数的多态性
	print(my_sum([1, 2], [3, 4]))
	print("hell", " world")
	try:
		my_sum(5, "7")
	except Exception as err:
		print("发生错误!{}".format(err))
		
	# 函数嵌套提高效率
	def factorial(input):
		# 输入检查，只运行一次
		if not isinstance(input, int):
			raise Exception("必须输入整数")
		if input < 0:
			raise Exception("输入必须大于等于0")
		
		# 实际计算
		def inner_factorial(input):
			if input <= 1:
				return 1
			return input*inner_factorial(input-1)
		
		return(inner_factorial(input))
		
	try:
		print(factorial(12))
	except Exception as err:
		print(err)
		
	# 函数中改变外部变量
	value = 2
	overvalue = 3
	def changeValue():
		global value
		value += 1
		overvalue = 6
		print(value, overvalue)
	changeValue()
	print(value)
	
	# 嵌套函数内部修改
	# 加nonlocal
	print("加nonlocal")
	def outer():
		x = 3
		def inner():
			nonlocal x
			x = 5
			print("内部", x)
		print("外部", x)
		inner()
		print("外部", x)
	outer()
	# 不加
	print("不加")
	def outer2():
		x = 3
		def inner2():
			x = 5
			print("内部", x)
		print("外部", x)
		inner2()
		print("外部", x)
	outer2()
	
	# 闭包，计算n次幂
	def nth_power(exp):
		def exponent_of(base):
			return base**exp
		return exponent_of
		
	square = nth_power(2)
	cube = nth_power(3)
	
	print(square(2))
	print(cube(2))
	