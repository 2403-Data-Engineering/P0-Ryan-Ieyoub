import os
from dotenv import load_dotenv
import mysql.connector

load_dotenv()

def get_connection():
    return mysql.connector.connect(
        host=os.getenv("HOST"),
        user=os.getenv("DB_USER"),
        password=os.getenv("PASS"),
        database=os.getenv("DB"),
        port=os.getenv("PORT")
    )
