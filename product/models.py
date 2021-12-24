from django.contrib.auth import get_user_model
from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models
from django.db.models.functions import datetime

User = get_user_model()


class Category(models.Model):  # Категории продукта
    name = models.CharField(max_length=50, unique=True)
    slug = models.SlugField(max_length=50, primary_key=True)

    def __str__(self):
        return self.name


class Brand(models.Model):  # Фирмы производители
    name = models.CharField(max_length=50, unique=True)
    slug = models.SlugField(max_length=50, primary_key=True)

    def __str__(self):
        return self.name


class GroupProduct(models.Model):  # Группы товаров
    name = models.CharField(max_length=50, unique=True)
    slug = models.SlugField(max_length=50, primary_key=True)

    def __str__(self):
        return self.name


CHOICES = (
    ('in_stock', 'В наличии'),
    ('out_of_stock', 'Нет в наличии')
)


class Product(models.Model):  # Товары

    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=10,
                                decimal_places=2)

    category = models.ForeignKey(Category, on_delete=models.RESTRICT, related_name='products')

    image = models.ImageField(upload_to='products', null=True, blank=True)  # Добавляем картинку
    status = models.CharField(choices=CHOICES, max_length=20)  # статусы в наличии или нет
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE, related_name='product')  # ссылка на производитель
    group = models.ForeignKey(GroupProduct, on_delete=models.CASCADE, related_name='product')  # ссылка на группу

    class Meta:
        ordering = ['price']  # сортировка по цене

    def __str__(self):
        return self.name


class Comment(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='comment')
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='comment')
    text = models.TextField()
    rating = models.SmallIntegerField(
        validators=[
            MinValueValidator(1),
            MaxValueValidator(5)
        ])

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.author} - {self.created_at}'  # отображает автора коммента и время
