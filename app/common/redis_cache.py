#!/usr/bin/env python
# coding=utf-8


import redis

redis_host = "10.15.1.11"
redis_port = "6489"

# 连接redis，加上decode_responses=True，写入的键值对中的value为str类型，不加这个参数写入的则为字节类型。
pool = redis.ConnectionPool(host=redis_host, port=redis_port, decode_responses=True)
r = redis.Redis(connection_pool=pool)
