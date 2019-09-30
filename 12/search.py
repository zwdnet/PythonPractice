# coding:utf-8
# 第12课，面向对象(下)


# 搜索引擎基类
class SearchEngineBase(object):
	def __init__(self):
		print("父类")
		
	def add_corpus(self, file_path):
		with open(file_path, "r") as fin:
			text = fin.read()
		self.process_corpus(file_path, text)
	
	def process_corpus(self, id, text):
		raise Exception("process_corpus未定义")
		
	def search(self, query):
		raise Exception("search未定义")
		
		
def main(search_engine):
	for file_path in ["1.txt", "2.txt", "3.txt", "4.txt"]:
		search_engine.add_corpus(file_path)
	
	while True:
		query = input("输入检索词，输q结束:")
		if query == "q":
			break
		results = search_engine.search(query)
		print("found {} result(s):".format(len(results)))
		
		for result in results:
			print(result)
			
			
# 简单的搜索引擎
class SimpleEngine(SearchEngineBase):
	def __init__(self):
		super(SimpleEngine, self).__init__()
		print("子类")
		self.__id_to_texts = {}
		
	def process_corpus(self, id, text):
		self.__id_to_texts[id] = text
		
	def search(self, query):
		results = []
		for id, text in self.__id_to_texts.items():
			if query in text:
				results.append(id)
		return results


# 分词的搜索引擎
import re

class BOWEngine(SearchEngineBase):
	def __init__(self):
		super(BOWEngine, self).__init__()
		self.__id_to_word = {}
		
	def process_corpus(self, id, text):
		self.__id_to_word[id] = self.parse_text_to_word(text)
		
	def search(self, query):
		query_words = self.parse_text_to_word(query)
		results = []
		for id, words in self.__id_to_word.items():
			if self.query_match(query_words, words):
				results.append(id)
		return results
		
	@staticmethod
	def parse_text_to_word(text):
		# 使用正则表达式去除标点和换行符
		text = re.sub(r'[^\w ]', ' ', text)
		# 转为小写
		text = text.lower()
		# 生成所有单词的列表
		word_list = text.split(' ')
		# 去除空白单词
		word_list = filter(None, word_list)
		# 返回单词的set
		return set(word_list)
		
	@staticmethod
	def query_match(query_words, words):
		for query_word in query_words:
			if query_word not in words:
				return False
		return True

# 减少查询的量
class BOWInvertedIndexEngine(SearchEngineBase):
	def __init__(self):
		super(BOWInvertedIndexEngine, self).__init__()
		self.inverted_index = {}
		
	def process_corpus(self, id, text):
		words = self.parse_text_to_word(text)
		for word in words:
			if word not in self.inverted_index:
				self.inverted_index[word] = []
			self.inverted_index[word].append(id)
			
	def search(self, query):
		query_words = list(self.parse_text_to_word(query))
		query_words_index = list()
		for query_word in query_words:
			query_words_index.append(0)
			
		# 如果某一单词倒序索引，立即返回
		for query_word in query_words:
			if query_word not in self.inverted_index:
				return []
				
		result = []
		while True:
			# 首先获得当前状态下所有倒序索引的index
			current_ids = []
			for idx, query_word in enumerate(query_words):
				current_index = query_words_index[idx]
				current_inverted_list = self.inverted_index[query_word]
				# 已经遍历到某个倒序索引的末尾，结束
				if current_index >= len(current_inverted_list):
					return result
				current_ids.append(current_inverted_list[current_index])
			
			# 然后，如果 current_ids 的所有元素都一样，那么表明这个单词在这个元素对应的文档中都出现了
			if all(x == current_ids[0] for x in current_ids):
				result.append(current_ids[0])
				query_words_index = [x+1 for x in query_words_index]
				continue
				
			# 如果不是，把最小元素加1
			min_val = min(current_ids)
			min_val_pos = current_ids.index(min_val)
			query_words_index[min_val_pos] += 1
			
	@staticmethod
	def parse_text_to_word(text):
		# 使用正则表达式去除标点和换行符
		text = re.sub(r'[^\w ]', ' ', text)
		# 转为小写
		text = text.lower()
		# 生成所有单词的列表
		word_list = text.split(' ')
		# 去除空白单词
		word_list = filter(None, word_list)
		# 返回单词的set
		return set(word_list)


# 缓存和多重继承
import pylru

class LRUCache(object):
	def __init__(self, size = 2):
		self.cache = pylru.lrucache(size)
		
	def has(self, key):
		return key in self.cache
		
	def get(self, key):
		return self.cache[key]
		
	def set(self, key, value):
		self.cache[key] = value
		

class BOWInvertedIndexEngineWithCache(BOWInvertedIndexEngine, LRUCache):
	def __init__(self):
		super(BOWInvertedIndexEngineWithCache, self).__init__()
		LRUCache.__init__(self)
		
	def search(self, query):
		if self.has(query):
			print("缓存命中!")
			return self.get(query)
			
		result = 		super(BOWInvertedIndexEngineWithCache, self).search(query)
		self.set(query, result)
		
		return result


if __name__ == "__main__":
	# search_engine = SimpleEngine()
	# main(search_engine)
	# search_engine = BOWEngine()
	# main(search_engine)
	# search_engine = BOWInvertedIndexEngine()
	# main(search_engine)
	search_engine = BOWInvertedIndexEngineWithCache()
	main(search_engine)
	