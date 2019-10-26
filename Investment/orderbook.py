# coding:utf-8
# 第36课 行情抓取


import copy
import json
import ssl
import time
import websocket


class OrderBook(object):
	
	BIDS = "bid"
	ASKS = "ask"
	
	def __init__(self, limit = 20):
		self.limit = limit
		
		# (price, mount)
		self.bids = {}
		self.asks = {}
		
		self.bids_sorted = []
		self.asks_sorted = []
		
	def insert(self, price, amount, direction):
		if direction == self.BIDS:
			if amount == 0:
				if price in self.bids:
					del self.bids[price]
			else:
				self.bids[price] = amount
		elif direction == self.ASKS:
			if amount == 0:
				if price in self.asks:
					del self.asks[price]
			else:
				self.asks[price] = amount
		else:
			print("错误:未知的方向{}".format(direction))
			
	def sort_and_truncate(self):
		# sort
		self.bids_sorted = sorted([(price, amount) for price, amount in self.bids.items()], reverse = True)
		self.asks_sorted = sorted([(price, amount) for price, amount in self.asks.items()])
		
		# truncate
		self.bids_sorted = self.bids_sorted[:self.limit]
		self.asks_sorted = self.asks_sorted[:self.limit]
		
		# copy back
		self.bids = dict(self.bids_sorted)
		self.asks = dict(self.asks_sorted)
		
	def get_copy_of_bids_and_asks(self):
		return copy.deepcopy(self.bids_sorted, copy.deepcopy(self.asks_sorted))


class Crawler:
	def __init__(self, symbol, output_file):
		self.orderbook = OrderBook(limit = 10)
		self.output_file = output_file
		
		self.ws = websocket.WebSocketApp("wss://api.gemini.com/v1/marketdata/{}".format(symbol), on_message = lambda ws, message : self.on_message(message))
		self.ws.run_forever(sslopt = {"cert_reqs" : ssl.CERT_NONE})
		
	def on_message(self, message):
		data = json.loads(message)
		print(data)
		for event in data["events"]:
			price, amount, direction = float(event["price"]), float(event["remaining"]), event["side"]
			self.orderbook.insert(price, amount, direction)
		
		self.orderbook.sort_and_truncate()
		
		# 输出到文件
		with open(self.output_file, "a+") as f:
			bids, asks = self.orderbook.get_copy_of_bids_and_asks()
			output = {
				"bids" : bids,
				"asks" : asks,
				"ts" : int(time.time() * 1000)
			}
			print(json.dump(output))
			f.write(json.dump(output) + "\n")


if __name__ == "__main__":
	crawler = Crawler(symbol = "BTCUSD", output_file = "BTCUSD.txt")
	