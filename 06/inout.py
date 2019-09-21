#coding:utf-8
#第6课:输入与输出


import re
import json


# 处理文本
def parse(text):
	# 去除标点符号和换行
	text = re.sub(r'[^\w ]', ' ', text)
	# 转为小写
	text = text.lower()
	# 单词列表
	word_list = text.split(' ')
	# 去除空白单词
	word_list = filter(None, word_list)
	# 生成单词和词频的字典
	word_cnt = {}
	for word in word_list:
		if word not in word_cnt:
			word_cnt[word] = 0
		word_cnt[word] += 1
		
	# 按照词频排序
	sorted_word_cnt = sorted(word_cnt.items(), key = lambda kv: kv[1], reverse = True)
	return sorted_word_cnt
	
	
# readline版本的parse，练习1
# 处理文本
def parse_readline(infile):
	# 生成单词和词频的字典
	word_cnt = {}
	while True:
		text = infile.readline()
		if not text:
			break
		print(text)
		# 去除标点符号和换行
		text = re.sub(r'[^\w ]', ' ', text)
		# 转为小写
		text = text.lower()
		# 单词列表
		word_list = text.split(' ')
		# 去除空白单词
		word_list = filter(None, word_list)
		
		for word in word_list:
			if word not in word_cnt:
				word_cnt[word] = 0
			word_cnt[word] += 1
		
		# 按照词频排序
		sorted_word_cnt = sorted(word_cnt.items(), key = lambda kv: kv[1], reverse = True)
		return sorted_word_cnt
	

if __name__ == "__main__":
	"""
	# 输入
	name = input("姓名:")
	gender = input("男的？(y/n)")
	
	welcome_str = "欢迎来到矩阵空间{prefix}{name}."
	welcome_dic = {
	     "prefix":"Mr." if gender == 'y' else "Mrs.",
	     "name":name
	}
	print(welcome_str.format(**welcome_dic))
	
	# 输入类型转换
	a = input("输入a:")
	b = input("输入b:")
	print("a + b ={}".format(a+b))
	print("a的类型为{}，b的类型为{}".format(type(a), type(b)))
	print("a + b ={}".format(int(a) + int(b)))
	"""
	# 文件输入输出
	with open("in.txt", "r") as fin:
		text = fin.read()
		
	word_and_freq = parse(text)
	
	with open("out.txt", "w") as fout:
		for word, freq in word_and_freq:
			fout.write('{} {}\n'.format(word, freq))
	
	# 使用JSON
	params = {
	     "symbol" : "123456",
	     "type" : "limit",
	     "price" : 123.4,
	     "amount" : 23
	}
	params_str = json.dumps(params)
	print("序列化以后")
	print("类型{},值{}".format(type(params_str), params_str))
	
	original_params = json.loads(params_str)
	print("在去序列化之后")
	print("类型{},值{}".format(type(original_params), original_params))
	
	# 思考题1
	with open("in.txt", "r") as fin:
		word_and_freq = parse_readline(fin)
	
	with open("out_readline.txt", "w") as fout:
		for word, freq in word_and_freq:
			fout.write('{} {}\n'.format(word, freq))
	