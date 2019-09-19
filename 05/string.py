#-*- coding:utf8-*-
# 基础篇:05深入浅出字符串


if __name__ == "__main__":
	name = 'aaa'
	city = "bbb"
	text = """ccc"""
	print(name, city, text)
	
	# 转义符
	s = "a\nb\tc"
	print(s)
	print(len(s))
	
	# 索引切片遍历
	name = "jason"
	print(name[0])
	print(name[1:3])
	for char in name:
		print(char)
		
	# 改变字符串
	s = "hello"
	s = 'H' + s[1:]
	print(s)
	s = s.replace('H', 'h')
	print(s)
	
	# 字符串拼接，时间复杂度O(N)
	s = ''
	for n in range(0, 100000):
		s += str(n)
	print(s)
	
	# join函数 时间复杂度O(N)
	l = []
	for n in range(0, 100000):
		l.append(str(n))
	l = ' '.join(l)
	print(l)
	
	# split分割数据
	path = "hive://ads/training_table"
	namespace = path.split('//')[1].split('/')[0]
	table = path.split('//')[1].split('/')[1]
	print(namespace, table)
	
	# strip函数
	s = " my name is jason "
	print(s.strip())
	
	# 字符串格式化函数
	print("我的名字叫{},年龄{}".format("zym", str(35)))