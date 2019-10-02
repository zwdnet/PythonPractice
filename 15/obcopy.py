# coding:utf-8
# 第15课 Python对象比较、拷贝

import copy


if __name__ == "__main__":
	a = 2
	b = 2
	print(a == b)
	print(a is b)
	print("id(a) = {}".format(id(a)))
	print("id(b) = {}".format(id(b)))
	# 以上只对-5至256的值有效
	a = 10000000
	b = 10000000
	print(a == b)
	print(a is b)
	print("id(a) = {}".format(id(a)))
	print("id(b) = {}".format(id(b)))
	
	# 对于不可变变量
	t1 = (1, 2, [3, 4])
	t2 = (1, 2, [3, 4])
	print(t1 == t2)
	print(id(t1), id(t2))
	t1[-1].append(5)
	print(t1 == t2)
	print(id(t1), id(t2))
	
	# 浅拷贝
	l1 = [1, 2, 3]
	l2 = list(l1)
	print(l1 == l2)
	print(l1 is l2)
	s1 = set([1, 2, 3])
	s2 = set(s1)
	print(s1, s2)
	print(s1 == s2)
	print(s1 is s2)
	# 通过切片操作
	l1 = [1, 2, 3]
	l2 = l1[:]
	print(l1 == l2)
	print(l1 is l2)
	# 使用copy函数
	l2 = copy.copy(l1)
	print(l1 == l2)
	print(l1 is l2)
	# 元组的不同，返回一个指向元组的引用
	t1 = (1,2,3)
	t2 = tuple(t1)
	print(t1 == t2)
	print(t1 is t2)
	
	# 浅拷贝的副作用
	l1 = [[1, 2], (30, 40)]
	l2 = list(l1)
	l1.append(100)
	l1[0].append(3)
	print(l1)
	print(l2)
	l1[1] += (50, 60)
	print(l1)
	print(l2)
	
	# 深拷贝
	l1 = [[1, 2], (30, 40)]
	l2 = copy.deepcopy(l1)
	l1.append(100)
	l1[0].append(3)
	print(l1, l2)
	# 陷入无限循环的深拷贝
	x = [1]
	x.append(x)
	print(x)
	y = copy.deepcopy(x)
	print(y)
	# 思考题
	# print(x == y) #报错
	print(x is y)