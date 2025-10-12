class PostOptions:
    def __init__(
        self,
        title: str | None,
        href: str | None,
        price: str | None,
        city: str | None,
        publish_date: str | None,
        district: str | None = None,
        phone: str | None = None,
        imgs_hrefs: list[str] | None = None
    ):
        self.title = title
        self.href = href
        self.price = price
        self.city = city
        self.publish_date = publish_date
        self.district = district
        self.phone = phone
        self.imgs_hrefs = imgs_hrefs
        

class Post:
    def __init__(self, options: PostOptions):
        self.title = options.title
        self.href = options.href
        self.price = options.price
        self.city = options.city
        self.publish_date = options.publish_date
        self.phone = options.phone
        self.imgs_hrefs = options.imgs_hrefs
        self.district = options.district

    def print(self):
        lines = ""
        for k, v in self.__dict__.items():
            lines += f"{k} - {v}\n" 
        lines += "\n"
        return lines
    
    def __repr__(self):
        return self.print()
        
        
    def __str__(self) -> str:
        return self.print()