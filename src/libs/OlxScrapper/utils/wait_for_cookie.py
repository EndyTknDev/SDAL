from selenium.webdriver.remote.webdriver import WebDriver
import time

def wait_for_cookie(driver: WebDriver, cookie_name: str, timeout: int = 300):
    end = time.time() + timeout
    while time.time() < end:
        if driver.get_cookie(cookie_name):
            print(cookie_name)
            return
        time.sleep(1)
    
    raise TimeoutError(f"Cookie '{cookie_name}' not found within {timeout} seconds.")
    