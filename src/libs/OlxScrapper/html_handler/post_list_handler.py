from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class ListPageOptions:
    def __init__(self, country: str, category: str, page: int, min_price: int | None = None):
        self.country = country
        self.category = category
        self.page = page
        self.min_price = min_price

def post_list_handler(driver: WebDriver, options: ListPageOptions):
    driver.get(f"https://www.olx.com.br/{options.category}/venda/estado-{options.country}?ps={options.min_price}&o={options.page}")

    wait = WebDriverWait(driver, 20)
    container = wait.until(EC.presence_of_element_located(
        (By.CSS_SELECTOR, "div.AdListing_adListContainer__ALQla")
    ))

    sections = container.find_elements(By.TAG_NAME, "section")
    return sections