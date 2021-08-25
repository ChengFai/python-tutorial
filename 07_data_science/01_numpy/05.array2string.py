# -*- coding: utf-8 -*-
"""
@author:XuMing(xuming624@qq.com)
@description: 
"""



import numpy as np

# 数组与字符串的转换
# tostring

a = np.array([[1, 2], [3, 4]], dtype=np.uint8)
print(a)
print(a.tostring())

# fromstring 函数
# 可以使用 fromstring 函数从字符串中读出数据，不过要指定类型：
s = a.tostring()
b = np.fromstring(s, dtype=np.uint8)
print(b)

# 此时，返回的数组是一维的，需要重新设定维度：
b.shape = 2, 2
print(b)
