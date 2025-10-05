from fastapi import APIRouter, HTTPException
from ..services.scrapper_service import scrapper_service

router = APIRouter(tags=["scraper"])

@router.post("/olx/extract")
async def extract_olx_data():
    """
    Endpoint para executar o scraping da OLX.
    """
    try:
        result = await scrapper_service.try_run()
        
        if not result["success"]:
            raise HTTPException(status_code=400, detail=result["message"])
            
        return result
        
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Erro interno: {str(e)}")

@router.get("/olx/status")
async def get_scraper_status():
    """
    Endpoint para verificar o status do scraper.
    """
    return scrapper_service.get_scraper_status()