# coding:utf-8
# 量化交易框架:行情数据对接和抓取


import requests
import timeit
import websocket
import threading
import ssl
import json


# 获取报价
def get_orderbook():
	orderbook = requests.get("https://api.gemini.com/v1/book/btcusd").json()
	
	
# WebSocket测试
# 在接收到服务器发送的消息时调用
def on_message(ws, message):
	print("接受到:" + message)
	with open("BTCUSD.txt", "a+") as f:
			print(message)
			f.write(json.dumps(message) + "/n")
	

# 在和服务器建立完全连接时调用
def on_open(ws):
	# 线程运行函数
	def gao():
		# 往服务器发送0-4，每次发送完休息0.1秒
		for i in range(5):
			time.sleep(0.1)
			msg = "{0}".format(i)
			ws.send(msg)
			print("发送了:" + msg)
		# 休息1秒用于接受服务器回复的消息
		time.sleep(1)
		
		# 关闭websocket连接
		ws.close()
		print("websocket关闭了")
	
	# 在另一个线程运行gao函数
	threading.start_new_thread(gao, ())


# 获取报价
count = 5

def on_mes(ws, message):
	global count
	print(message)
	count -= 1
	print("count={}".format(count))
	# 接受五次消息后关闭
	if count == 0:
		ws.close()


if __name__ == "__main__":
	'''
	n = 10
	latency = timeit.timeit("get_orderbook()", setup = "from __main__ import get_orderbook", number = n)
	print("Latency is {} ms.".format(latency * 1000))
	'''
	# ws = websocket.WebSocketApp("ws://echo.websocket.org", on_message = on_message, on_open = on_open)
	# ws.run_forever()
	ws = websocket.WebSocketApp("wss://api.gemini.com/v1/marketdata/btcusd?top_of_book=true&offers=true", on_message = on_message)
	ws.run_forever(sslopt={"cert_reqs" : ssl.CERT_NONE})
	