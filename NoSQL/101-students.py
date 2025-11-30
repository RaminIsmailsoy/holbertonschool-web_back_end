#!/usr/bin/env python3

''' Write a Python function that returns all students sorted by average score:
Prototype: def top_students(mongo_collection):  mongo_collection will be the pymongo collection object
The top must be ordered  The average score must be part of each item returns with key = averageScore '''


def top_students(mongo_collection):
    '''  Returns all students sorted by average score. Each student will have a new key 'averageScore'. '''

    students = []
    for student in mongo_collection.find():
        scores = student.get('topics', [])
        if scores:
            # Calculate average of the 'score' values
            avg = sum(topic['score'] for topic in scores) / len(scores)
        else:
            avg = 0
        student['averageScore'] = round(avg, 2)  # match test formatting
        students.append(student)

    # Sort by averageScore descending
    students.sort(key=lambda x: x['averageScore'], reverse=True)

    return students

def top_students(mongo_collection):
    ''' Returns all students sorted by average score '''

    return list(mongo_collection.find())
