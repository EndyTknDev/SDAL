from datetime import datetime
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
import os
from pathlib import Path
from .login.login_scrapper import login_scrapper


class OlxScrapper:
    def __init__(self):
        self.start_date = datetime.now()
        self.end_date = None
        self.is_running = False
        self.driver = None

    def _ensure_profile_path(self, path: str) -> str:
        if not path:
            return ""
        p = Path(path).expanduser()
        if not p.exists():
            raise FileNotFoundError(f"Profile path não existe: {p}")
        return str(p)

    def set_driver(self, options: Options, headless: bool = True, profile_path: str = None):
        if headless:
            options.add_argument("--headless")
        profile_path = self._ensure_profile_path(profile_path) if profile_path else None
        if profile_path:
            profile = webdriver.FirefoxProfile(profile_path)
            self.driver = webdriver.Firefox(firefox_profile=profile, options=options)
        else:
            self.driver = webdriver.Firefox(options=options)
        
    def start(self):
        self.is_running = True
        self.start_date = datetime.now()
        self.set_driver(Options(), headless=False, profile_path=os.getenv("FIREFOX_PROFILE_PATH"))

    def end(self):
        self.is_running = False
        self.end_date = datetime.now()
        if self.driver:
            self.driver.quit()
            self.driver = None

    def scrappe(self):
        self.start()
        self.on_login()
        self.end()

    def on_login(self):
        self.driver = login_scrapper(self.driver)
        new_driver = webdriver.Firefox(options=Options().add_argument("--headless"))
        for cookie in self.driver.get_cookies():
            new_driver.add_cookie(cookie)
        self.driver.close()
        self.driver = new_driver
        print(self.driver.get_cookies())
