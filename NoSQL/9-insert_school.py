#!/usr/bin/env python3
""" 9-insert_school.py """


def insert_school(school_collection, **kwargs):
    """function that inserts a new document in a collection based on kwargs"""
    return school_collection.insert_one(kwargs).inserted_id
