from django.test import TestCase
from .models import Category, Product

class CategoryModelTest(TestCase):

    @classmethod
    def setUpTestData(cls) -> None:
        Category.objects.create(name='first_name', slug='a slug here')

    def test_name_content(self):
        category = Category.objects.get(id=1)
        expected_object_name = f'{category.name}'
        self.assertEqual(expected_object_name, 'first_name')

    def test_slug_content(self):
        category = Category.objects.get(id=1)
        expected_object_name = f'{category.slug}'
        self.assertEqual(expected_object_name, 'a slug here')

class ProductModelTest(TestCase):

    @classmethod
    def setUpTestData(cls) -> None:
        Product.objects.create(category='', name='', slug='', description='', price='', image='', thumbnail='', data_added='')

    def test_category_content(self):
        product = Product.objects.get(id=1)
        expected_object_name = f'{product.}'
        self.assertEqual(expected_object_name, '')

    def test_category_content(self):
        product = Product.objects.get(id=1)
        expected_object_name = f'{product.}'
        self.assertEqual(expected_object_name, '')

    

    