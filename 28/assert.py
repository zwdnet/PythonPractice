# coding:utf-8
# 第28课 assert


def apply_discount(price, discount):
	updated_price = price * (1 - discount)
	assert 0 <= updated_price <= price, "价格必须大于等于0小于原价"
	return updated_price
	
	
def calculate_average_price(total_sales, num_sales):
	assert num_sales > 0, "销售数量必须大于0"
	return total_sales / num_sales
	

if __name__ == "__main__":
	print(apply_discount(100, 0.2))
	# print(apply_discount(100, 2))
	print(calculate_average_price(100, 2))
	print(calculate_average_price(100, -2))