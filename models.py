from hashlib import new
from typing import List, Optional
from uuid import UUID, uuid4
from pydantic import BaseModel
from enum import Enum


class Movies(BaseModel):
    id: Optional[UUID] = uuid4()
    Poster_Link: str
    Series_Title: str
    Released_Year: int
    Certificate: str
    Runtime: str
    Genre: str
    IMDB_Rating: float
    Overview: str
    Director: str
    Star1: str
    Star2: str
    Star3: str
    Star4: str
    No_of_Votes: int
    Gross: str
