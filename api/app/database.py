from motor.motor_asyncio import AsyncIOMotorClient

# MongoDB bilan ulanish
client = AsyncIOMotorClient("mongodb://localhost:27017")
db = client.products_db
products_collection = db.products
