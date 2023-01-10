from fastapi import FastAPI, File, UploadFile
from pyspark.sql import SparkSession
from models import Movies
from typing import List
from fastapi.middleware.cors import CORSMiddleware
import jsondb
from hashlib import new
from sqlalchemy import null

#  uvicorn main:app --reload

app = FastAPI()

origins = [
    "http://localhost.tiangolo.com",
    "https://localhost.tiangolo.com",
    "http://localhost",
    "http://localhost:8080",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


#spark = SparkSession.builder.appName("API").getOrCreate()

movieDb: List[Movies] = []

moviedbfile = jsondb.read_json("moviesDb.json")

for movie in moviedbfile:
    if (type(movie["Released_Year"]) != int):
        movie["Released_Year"] = 1990
    a = Movies(**movie)
    movieDb.append(a)

# get all products from productdb
@app.get("/movies")
async def get_movies():
    return movieDb
