from colorama import Cursor
import pymongo
import json
import models
from pymongo import MongoClient



client = MongoClient('mongodb://localhost:27017/')
mydb = client['ceng465']
collection_movies = mydb['movies']


async def fetch_one_user(movie_name):
    return await collection_movies.find_one({"_id": movie_name})


async def fetch_all_movies():
    movies = []
    cursor = collection_movies.find({})
    async for movie in cursor:
        movies.append(models.Movies(**movie))
    return movies



