# coding:utf-8
# 第13课 Python模块化

import sys
sys.path.append("..")

from utils.class_utils import *
from utils.utils import *


if __name__ == "__main__":
	print(get_sum(1, 2))
	
	encoder = Encoder()
	decoder = Decoder()
	
	print(encoder.encode("abcde"))
	print(decoder.decode("edcba"))
	