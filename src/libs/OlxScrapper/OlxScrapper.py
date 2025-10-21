from datetime import datetime
from selenium import webdriver
from selenium.webdriver.remote.webelement import WebElement
import os
from .html_handler.login_handler import login_handler
from .html_handler.post_list_handler import post_list_handler, ListPageOptions
from .html_handler.imoveis_sections_handler import imoveis_sections_handler
from dotenv import load_dotenv
from .utils.driver_setup import setup_firefox_driver, setup_chrome_driver

load_dotenv()

class OlxScrapper:
    def __init__(self, ):
        self.start_date = datetime.now()
        self.end_date = None
        self.is_running = False
        self.driver = None

    def handle_browser(self):
        browser = os.environ.get("BROWSER", "firefox").lower()
        if browser == "firefox":
            return setup_firefox_driver(profile_path=os.environ.get("FIREFOX_PROFILE_PATH"), headless=False)
        elif browser == "chrome":
            return setup_chrome_driver(profile_path=os.environ.get("CHROME_PROFILE_PATH"), headless=False)
        else:
            raise ValueError(f"Browser não suportado: {browser}")
        
    def start(self):
        self.is_running = True
        self.start_date = datetime.now()
        self.driver = self.handle_browser()

    def end(self):
        self.is_running = False
        self.end_date = datetime.now()
        if self.driver:
            self.driver.quit()
            self.driver = None

    def handle_login(self):
        login_handler(self.driver)

    def handle_pages(self, page):
        options = ListPageOptions(country="am", category="imoveis", page=page, min_price=1000)
        return post_list_handler(self.driver, options=options)

    def handle_imoveis_sections(self, sections: list[WebElement]):
        return imoveis_sections_handler(sections)                        
        
