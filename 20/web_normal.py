# coding:utf-8
# 第20课 揭秘Python协程，常规爬虫


import requests
from bs4 import BeautifulSoup
import time


def crawler():
	url = "https://movie.douban.com/cinema/later/beijing/"
	init_page = requests.get(url).content
	init_soup = BeautifulSoup(init_page, "lxml")
	
	all_movies = init_soup.find("div", id = "showing-soon")
	for each_movie in all_movies.find_all("div", class_ = "item"):
		all_a_tag = each_movie.find_all("a")
		all_li_tag = each_movie.find_all("li")
		
		movie_name = all_a_tag[1].text
		url_to_fetch = all_a_tag[1]['href']
		movie_date = all_li_tag[0].text
		
		response_item = requests.get(url_to_fetch).content
		soup_item = BeautifulSoup(response_item, "lxml")
		img_tag = soup_item.find("img")
		
		print("{} {} {}".format(movie_name, movie_date, img_tag))
		
		
if __name__ == "__main__":
	start = time.perf_counter()		
	crawler()
	end = time.perf_counter()
	print("常规爬虫运行耗时{}秒".format(end-start))

		