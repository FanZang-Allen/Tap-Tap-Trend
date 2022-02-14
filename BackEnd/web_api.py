""" This file is part of Tap Tap Web Scraper

Local web sever to handle good read api request
"""
from flask import Flask, request
from flask_cors import CORS, cross_origin
from BackEnd.database import database, exist_in_collection
from BackEnd import user_system
from BackEnd import web_api_utility

app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'


@app.route('/api/rank', methods=['GET'])
def get_rank_game():
    """
    Get ranking list in one region along with corresponding game info
    :return: query result or error message
    """
    region_name = web_api_utility.check_valid_region()
    if region_name is None:
        return {"Error_message": "Query arg region is not valid"}, 400
    game_id_cursor = database['Ranking'].find({'region': region_name}, {'id_list': 1, '_id': 0})
    game_id_list = game_id_cursor[0]['id_list']
    info_cursor = database['Game'].find({'id': {'$in': game_id_list}}, {'_id': 0})
    return {'Query Result': list(info_cursor)}, 200


@app.route('/api/genre', methods=['GET'])
def get_one_genre():
    """
    Get list of game in one genre
    :return: query result or error message
    """
    genre_name = web_api_utility.check_valid_genre()
    if genre_name is None:
        return {"Error_message": "Query arg genre is not valid"}, 400
    game_id_cursor = database['Genre'].find({'genre': genre_name}, {'id_list': 1, '_id': 0})
    game_id_list = game_id_cursor[0]['id_list']
    info_cursor = database['Game'].find({'id': {'$in': game_id_list}}, {'_id': 0})
    return {'Query Result': list(info_cursor)}, 200


@app.route('/api/game', methods=['POST'])
def get_games_info():
    """
    Get detail information of list of games in request body
    :return: query result or error message
    """
    if request.content_type != "application/json":
        return {"Error_message": "Content type should be application/json"}, 415
    id_list = web_api_utility.check_valid_games_id()
    if id_list is None:
        return {"Error_message": "Provided body is invalid"}, 400
    query_result = database['Game'].find({'id': {'$in': id_list}}, {'_id': 0})
    return {'Query Result': list(query_result)}, 200


@app.route('/api/search', methods=['GET'])
def search_games():
    """
    Search game collection using query string
    :return: query result or error message
    """
    query_exp = web_api_utility.check_valid_query_str()
    if query_exp is None:
        return {"Error_message": "Query arg query is invalid"}, 400
    query_result = database['Game'].find(query_exp, {'_id': 0})
    return {'Query Result': list(query_result)}, 200


if __name__ == "__main__":
    app.run(debug=True)
