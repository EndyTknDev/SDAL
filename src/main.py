from fastapi import FastAPI
from .api.scraper_routes import router as scraper_router
from .api.posts_routes import router as posts_router

app = FastAPI(
    title="SDAL API",
    description="API para scraping e gerenciamento de dados",
    version="1.0.0"
)

# Registra as rotas
app.include_router(scraper_router, prefix="/api/v1/scraper")
app.include_router(posts_router, prefix="/api/v1/posts")

@app.get("/")
async def root():
    return {"message": "SDAL API está funcionando!"}

@app.get("/health")
async def health_check():
    return {"status": "healthy"}
