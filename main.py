from fastapi import FastAPI
from src.api.scraper_routes import router as scraper_router
from src.api.posts_routes import router as posts_router
import uvicorn

app = FastAPI(
    title="SDAL API",
    description="API para scraping e gerenciamento de dados",
    version="1.0.0"
)

app.include_router(scraper_router, prefix="/api/v1/scraper")
app.include_router(posts_router, prefix="/api/v1/posts")

@app.get("/")
async def root():
    return {"message": "SDAL API está funcionando!"}
 
if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)