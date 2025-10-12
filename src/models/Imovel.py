from .Post import Post, PostOptions

class Imovel(Post):
    def __init__(
        self,
        post_options: PostOptions,
        area: float = None,
        bedrooms: int | None = None,
        bathrooms: int | None = None,
        parking_spaces: int | None = None
    ):
        super().__init__(post_options)
        self.area = area
        self.bedrooms = bedrooms
        self.bathrooms = bathrooms
        self.parking_spaces = parking_spaces
    