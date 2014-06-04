#!/usr/bin/env python
# coding=utf-8
import redis
class redis_pool():

    def __init__(self, redis_addr, redis_port, redis_password, redis_db):
        self.redis_addr = redis_addr
        self.redis_password = redis_password
        self.redis_port = redis_port
        self.redis_db = redis_db
		
    def get_redis(self):
        pool=redis.ConnectionPool(host=self.redis_addr, port=self.redis_port, 
                                  password=self.redis_password, db=self.redis_db)
        return redis.Redis(connection_pool=pool)	

    def get_port_password(self, port):
        r = self.get_redis()
        return r.get("shadowsocks_redis_port_"+port)
