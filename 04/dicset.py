# -*- coding:utf-8 -*-
# 基础篇 04 字典和集合


# 根据商品ID求价格，用列表
def find_product_price(products, product_id):
	for id, price in products:
		if id == product_id:
			return price
	return None
    
products = [
	(1, 100),
	(2, 400),
	(3, 50),
	(4, 400)
]


# 更改需求，找出有多少种不同的价格
def find_unique_price(products):
	unique_price_list = []
	for _, price in products:
		if price not in unique_price_list:
			unique_price_list.append(price)
	return len(unique_price_list)
	
	
# 字典版
def find_unique_price_set(products):
	unique_price_set = set()
	for _, price in products:
		unique_price_set.add(price)
	return len(unique_price_set)


if __name__ == "__main__":
    # 初始化字典和集合
    d1 = {"name":"jason", "age":20, "gender":"male"}
    d2 = dict({"name":"jason", "age":20, "gender":"male"})
    d3 = dict([('name', 'jason'), ('age', 20), ('gender', 'male')])
    d4 = dict(name='jason', age=20, gender='male')
    print(d1 == d2 == d3 == d4)
    
    s1 = {1, 2, 3}
    s2 = set([1, 2, 3])
    print(s1 == s2)
    
    # 混合类型
    s = {1, "hello", 5.0}
    print(s)
    
    # 元素访问
    d = {"name":"zym", "age":20}
    print(d["name"])
    print(d.get("age"))
    print(d.get("locate", "null"))
    
    s = {1, 2, 3}
    # print(s[1]) #本行出错
    
    # 判断元素是否在字典/集合内
    s = {1, 2, 3}
    print(1 in s)
    print(10 in s)
    d = {"name":"zym", "age":20}
    print("name" in d)
    print("location" in d)
    
    # 增删查改函数
    d = {"name":"zym", "age":20}
    d["gender"] = "male" #增加元素
    d["dob"] = "1999-02-01"
    print(d)
    d["dob"] = "1998-01-01" #更新键值
    print(d)
    d.pop("dob")  #删除键值
    print(d)
    
    s = {1, 2, 3}
    s.add(4) #增加元素
    print(s)
    s.remove(4) #删除元素
    print(s)
    
    # 字典排序
    d = {'b':1, 'a':2, 'c':10}
    # 根据字典键的升序排序
    d_sorted_by_key = sorted(d.items(), key = lambda x:x[0])
    print(d_sorted_by_key)
    # 根据字典值的升序排序
    d_sorted_by_value = sorted(d.items(), key = lambda x:x[1])
    print(d_sorted_by_value)
    
    # 对集合排序
    s = [3, 4, 2, 1]
    s_sorted = sorted(s)
    print(s_sorted)
    
    # 根据商品ID找商品价格
    print("id为2的商品价格为{}".format(find_product_price(products, 2)))
    
    # 用字典来存储
    products_set = {
        1:100,
        2:400,
        3:50,
        4:400}
    print("id为3的商品价格为{}".format(products_set[3]))
    
    # 看商品里有多少种不同的价格？
    # 列表版， O(N²)
    print("不同价格的数目为{}".format( find_unique_price(products)))
    # 字典版，O(N)
    print("不同价格的数目为{}".format( find_unique_price_set(products)))
    
    # 计算效率
    import time
    
    id = [x for x in range(0, 10000)]
    price = [x for x in range(20000, 30000)]
    products = list(zip(id, price))
    
    # 计算列表版本的时间
    start_using_list = time.perf_counter()
    find_unique_price(products)
    end_using_list = time.perf_counter()
    print("使用列表耗时:{}".format(end_using_list - start_using_list))
    
    # 计算字典版本的时间
    start_using_set = time.perf_counter()
    find_unique_price_set(products)
    end_using_set = time.perf_counter()
    print("使用列表耗时:{}".format(end_using_set - start_using_set))

    