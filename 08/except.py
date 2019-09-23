# coding:utf-8
# 第八课 异常处理:如何提高程序的稳定性


# 自定义异常类
class MyInputError(Exception):
	def __init__(self, value):
		self.value = value
	
	def __str__(self):
		return("{} is invalid input".format(repr(self.value)))


if __name__ == "__main__":
	# try except语句
	try:
		s = input("输入数字，以,分隔:")
		num1 = int(s.split(",")[0].strip())
		num2 = int(s.split(",")[1].strip())
		
	except ValueError as err:
		print("值错误:{}".format(err))
	except Exception as err:
		print("其它异常:{}".format(err))
		
	print("继续")
	
	# 自定义异常
	try:
		raise MyInputError(1)
	except MyInputError as err:
		print("error:{}".format(err))
	print("继续2")
		