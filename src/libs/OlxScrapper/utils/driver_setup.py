# ...existing code...
from selenium import webdriver
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium.webdriver.chrome.options import Options as ChromeOptions
import os

def setup_chrome_driver(headless: bool = True, profile_path: str = None):
    options = ChromeOptions()
    if headless:
        options.add_argument("--headless=new")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--disable-gpu")
    options.add_argument("--disable-extensions")
    options.add_argument("--disable-blink-features=AutomationControlled")
    options.add_experimental_option("excludeSwitches", ["enable-automation"])
    options.add_experimental_option("useAutomationExtension", False)

    if profile_path:
        p = os.path.expanduser(profile_path)
        base = os.path.basename(p)
        if base.lower() == "default":
            user_data_dir = os.path.dirname(p)
            options.add_argument(f"--user-data-dir={user_data_dir}")
            options.add_argument(f"--profile-directory=Default")
        else:
            options.add_argument(f"--user-data-dir={p}")

    driver = webdriver.Chrome(options=options)

    try:
        driver.execute_cdp_cmd(
            "Page.addScriptToEvaluateOnNewDocument",
            {"source": "Object.defineProperty(navigator, 'webdriver', {get: () => undefined})"}
        )
    except Exception:
        pass

    return driver

def setup_firefox_driver(headless: bool = True, profile_path: str = None):
    options = FirefoxOptions()
    if headless:
        options.add_argument("--headless")
    if profile_path:
        options.profile = webdriver.FirefoxProfile(profile_path)
    driver = webdriver.Firefox(options=options)
    return driver