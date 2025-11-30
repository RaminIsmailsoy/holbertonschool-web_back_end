#!/usr/bin/env python3

''' Module for using PyMongo '''


from pymongo import MongoClient


def log_stats():
    client = MongoClient('mongodb://127.0.0.1:27017')
    logs = client.logs.nginx

    # Total logs
    total_logs = logs.count_documents({})
    print(f"{total_logs} logs")

    # Methods
    print("Methods:")
    for method in ["GET", "POST", "PUT", "PATCH", "DELETE"]:
        count = logs.count_documents({"method": method})
        print(f"\tmethod {method}: {count}")

    # Status check
    status_count = logs.count_documents({"method": "GET", "path": "/status"})
    print(f"{status_count} status check")

    # Top 10 IPs using aggregation
    pipeline = [
        {"$group": {"_id": "$ip", "count": {"$sum": 1}}},
        {"$sort": {"count": -1, "_id": 1}},  # sort by count desc, then IP asc
        {"$limit": 10}
    ]
    top_ips = logs.aggregate(pipeline)

    print("IPs:")
    for ip in top_ips:
        print(f"\t{ip['_id']}: {ip['count']}")


if __name__ == "__main__":
    log_stats()
