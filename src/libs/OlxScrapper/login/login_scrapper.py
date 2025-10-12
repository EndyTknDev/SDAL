from selenium.webdriver.remote.webdriver import WebDriver
from ..utils.wait_for_cookie import wait_for_cookie

def login_scrapper(driver: WebDriver):
    driver.get("https://www.olx.com.br/")
    
    wait_for_cookie(driver, "loginidentifier", timeout=300)

    return driver.get_cookies()
