# coding:utf-8
# 第38课 数据库 日志系统


import peewee
from peewee import *


db = SqliteDatabase("test.db")


class Price(peewee.Model):
	timestamp = peewee.DateTimeField(primary_key = True)
	BTCUSD = peewee.FloatField()
	
	class Meta:
		database = db
		
		
def test_peewee():
	Price.create_table()
	price = Price(timestamp = "2019-11-04 20:00:00", BTCUSD = "123456.78")
	price.save()


if __name__ == "__main__":
	test_peewee()
	