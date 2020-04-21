# -*- coding: utf-8 -*-
# @Data : 2020-04-17

'''
Python 数据结构

'''

# 队列
from collections import deque

q = deque()
q.append('eat')
q.append('sleep')
q.append('code')

print(q.popleft())