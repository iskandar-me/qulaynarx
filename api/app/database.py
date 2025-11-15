import os
from motor.motor_asyncio import AsyncIOMotorClient
from dotenv import load_dotenv

load_dotenv()

mongo_url = os.getenv("MONGO_URL")
client = AsyncIOMotorClient(mongo_url)
db = client["products_db"]
products_collection=db.products
