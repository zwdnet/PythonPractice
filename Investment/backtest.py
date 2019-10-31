# coding:utf-8
# 第36课 策略与回测系统


import pandas as pd
from os import path
import abc
import numpy as np
from typing import Callable
from ultil import SMA, crossover
from numbers import Number


def assert_msg(condition, msg):
	if not condition:
		raise Exception(msg)
		

def read_file(filename):
	# 获得文件绝对路径
	filepath = path.join(path.dirname(__file__), filename)
	
	# 判断文件是否存在
	assert_msg(path.exists(filepath), "文件不存在")
	
	# 读取csv文件并返回
	return pd.read_csv(filepath,
	                index_col = 0,
	                parse_dates = True,
	                infer_datetime_format =  True)
	
	
# 策略类
class Strategy(metaclass = abc.ABCMeta):
	"""抽象策略类，用于定义交易策略"""
	def __init__(self, broker, data):
		self._indicators = []
		self._broker = broker
		self._data = data
		self._tick = 0
		
	def I(self, func : Callable, *args)->np.ndarray:
		value = func(*args)
		value = np.asarray(value)
		assert_msg(value.shape[-1] == len(self._data.Close), "指示器长度必须和data长度相同")
		
		self._indicators.append(value)
		return value
		
	@property
	def tick(self):
		return self._tick
		
	@abc.abstractmethod
	def init(self):
		pass
		
	@abc.abstractmethod
	def next(self, tick):
		"""步进函数"""
		pass
	
	def buy(self):
		self._broker.buy()
		
	def sell(self):
		self._broker.sell()
		
	@property
	def data(self):
		return self._data


class SmaCross(Strategy):
	fast = 10
	slow = 20
	
	def init(self):
		# 计算每个时刻的快线和慢线
		self.sma1 = self.I(SMA, self.data.Close, self.fast)
		self.sma2 = self.I(SMA, self.data.Close, self.slow)
		
	def next(self, tick):
		# 快线越过慢线，买入
		if crossover(self.sma1[:tick], self.sma2[:tick]):
			self.buy()
		# 慢线越过快线，卖出
		elif crossover(self.sma2[:tick], self.sma1[:tick]):
			self.sell()
		else:
			pass
		
		
# 交易所类
class ExchangeAPI:
	def __init__(self, data, cash, commission):
		assert_msg(0 < cash, "初始现金数量需大于0，输入初始金额为{}".format(cash))
		assert_msg(0 <= commission <= 0.05, "合理手续费率不大于5%，输入的为{}".format(commission))
		self._initial_cash = cash
		self._data = data
		self._commission = commission
		self._position = 0
		self._cash = cash
		self._i = 0
		
	@property
	def cash(self):
		return self._cash
		
	@property
	def position(self):
		return self._position
		
	@property
	def initial_cash(self):
		return self._initial_cash
		
	@property
	def market_value(self):
		return self._cash + self._position * self.current_price
	
	@property
	def current_price(self):
		return self._data.Close[self._i]
		
	def buy(self):
		"""用当前账户余额，全部按市价买入"""
		self._position = float(self._cash / (self.current_price * (1 + self._commission)))
		self._cash = 0.0
		
	def sell(self):
		"""卖出当前账户所有持仓"""
		self._cash += float(self._position * self.current_price * (1 - self._commission))
		self._position = 0.0
		
	def next(self, tick):
		self._i = tick


class Backtest:
	"""
	回测类，用于读取历史行情数据，执行策略，模拟交易并估计收益。
	调用run成员函数来执行。
	"""
	def __init__(self,
	           data : pd.DataFrame,
	           strategy_type : type(Strategy),
	           broker_type : type(ExchangeAPI),
	           cash : float = 10000,
	           commission : float = .0):
		assert_msg(issubclass(strategy_type, Strategy), "strategy_type不是一个Stragegy类型")
		assert_msg(issubclass(broker_type, ExchangeAPI), "broker_type不是一个ExchangeAPI类型")
		assert_msg(isinstance(commission, Number), "commission不是浮点数值类型")
        
		data = data.copy(False)
        
        # 如果没有volume列，填充Nan
		if "Volume" not in data:
			data["Volume"] = np.Nan
        	
        # 验证OHLC数据格式
		assert_msg(len(data.columns & {"Open", "High", "Low", "Close", "Volume"}) == 5, "输入data格式不正确，至少要包括五列")
        
        # 检查缺失值
		assert_msg(not data[["Open", "High", "Low", "Close", "Volume"]].max().isnull().any(), "部分数据包含缺失值")
        
        # 如果数据没有排序，就排序
		if not data.index.is_monotonic_increasing:
			data = data.sort_index()
        
        # 利用数据,初始化交易所对象和策略对象
		self._data = data
		self._broker = broker_type(data, cash, commission)
		self._strategy = strategy_type(self._broker, self._data)
		self._result = None
		
	def run(self) -> pd.Series:
		"""运行回测"""
		strategy = self._strategy
		broker = self._broker
		# 策略初始化
		strategy.init()
		
		# 设定回测开始和结束位置
		start = 100
		end = len(self._data)
		
		# 回测主循环，更新市场状态，执行策略
		for i in range(start, end):
			# 先把市场状态移动到第i时刻，然后执行策略
			broker.next(i)
			strategy.next(i)
		
		# 执行完策略，计算并返回结果
		self._results = self._compute_result(broker)
		return self._results
		
	def _compute_result(self, broker):
		s = pd.Series()
		s["初始市值"] = broker.initial_cash
		s["结束市值"] = broker.market_value
		s["收益"] = broker.market_value - broker.initial_cash
		print(s)
		return s
		

if __name__ == "__main__":
	BTCUSD = read_file("BTCUSD_GEMINI.csv")
	assert_msg(BTCUSD.__len__() > 0, "读取失败")
	print(BTCUSD.head())
	
	ret = Backtest(BTCUSD, SmaCross, ExchangeAPI,  10000.0, 0.03).run()
	print(ret)
	