# -*- coding:utf-8 -*-
# 基础篇 03 列表和元组

if __name__ == "__main__":
    l = [1, 2, "hello", "world"]
    tup = ("jason", 22)
    print(l)
    print(tup)
    
    l = [1, 2, 3, 4]
    l[3] = 40
    print(l)
    tup = (1, 2, 3, 4)
    # tup[3] = 40
    print(tup)
    # 增加元素
    new_tup = tup + (5,)
    print(new_tup)
    l.append(5)
    print(l)
    
    # 片切操作
    l = [1, 2, 3, 4]
    print(l[1:3])
    tup = (1, 2, 3, 4)
    print(tup[1:3])
    
    # 嵌套
    l = [[1,2,3], [4,5]]
    tup = ((1,2,3), (4,5,6))
    print(l)
    print(tup)
    
    # 相互转换
    print(list((1,2,3)))
    print(tuple([1,2,3]))
    
    # 内置函数
    l = [3,2,3,7,8,1]
    print(l.count(3))
    print(l.index(7))
    l.reverse()
    print(l)
    l.sort()
    print(l)
    
    tup = (3,2,3,7,8,1)
    print(tup.count(3))
    print(tup.index(7))
    print(list(reversed(tup)))
    print(sorted(tup))
    
    # 列表和元组的存储差异
    l = [1,2,3]
    tup = (1,2,3)
    print(l.__sizeof__()) #32
    print(tup.__sizeof__()) #24
    
    l = []
    print(l.__sizeof__()) #20
    l.append(1)
    print(l.__sizeof__()) #36
    l.append(2)
    print(l.__sizeof__()) #36
    l.append(3)
    print(l.__sizeof__()) #36
    l.append(4)
    print(l.__sizeof__()) #36
    l.append(5)
    print(l.__sizeof__()) #52
