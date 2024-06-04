from src.classes import Category, Product


def test_category_number():
    assert Category.category_num == 2


def test_product_number():
    assert Category.product_num == 8


def test_class_product():
    assert type(Product('Iphone', 'an Apple phone', 599.50, 20)) == Product


def test_class_category():
    assert type(Category("Apple", "devices from Apple", [])) == Category
