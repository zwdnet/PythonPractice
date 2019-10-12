# coding:utf-8
# 第21课 Python并发编程之futures


import requests
import time
import concurrent.futures
import threading


# 单线程版下载
def download_one(url):
	resp = requests.get(url)
	print("read {} from {}".format(len(resp.content), url))
	

def download_all(sites):
	for site in sites:
		download_one(site)
		

# 多线程版下载
def download_all_futures(sites):
	with concurrent.futures.ThreadPoolExecutor(max_workers = 5) as executor:
		executor.map(download_one, sites)
		

# 并行版
def download_all_futures_bx(sites):
	with concurrent.futures.ThreadPoolExecutor() as executor:
		executor.map(download_one, sites)
		

# 另一种写法的并行版本
def download_all_futures_bx2(sites):
	with concurrent.futures.ThreadPoolExecutor() as executor:
		to_do = []
		for site in sites:
			future = executor.submit(download_one, site)
			to_do.append(future)
		for future in concurrent.futures.as_completed(to_do):
			future.result()


if __name__ == "__main__":
	sites = [
		'http://www.dapenti.com/blog/readforwx.asp?name=xilei&id=143655',
		'http://www.dapenti.com/blog/readforwx.asp?name=xilei&id=143656',
		'http://www.dapenti.com/blog/readforwx.asp?name=xilei&id=143657',
		'http://www.dapenti.com/blog/readforwx.asp?name=xilei&id=143658',
		'http://www.dapenti.com/blog/readforwx.asp?name=xilei&id=143659',
		'http://www.dapenti.com/blog/readforwx.asp?name=xilei&id=143660',
		'http://www.dapenti.com/blog/readforwx.asp?name=xilei&id=143661',
		'http://www.dapenti.com/blog/readforwx.asp?name=xilei&id=143662'
	]
	try:
		start_time = time.perf_counter()
		download_all(sites)
		end_time = time.perf_counter()
		print("单线程版下载了{}个网站，耗时{}".format(len(sites), end_time-start_time))
	
		start_time = time.perf_counter()
		download_all_futures(sites)
		end_time = time.perf_counter()
		print("多线程版下载了{}个网站，耗时{}".format(len(sites), end_time-start_time))
	
		start_time = time.perf_counter()
		download_all_futures_bx(sites)
		end_time = time.perf_counter()
		print("并行版下载了{}个网站，耗时{}".format(len(sites), end_time-start_time))
	
		start_time = time.perf_counter()
		download_all_futures_bx2(sites)
		end_time = time.perf_counter()
		print("另一个并行版下载了{}个网站，耗时{}".format(len(sites), end_time-start_time))
	# 处理requests异常
	except ConnectionError as err:
		print(err)
	except HTTPError as err:
		print(err)
	except Timeout as err:
		print(err)
	# 处理futures异常
	except TooManyRedirects as err:
		print(err)
	except CancelledError as err:
		print(err)
	except TimeoutError as err:
		print(err)
	except BrokenExecutor as err:
		print(err)
	except:
		print("发生错误")
	