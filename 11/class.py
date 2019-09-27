# coding:utf-8
# 第11课，面向对象(上)


# 类
class Document():
	def __init__(self, title, author, context):
		print("调用初始函数!")
		self.title = title
		self.author = author
		self.__context = context #私有属性
		
	def get_context_length(self):
		return len(self.__context)
		
	def intercept_context(self, length):
		self.__context = self.__context[:length]
		
		
# 类2
class Document2():
	WELCOME_STR = "欢迎，本书的内容为{}."
	
	def __init__(self, title, author, context):
		print("调用初始函数!")
		self.title = title
		self.author = author
		self.__context = context #私有属性
		
	# 类函数
	@classmethod
	def create_empty_book(cls, title, author):
		return cls(title=title, author=author, context="nothing")
		
	# 成员函数
	def get_context_length(self):
		return len(self.__context)
		
	# 静态函数
	@staticmethod
	def get_welcome(context):
		return Document2.WELCOME_STR.format(context)
		
# 类的继承
class Entity():
	def __init__(self, object_type):
		print("父类构造函数")
		self.object_type = object_type
		
	def get_contex_length(self):
		raise Exception("没有定义get_context_length")
		
	def print_title(self):
		print(self.title)
		
		
class Document3(Entity):
	def __init__(self, title, author, context):
		Entity.__init__(self, "document")
		print("Document3调用初始函数!")
		self.title = title
		self.author = author
		self.__context = context 
		
	def get_context_length(self):
		return len(self.__context)
		
class Video(Entity):
	def __init__(self, title, author, video_length):
		Entity.__init__(self, "video")
		print("video调用初始函数!")
		self.title = title
		self.author = author
		self.__video_length = video_length
		
	def get_context_length(self):
		return self.__video_length
		

# 抽象函数和抽象类
from abc import ABCMeta, abstractmethod
class Entity2(metaclass = ABCMeta):
	@abstractmethod
	def get_title(self):
		pass
		
	@abstractmethod
	def set_title(self, title):
		pass
		

class Document4(Entity2):
	def get_title(self):
		return self.title
		
	def set_title(self, title):
		self.title = title
			
			
# 思考题
class A():
	def __init__(self):
		print("A")
		
class B(A):
	def __init__(self):
		A.__init__(self)
		print("B")
		
class C(A):
	def __init__(self):
		A.__init__(self)
		print("C")
		
class D(B, C):
	def __init__(self):
		B.__init__(self)
		C.__init__(self)
		print("D")

if __name__ == "__main__":
	harry_potter_book = Document("hp", "J.K.Rowling", "aabbccgfdghhddee")
	
	print(harry_potter_book.title)
	print(harry_potter_book.author)
	print(harry_potter_book.get_context_length())
	harry_potter_book.intercept_context(10)
	print(harry_potter_book.get_context_length())
	# print(harry_potter_book.__context)
	
	empty_book = Document2.create_empty_book("aaaaa", "bbbbb")
	print(empty_book.get_context_length())
	print(empty_book.get_welcome("indeed nothing"))
	
	# 类继承
	hp_book = Document3("a", "aa", "aaa")
	hp_movie = Video("b", "bb", 30)
	
	print(hp_book.object_type)
	print(hp_movie.object_type)
	
	print(hp_book.get_context_length())
	print(hp_movie.get_context_length())
	
	# 抽象类
	document = Document4()
	document.set_title("hp")
	print(document.get_title())
	
	# entity = Entity2()
	# 思考题
	d = D()
	