from selenium.webdriver.remote.webelement import WebElement

def first_text(section: WebElement, selector: str, value: str) -> str | None:
    try:
        return section.find_element(selector, value).text
    except:
        return None

def first_attr(section: WebElement, selector: str, value: str, attr: str) -> str | None:
    try:
        return section.find_element(selector, value).get_attribute(attr)
    except:
        return None