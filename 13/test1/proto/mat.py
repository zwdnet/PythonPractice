# coding:utf-8
# 第13课 Python模块化
# /proto/mat.py

class Matrix(object):
	def __init__(self, data):
		self.data = data
		self.n = len(data)
		self.m = len(data[0])
