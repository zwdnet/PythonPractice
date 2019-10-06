# coding:utf-8
# 第18课 metaclass


import yaml


class Monster(yaml.YAMLObject):
	yaml_tag = "Monster"
	def __init__(self, name, hp, ac, attacks):
		self.name = name
		self.hp = hp
		self.ac = ac
		self.attacks = attacks
		
	def __repr__(self):
		return "{}(name = {}, hp = {}, ac = {}, attacks = {}".format(self.__class__.__name__, self.name, self.hp, self.ac, self.attacks)
	

if __name__ == "__main__":
	Monster(name = "zym", hp = [2, 6], ac = 16, attacks = ["BITE", "HURT"])
	print(yaml.dump(Monster(name = "zym2", hp = [3, 6], ac = 18, attacks = ["BITE", "HURT"])))
	
	# 所有用户自定义类，是type的实例
	class MyClass:
		pass
		
	instance = MyClass()
	print(type(instance))
	print(type(MyClass))
	# 用户自定义类，是type类的__call__运算符重载
	class MyClass2:
		data = 1
		
	instance = MyClass2()
	print(MyClass2, instance, instance.data)
	
	MyClass = type("MyClass", (), {"data":1})
	instance = MyClass()
	print(MyClass, instance, instance.data)
	
	# 网友的例子
	class MyMeta(type):
		def __init__(self, name, bases, dic):
			super().__init__(name, bases, dic)
			print("===>MyMeta.__init__")
			print(self.__name__)
			print(dic)
			print(self.yaml_tag)
			
		def __new__(cls, *args, **kwargs):
			print("===>MyMeta.__new__")
			print(cls.__name__)
			return type.__new__(cls, *args, **kwargs)
			
		def __call__(cls, *args, **kwargs):
			print("===>MyMeta.__call__")
			obj = cls.__new__(cls)
			cls.__init__(cls, *args, **kwargs)
			return obj
			
		
	class Foo(metaclass=MyMeta):
		yaml_tag = "!Foo"
			
		def __init__(self, name):
			print("Foo.__init__")
			self.name = name
				
		def __new__(cls, *args, **kwargs):
			print("Foo.__new__")
			return object.__new__(cls)
				
	foo = Foo("foo")
			