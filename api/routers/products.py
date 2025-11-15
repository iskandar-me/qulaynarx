# import collection from MongoDB
from api.database import products_collection


from fastapi import APIRouter, Query
from typing import List,Optional


router = APIRouter()

# Helper: ObjectId ni stringga aylantirish
def fix_product(product:dict) -> dict:
    product['_id']=str(product["_id"])
    return product

@router.get("/search")
async def search_products(
    name :str = Query(...,min_length=1, description="Searching by product name"),
    # name :Optional[str] = Query(None, description="Searching by product name"),
    page : int = Query(1,ge=1,description="Page number"),
    limit : int = Query(10,ge=1, le=50, description="Products per page"),
    min_price : Optional[float]= Query(None,description="Minimum price"),
    max_price : Optional[float]= Query(None,description="Maximum price"),
    market_name : Optional[str] = Query(None, description="Market name"),
    sort_by : Optional[str] = Query("current_price", description="Sort products by current_price"),
    sort_order : Optional[str] = Query("asc",description="asc or desc")
    ):

    skip=(page-1)*limit

    query = {"product_name": {"$regex": name, "$options": "i"}}

    # if name and name.strip():
        # query["product_name"] = {"$regex": name.strip(), "$options": "i"}

    if min_price is not None or max_price is not None:
        price_filter={}
        if min_price is not None:
            price_filter["$gte"]=min_price
        if max_price is not None:
            price_filter["$lte"]= max_price
        query["current_price"] = price_filter

    if market_name:
        query["market_name"] = {"$regex":market_name, "$options":"i"}

    # sort direction
    sort_dir=1 if sort_order.lower()=="asc" else -1

    # MongoDB query
    cursor=products_collection.find(query).sort(sort_by,sort_dir).skip(skip).limit(limit)

    results=[]

    async for product in cursor:
        product['_id']=str(product["_id"])
        results.append(product)

    total_count=await products_collection.count_documents(query)

    return {
        "page":page,
        "limit":limit,
        "total":total_count,
        "products":results
    }
