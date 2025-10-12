from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.common.by import By
from .post_card_handler import post_card_handler
from ....models.Imovel import Imovel
from ....models.Post import PostOptions
import re

def imoveis_sections_handler(sections: list[WebElement]):
    imoveis_sections = []
    for section in sections:
        post = post_card_handler(section)
        details = section.find_elements(By.CSS_SELECTOR, ".olx-adcard__detail")
        
        details_values = list(map(lambda d: d.text, details))
        bedrooms = details_values[0] if len(details_values) > 0 else None
        area = details_values[1] if len(details_values) > 1 else None
        parking_spaces = details_values[2] if len(details_values) > 2 else None
        bathrooms = details_values[3] if len(details_values) > 3 else None


        new_imovel = Imovel(
            post_options=PostOptions(
                href=post.href,
                title=post.title,
                price=post.price,
                city=post.city,
                district=post.district,
                publish_date=post.publish_date
            ),
            area=area,
            parking_spaces=parking_spaces,
            bathrooms=bathrooms,
            bedrooms=bedrooms
        )
        imoveis_sections.append(new_imovel)
        
    return imoveis_sections