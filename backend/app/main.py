from fastapi import FastAPI
from app.routes import receipts, ocr  # ✅ Import both from the same `app.routes`

app = FastAPI(
    title="CardWise AI Backend",
    description="Upload receipts or merchant pages to extract transaction insights",
    version="0.1.0"
)

# ✅ Register both routers
app.include_router(receipts.router)
app.include_router(ocr.router)

@app.get("/")
def root():
    return {"message": "CardWise AI backend running"}
