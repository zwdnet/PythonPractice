# coding:utf-8
# 工具函数


import pandas as pd


def SMA(values, n):
	"""返回简单滑动平均"""
	return pd.Series(values).rolling(n).mean()
	
	
def crossover(series1, series2):
	"""检查两个序列是否在结尾交叉"""
	return series1[-2] < series2[-2] and series1[-1] > series1[-1]
	