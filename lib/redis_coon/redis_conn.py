#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/1/9 16:08
# @Author  : Liquid
# @Site    : 
# @File    : redis_conn.py
# @Software: PyCharm
import redis

from baizhi_web.settings import REDIS_IP, REDIS_PORT

conn = redis.Redis(REDIS_IP, REDIS_PORT, 14)

