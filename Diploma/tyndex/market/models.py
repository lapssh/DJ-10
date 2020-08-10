from django.db import models
from django.contrib.auth.models import User


class Section(models.Model):
    name = models.CharField(max_length=50, verbose_name='Наименование раздела')
    slug = models.SlugField(max_length=50, unique=True)

    class Meta:
        verbose_name = 'Раздел'
        verbose_name_plural = 'Разделы'

    def __str__(self):
        return self.name


class Category(models.Model):
    name = models.CharField(max_length=50, verbose_name='Наименование категории')
    section = models.ForeignKey(
        Section, related_name='categories', on_delete=models.PROTECT, verbose_name='Раздел'
    )
    slug = models.SlugField(max_length=50, unique=True)

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=100, verbose_name='Товар')
    price = models.DecimalField(max_digits=12, blank=False, verbose_name='Цена', decimal_places=2, default=0)
    product_number = models.IntegerField(blank=False, verbose_name='Артикул товара', unique=True)
    img = models.ImageField(upload_to='media/img/', blank=True, verbose_name='Изображение')
    category = models.ForeignKey(Category, related_name='products',
                                 on_delete=models.PROTECT, verbose_name='Категория')
    slug = models.SlugField(max_length=100, unique=True)
    description = models.CharField(max_length=512, verbose_name='Описание')

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'

    def __str__(self):
        return self.name


class Article(models.Model):
    title = models.CharField(max_length=200, verbose_name='Кликбейтный заголовок')
    text = models.TextField(max_length=1500, verbose_name='Содержание статьи')
    published = models.DateTimeField(auto_now_add=True, verbose_name='Дата публикации')
    products = models.ManyToManyField(Product, verbose_name='Связанные товары', blank=True)

    class Meta:
        verbose_name = 'Статья'
        verbose_name_plural = 'Статьи'

    def __str__(self):
        return self.title


class Customer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='customer')
    register_date = models.DateTimeField(auto_now_add=True, verbose_name='Дата регистрации')

    class Meta:
        verbose_name = 'Покупатель'
        verbose_name_plural = 'Покупатели'

    def __str__(self):
        return self.user.username


class Order(models.Model):
    customer = models.ForeignKey(Customer, related_name='customer',
                                 on_delete=models.CASCADE, verbose_name='Покупатель')
    products = models.ManyToManyField(Product, verbose_name='Товары', blank=True, through='ProductsInOrder')
    created = models.DateTimeField(auto_now_add=True, verbose_name='Дата и время создания')

    class Meta:
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'

    def __str__(self):
        return f'{self.customer} - {self.created}'


class ProductsInOrder(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, verbose_name='Заказ')
    product = models.ForeignKey(Product, on_delete=models.PROTECT, verbose_name='Товар',
                                related_name='count_in_order', )
    quantity = models.PositiveSmallIntegerField(verbose_name='Количество единиц товара')
