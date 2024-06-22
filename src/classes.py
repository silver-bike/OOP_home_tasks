class Category:
    name: str
    description: str
    product: list

    category_num = 0
    __product_set = set()
    product_num = 0

    def __init__(self, name, description, product):
        self.name = name
        self.description = description
        self.__product = product
        self.add_category()
        self.add_product(product)

    @classmethod
    def add_category(cls):
        cls.category_num += 1

    @classmethod
    def add_product(cls, product):
        cls.__product_set.update(set(product))
        cls.product_num = len(cls.__product_set)

    @property
    def show_products_in_stock(self):
        lst = self.__product
        return [(f'{product.name}, {product.price} руб. Остаток: '
                 f'{product.quantity} шт.') for product in lst]

    def __len__(self):
        return len(self.__product)

    def __str__(self):
        return f'{self.name}, количество продуктов: {len(self)} шт.'


class Product:
    name: str
    description: str
    price: float
    quality: int

    def __init__(self, name, description, price, quantity):
        self.name = name
        self.description = description
        self.price = round(price, 2)
        self.quantity = quantity

    def __str__(self):
        return f'{self.name}, {self.price} руб. Остаток: {self.quantity} шт.'

    @classmethod
    def new_product(cls, name, description, price, quantity):
        return cls(name, description, price, quantity)

    @property
    def price_(self):
        return self.price

    @price_.setter
    def price_(self, new_price):
        if new_price > 0:
            self.price = round(new_price, 2)
        else:
            print('введена некорректная цена')

    def __add__(self, other):
        return self.price * self.quantity + other.price * other.quantity


# код для проверки

product_1 = Product('Iphone', 'an Apple phone', 599.50, 20)
product_2 = Product('Ipod', 'an Apple media player', 249.50, 10)
product_3 = Product('IMac', 'an Apple computer', 1999.50, 5)
product_4 = Product('IMac', 'an Apple planchet', 449.50, 15)
category_1 = Category("Apple devises", "Some devises from Apple",
                      [product_1, product_2, product_3, product_4])

product_5 = Product('Phone', 'a phone', 99.50, 120)
product_6 = Product('Player', 'a media player', 49.50, 210)
product_7 = Product('PC', 'a computer', 1999.50, 5)
product_8 = Product('planchet', 'a planchet', 99.50, 150)
category_2 = Category("Devises", "Some devises from Apple",
                      [product_5, product_6, product_7, product_8])

print(Category.category_num)
print(Category.product_num)
[print(x) for x in category_2.show_products_in_stock]
product_11 = Product.new_product('кубик рубика', 'головоломка', 9.50, 10)
print(product_11.price_)
product_11.price_ = 3.88
print(product_11)
print(category_1)
print(product_5 + product_5)
