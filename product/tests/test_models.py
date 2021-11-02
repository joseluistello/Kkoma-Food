from django.test import TestCase
from models import Category, Product

class CategoryModelTest(TestCase):

    @classmethod
    def setUpTestData(cls) -> None:
        Category.objects.create(name='Mariana', slug='/Mariana-505')

    def test_name_content(self):
        category = Category.objects.get(id=1)
        expected_object_name = f'{category.name}'
        self.assertEqual(expected_object_name, 'Mariana')

    def test_slug_content(self):
        category = Category.objects.get(id=1)
        expected_object_name = f'{category.slug}'
        self.assertEqual(expected_object_name, '/Mariana-505')

class ProductModelTest(TestCase):

    @classmethod
    def setUpTestData(cls) -> None:
        Product.objects.create(category='Bebidas', name='Pepsi', slug='/Pepsi-600-ml', description='Compre en paquetes de 6', price='$600', image='pepsi.jpge', thumbnail='pepsi1.jpge', data_added='500')

    def test_category_content(self):
        product = Product.objects.get(id=1)
        expected_object_name = f'{product.category}'
        self.assertEqual(expected_object_name, 'Bebidas')

    def test_name_content(self):
        product = Product.objects.get(id=1)
        expected_object_name = f'{product.name}'
        self.assertEqual(expected_object_name, 'Pepsi')

    def test_slug_content(self):
        product = Product.objects.get(id=1)
        expected_object_name = f'{product.slug}'
        self.assertEqual(expected_object_name, '/Pepsi-600-ml')

    def test_description_content(self):
        product = Product.objects.get(id=1)
        expected_object_name = f'{product.description}'
        self.assertEqual(expected_object_name, 'Compre en paquetes de 6')    

    def test_price_content(self):
        product = Product.objects.get(id=1)
        expected_object_name = f'{product.price}'
        self.assertEqual(expected_object_name, '$600')

    def test_image_content(self):
        product = Product.objects.get(id=1)
        expected_object_name = f'{product.image}'
        self.assertEqual(expected_object_name, 'pepsi.jpge')

    def test_thumbnail_content(self):
        product = Product.objects.get(id=1)
        expected_object_name = f'{product.thumbnail}'
        self.assertEqual(expected_object_name, 'pepsi1.jpge')

    def test_data_added_content(self):
        product = Product.objects.get(id=1)
        expected_object_name = f'{product.data_added}'
        self.assertEqual(expected_object_name, '500')
    