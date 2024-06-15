class Category:
    name: str
    description: str
    product: list

    category_num = 0
    product_set = set()
    product_num = 0

    def __init__(self, name, description, product):
        self.name = name
        self.description = description
        self.product = product
        Category.category_num += 1
        Category.product_set.update(set(self.product))
        Category.product_num = len(Category.product_set)


class Product:
    name: str
    description: str
    price: float
    quality: int

    def __init__(self, name, description, price, quantity):
        self.name = name
        self.description = description
        self.price = round(price, 2)
        self.quality = quantity


product_1 = Product('Iphone', 'an Apple phone', 599.50, 20)
product_2 = Product('Ipod', 'an Apple media player', 249.50, 10)
product_3 = Product('IMac', 'an Apple computer', 1999.50, 5)
product_4 = Product('IMac', 'an Apple planchet', 449.50, 15)
category_1 = Category("Apple devises", "Some devises from Apple", [product_1, product_2, product_3, product_4])


product_5 = Product('Phone', 'a phone', 99.50, 120)
product_6 = Product('Player', 'a media player', 49.50, 210)
product_7 = Product('PC', 'a computer', 1999.50, 5)
product_8 = Product('planchet', 'a planchet', 99.50, 150)
category_2 = Category("Devises", "Some devises from Apple", [product_5, product_6, product_7, product_8])


