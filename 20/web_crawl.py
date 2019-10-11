# coding:utf-8
# 第20课 揭秘Python协程，协程版爬虫


import asyncio
import aiohttp
from bs4 import BeautifulSoup
import time


async def fetch_content(url):
	async with aiohttp.ClientSession(connector = aiohttp.TCPConnector(ssl=False)) as session:
		async with session.get(url) as response:
			return await response.text()


async def main():
	url =  "https://movie.douban.com/cinema/later/beijing/"
	init_page = await fetch_content(url)
	init_soup = BeautifulSoup(init_page, 'lxml')
	
	movie_names, urls_to_fetch, movie_dates = [], [], []
	
	all_movies = init_soup.find("div", id = "showing-soon")
	
	for each_movie in all_movies.find_all("div", class_ = "item"):
		all_a_tag = each_movie.find_all('a')
		all_li_tag = each_movie.find_all("li")
		
		movie_names.append(all_a_tag[1].text)
		urls_to_fetch.append(all_a_tag[1]["href"])
		movie_dates.append(all_li_tag[0].text)
		
	tasks = [fetch_content(url) for url in urls_to_fetch]
	pages = await asyncio.gather(*tasks)
	
	for movie_name, movie_date, page in zip(movie_names, movie_dates, pages):
		soup_item = BeautifulSoup(page, "lxml")
		img_tag = soup_item.find("img")
		print("{} {} {}".format(movie_name, movie_date, img_tag["src"]))
	

if __name__ == "__main__":
	start = time.perf_counter()		
	asyncio.run(main())
	end = time.perf_counter()
	print("协程爬虫运行耗时{}秒".format(end-start))