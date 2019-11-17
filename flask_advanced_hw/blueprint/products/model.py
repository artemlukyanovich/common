import uuid


class Product:
    def __init__(self, name, description, img_name, price):
        self.id = self.id = str(uuid.uuid4())
        self.name = name
        self.description = description
        self.img_name = img_name
        self.price = price

