# coding:utf-8
# 第16课 Python里的参数传递


if __name__ == "__main__":
	# 变量及赋值
	a = 1
	b = a
	a = a + 1
	print(a, b)
	# 列表赋值
	l1 = [1,2,3]
	l2 = l1
	l1.append(4)
	print(l1)
	print(l2)
	
	# 函数参数传递
	def my_func1(b):
		b = 2
		
	a = 1
	my_func1(a)
	print(a)
	
	def my_func2(b):
		b = 2
		return b
		
	a = my_func2(a)
	print(a)
	# 传入可变对象
	def my_func3(l2):
		l2.append(4)
	l1 = [1,2,3]
	my_func3(l1)
	print(l1)
	# 参数原值不变
	def my_func4(l2):
		l2 = l2 + [4]
	l1 = [1,2,3]
	my_func4(l1)
	print(l1)
	# 要改变参数原值的做法
	def my_func5(l2):
		l2 = l2 + [4]
		return l2
	l1 = [1,2,3]
	l1 = my_func5(l1)
	print(l1)
	
	# 思考题1
	l1 = [1,2,3,4]
	l2 = [1,2,3,4]
	l3 = l2
	print(id(l1), id(l2), id(l3))
	# 思考题2
	def func(d):
		d["a"] = 10
		d["b"] = 20
		
	d = {"a":1, "b":2}
	func(d)
	print(d)
	