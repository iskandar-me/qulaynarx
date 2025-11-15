from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from api.routers.products import router as products_router  # absolute import

app = FastAPI(title="Products API")

# Routerni ulash
app.include_router(products_router, prefix="/products", tags=["Products"])


origins=[
    "http://localhost:5174",  # Vue dev server
    "http://127.0.0.1:5174",
    "https://qulaynarx.vercel.app/"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,       # ruxsat berilgan frontendlar
    allow_credentials=True,
    allow_methods=["*"],         # GET, POST, PUT, DELETE ...
    allow_headers=["*"],
)

# Root endpoint (ixtiyoriy, test uchun)
@app.get("/")
async def root():
    return {"message": "Products API ishlayapti"}
