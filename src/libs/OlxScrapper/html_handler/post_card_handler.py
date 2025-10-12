from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from ..utils.web_element_helpers import first_text, first_attr
from ....models.Post import Post, PostOptions
import re 
def post_card_handler(post: WebElement) -> Post:
    title = first_text(post, By.CSS_SELECTOR, "h2.olx-adcard__title")
    href =first_attr(post, By.CSS_SELECTOR, "a.olx-adcard__link", "href")
    price = first_text(post, By.CSS_SELECTOR, "h3.olx-adcard__price")
    publish_date = first_text(post, By.CSS_SELECTOR, ".olx-adcard__date")
    address = first_text(post, By.CSS_SELECTOR, ".olx-adcard__location")

    if (address == None):
        city = None
        district = None
    else:
        address_re = re.search(r'([\wÀ-ÖØ-öø-ÿ\s\.-]+),\s*([\wÀ-ÖØ-öø-ÿ\s\.-]+)', address)
        city = address_re.group(1) if address_re else None
        district = address_re.group(2) if address_re else None

    return Post(
        options=PostOptions(
            city=city,
            district=district,
            href=href,
            price=price,
            title=title,
            publish_date=publish_date,
        )
    )