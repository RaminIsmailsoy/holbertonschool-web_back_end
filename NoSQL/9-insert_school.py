#!/usr/bin/env python3

''' Insert a document in Python Prototype: def insert_school(mongo_collection, **kwargs)
mongo_collection will be the pymongo collection object. Returns the new _id '''


def insert_school(mongo_collection, **kwargs):
    ''' function that inserts a new document in a collection based on kwargs '''

    new_document = mongo_collection.insert_one(kwargs)
    return new_document.inserted_id
