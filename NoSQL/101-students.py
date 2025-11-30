#!/usr/bin/env python3

''' Write a Python function that returns all students sorted by average score:
Prototype: def top_students(mongo_collection):  mongo_collection will be the pymongo collection object
The top must be ordered  The average score must be part of each item returns with key = averageScore '''


def top_students(mongo_collection):
     ''' Returns all students sorted by average score. Each student will have a new key 'averageScore'. '''

    students = []
    for student in mongo_collection.find():
        topics = student.get('topics', [])
        if topics:
            avg = sum(topic['score'] for topic in topics) / len(topics)
        else:
            avg = 0
        student['averageScore'] = avg  # Keep full precision
        students.append(student)

    # Sort descending by averageScore
    students.sort(key=lambda x: x['averageScore'], reverse=True)
    return students
