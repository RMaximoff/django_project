import json
from django.core.management import BaseCommand
from catalog.models import Category, Product, Version
from django.db import connection

from users.models import User


class Command(BaseCommand):

    def handle(self, *args, **kwargs):

        Category.objects.all().delete()
        Product.objects.all().delete()
        Version.objects.all().delete()

        with connection.cursor() as cursor:
            cursor.execute("ALTER SEQUENCE catalog_category_id_seq RESTART WITH 1;")
            cursor.execute("ALTER SEQUENCE catalog_product_id_seq RESTART WITH 1;")
            cursor.execute("ALTER SEQUENCE catalog_version_id_seq RESTART WITH 1;")

        with open('category.json', 'r', encoding='utf-8') as file:
            categories = json.load(file)

            categories_for_create = []
            for category_data in categories:
                category_fields = category_data['fields']
                category_instance = Category(**category_fields)
                categories_for_create.append(category_instance)
            Category.objects.bulk_create(categories_for_create)

        with open('product.json', 'r', encoding='utf-8') as file:
            products = json.load(file)

            products_for_create = []
            for product_data in products:
                product_fields = product_data['fields']
                product_fields['category'] = Category.objects.get(pk=product_fields['category'])
                user_id = product_fields.pop('user')  # Получаем и удаляем идентификатор пользователя
                user = User.objects.get(id=user_id)  # Получаем экземпляр пользователя по идентификатору
                product_fields['user'] = user
                product_instance = Product(**product_fields)
                products_for_create.append(product_instance)
            Product.objects.bulk_create(products_for_create)

        with open('version.json', 'r', encoding='utf-8') as file:
            versions = json.load(file)

            versions_for_create = []
            for version_data in versions:
                version_fields = version_data['fields']
                version_fields['product'] = Product.objects.get(pk=version_fields['product'])
                version_instance = Version(**version_fields)
                versions_for_create.append(version_instance)
            Version.objects.bulk_create(versions_for_create)

