from typing import Dict, Any
import asyncio
import logging


logger = logging.getLogger(__name__)

class ScrapperService:
    def __init__(self):
        self.is_running = False
    
    async def can_run(self) -> bool:
        return not self.is_running
 
    async def try_run(self):
        if (await self.can_run()) is False:
            raise ValueError("Scraper is already running.")
        task = asyncio.create_task(self._run_olx_scraper())
        return task

    async def _run_olx_scraper(self):
        result = await olx_scraper_runner()
        
        print(result)

# Instância singleton do service
scrapper_service = ScrapperService()
