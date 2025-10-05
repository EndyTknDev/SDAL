from datetime import datetime
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from .login.login_scrapper import login_scrapper


class OlxScrapper:
    def __init__(self):
        self.start_date = datetime.now()
        self.end_date = None
        self.is_running = False
        self.driver = None
        
    def start(self):
        self.is_running = True
        self.start_date = datetime.now()
        self.driver = webdriver.Chrome()

    def end(self):
        self.is_running = False
        self.end_date = datetime.now()
        if self.driver:
            self.driver.quit()
            self.driver = None

    def scrapper(self):
        self.start()
        self.on_login()
        self.end()

    def on_login(self):
        self.driver = login_scrapper(self.driver)
        
        new_driver = webdriver.Chrome(options=Options().add_argument("--headless"))
        for cookie in self.driver.get_cookies():
            new_driver.add_cookie(cookie)
        self.driver.close()
        self.driver = new_driver
        print(self.driver.get_cookies())
