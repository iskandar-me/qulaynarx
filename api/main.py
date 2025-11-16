from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routers.products import router as products_router  # absolute import

app = FastAPI(title="Products API")

# Routerni ulash
app.include_router(products_router, prefix="/products", tags=["Products"])


origins = [
    "http://localhost:5174",                 # local frontend
    "http://localhost:5173",                 # local frontend
    "http://127.0.0.1:5174",                 # local frontend
    "http://127.0.0.1:5173",                 # local frontend
    "https://qulaynarx.vercel.app"           # production frontend
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,      
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
async def root():
    return {"message": "Products API is working"}
