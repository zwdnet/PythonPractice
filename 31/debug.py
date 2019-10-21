# coding:utf-8
# 第31课 pdb与cProfile


import pdb
import cProfile


def func():
	print("进入func()")
	

def memoize(f):
	memo = {}
	def helper(x):
		if x not in memo:
			memo[x] = f(x)
		return memo[x]
	return helper


@memoize
def fib(n):
	if n == 0:
		return 0
	elif n == 1:
		return 1
	else:
		return fib(n - 1) + fib(n - 2)
		

def fib_seq(n):
	res = []
	if n > 0:
		res.extend(fib_seq(n - 1))
	res.append(fib(n))
	return res


if __name__ == "__main__":
	a = 1
	b = 2
	# pdb.set_trace()
	func()
	c = 3
	print(a + b + c)
	
	# res = fib_seq(30)
	# print(res)
	cProfile.run("fib_seq(30)")