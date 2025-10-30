from pymongo import MongoClient
import pandas as pd

def load_books_from_mongo():
    client = MongoClient("mongodb://localhost:27017/")
    db = client["library_db"]
    books_collection = db["books"]
    books = list(books_collection.find({}, {"_id": 0}))  # exclude _id
    return pd.DataFrame(books)

from pymongo import MongoClient

def get_db():
    client = MongoClient("mongodb://localhost:27017/")
    return client["library_db"]
