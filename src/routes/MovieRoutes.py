from flask import Blueprint, jsonify

main = Blueprint('movie_blueprint', __name__)

@main.route('/')
def get_movies():
    return jsonify({'message': 'Welcome to the movies API'})