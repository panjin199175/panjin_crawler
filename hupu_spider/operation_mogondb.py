# encding:utf-8

'''
@author: Hollow
@file: operation_mogondb.py
@time: 2019-11-04 15:24

'''

from pymongo import MongoClient

class MongoAPI(object):
    '''封装一个链接数据库，实现多功能的一个方法类'''
    def __init__(self,db_ip,db_port,db_name,table_name):
        self.db_ip = db_ip
        self.db_port = db_port
        self.db_name = db_name
        self.table_name = table_name
        self.conn = MongoClient(host= self.db_ip,port=self.db_port)
        self.db = self.conn[self.db_name]
        self.table = self.db[self.table_name]

    def get_one(self,query):
        return self.table.find_one(query,projection = {"_id":False})

    def get_all(self,query):
        return self.table.find(query)

    def add(self,kv_dict):
        return self.table.insert(kv_dict)

    def delete(self,query):
        return self.table.delete_many(query)

    def check_exist(self,query):
        ret = self.table.find_one(query)
        return ret != None

    #如果没有会创建
    def update(self,query,kv_dict):
        self.table.update_one(query,{
            "$set":kv_dict
        },upsert = True)
