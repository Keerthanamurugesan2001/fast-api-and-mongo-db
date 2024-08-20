import os

from dotenv import load_dotenv
from urllib.parse import quote_plus

username = quote_plus(os.getenv('USERNAME'))
password = quote_plus(os.getenv('PASSWORD'))
connection_string = f"mongodb+srv://{username}:{password}@cluster0.oi1o4.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"
