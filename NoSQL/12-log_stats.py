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


# default host:port is localhost:27017
client = MongoClient()
col = client.logs.nginx

# have to use empty {} to get count of all docs!
count = col.count_documents({})
get = col.count_documents({"method": "GET"})
post = col.count_documents({"method": "POST"})
put = col.count_documents({"method": "PUT"})
patch = col.count_documents({"method": "PATCH"})
delete = col.count_documents({"method": "DELETE"})
status = col.count_documents({"method": "GET", "path": "/status"})

if __name__ == "__main__":
    print(f"{count} logs")
    print("Methods:")
    print(f"\tmethod GET: {get}")
    print(f"\tmethod POST: {post}")
    print(f"\tmethod PUT: {put}")
    print(f"\tmethod PATCH: {patch}")
    print(f"\tmethod DELETE: {delete}")
    print(f"{status} status check")
