#!/usr/bin/env python3

''' Log stats Write a Python script that provides some stats about Nginx logs stored in MongoDB:

    Database: logs
    Collection: nginx
    Display (same as the example):
        first line: x logs where x is the number of documents in this collection
        second line: Methods:
        5 lines with the number of documents with the method = ["GET", "POST", "PUT", "PATCH", "DELETE"] in this order (see example below - warning: its a tabulation before each line)
        one line with the number of documents with:
            method=GET
            path=/status
'''


from pymongo import MongoClient

def log_stats():
    x = MongoClient('mongodb://localhost:27017').logs.nginx


    print(f'{x.count_documents({})} logs')


    print('Methods:')
    print(f'\tmethod GET: {x.count_documents({"method": "GET"})}')
    print(f'\tmethod POST: {x.count_documents({"method": "POST"})}')
    print(f'\tmethod PUT: {x.count_documents({"method": "PUT"})}')
    print(f'\tmethod PATCH: {x.count_documents({"method": "PATCH"})}')
    print(f'\tmethod DELETE: {x.count_documents({"method": "DELETE"})}')


    print(f'{x.count_documents({"method": "GET", "path": "/status"})} status check')

if __name__ == "__main__":
    log_stats()
