# coding:utf-8
# 第13课 Python模块化
# src/main.py
import sys
sys.path.append("..")
from proto.mat import Matrix
from utils.mat_mul import mat_mul

a = Matrix([[1,2], [3,4]])
b = Matrix([[5,6], [7,8]])

print(mat_mul(a, b).data)