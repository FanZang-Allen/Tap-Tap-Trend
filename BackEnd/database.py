""" This file is part of Good Read Web Scraper

DataBase class connect to the cloud mongodb database using key stored in dotenv file
Contain useful operation functions of the database
"""

import os
import json
import certifi
import pymongo
from dotenv import load_dotenv

load_dotenv()
client = pymongo.MongoClient(os.getenv('MONGODB_KEY'), tlsCAFile=certifi.where())
database = client['TapTap']


def clear_collection(collection_name: str):
    """
    Clear the given collection in the database
    :param collection_name: name of collection to clear
    :return: None
    """
    if collection_name in database.list_collection_names():
        database[collection_name].delete_many({})
    else:
        print("Collection not exist")


def exist_in_collection(check_id: str, collection_name: str):
    """
    Check if document with given id exist in collection
    :param check_id: id of document
    :param collection_name: name of collection
    :return: True if exist
    """
    if collection_name not in database.list_collection_names():
        return False
    curr_collection = database[collection_name]
    if curr_collection.count_documents({'id': check_id}, limit=1) != 0:
        return True
    return False


def add_data(data: dict, collection_name: str):
    """
    Add data to collection. If data id already exist, update the corresponding documentation
    :param data: data in python dict
    :param collection_name: should exist in database
    :return: True if success
    """
    if collection_name not in database.list_collection_names():
        print("Collection not exist")
        return False

    curr_collection = database[collection_name]
    if curr_collection.count_documents({'id': data['id']}, limit=1) != 0:
        update_data(data, collection_name)
    else:
        curr_collection.insert_one(data)
        print(collection_name + ' with id:' + str(data['id']) + ' is created in database')
    return True


def update_data(data: dict, collection_name: str):
    """
    Update documentation using info in data dict
    :param data: data in python dict
    :param collection_name: should exist in database
    :return:True if success
    """
    if collection_name not in database.list_collection_names():
        print("Collection not exist")
        return False

    curr_collection = database[collection_name]
    curr_id = data['id']
    for key in data:
        if key != 'id':
            curr_collection.update_one({'id': curr_id}, {"$set": {key: data[key]}})
    print(collection_name + ' with id:' + str(data['id']) + ' is updated in database')
    return True


def delete_data(collection_name: str, data_id: str):
    """
    Delete documentation with given id
    :param collection_name: should exist in database
    :param data_id: id of documentation
    :return:True if success
    """
    if collection_name not in database.list_collection_names():
        print("Collection not exist")
        return False

    curr_collection = database[collection_name]
    curr_collection.delete_one({'id': data_id})
    return True


def export_data_json(file_name: str, collection_name: str, id_list):
    """
    Export request documentation in a collection to json
    :param file_name: file to store result
    :param collection_name: name of collection for query
    :param id_list: list of id of request doc
    :return: None
    """
    result_list = []
    if id_list is None:
        query_result = database[collection_name].find({}, {'_id': 0})
    else:
        query_result = database[collection_name].find({'id': {'$in': id_list}}, {'_id': 0})
    for result in query_result:
        result_list.append(result)

    with open(file_name, 'w') as export_file:
        json.dump(result_list, export_file, indent=2)
        print("data has been export to " + file_name)
