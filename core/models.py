from django.db import models

class Product(models.Model):

    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'

    title = models.CharField(max_length=300, verbose_name='Название продукта')
    description = models.CharField(max_length=500, verbose_name='Описание продукта', null=True)
    price = models.FloatField(verbose_name='Цена продукта', null=True)
    image = models.ImageField(verbose_name='Изображение',)
    avaliabled = models.BooleanField(default=True, verbose_name='Отображать на сайте')

    def __str__(self):
        return str(self.title)

class Order(models.Model):

    class Meta:
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'

    name = models.CharField(max_length=200, verbose_name='Имя заказчика')
    phone = models.CharField(max_length=20, verbose_name='Телефон')
    email = models.CharField(max_length=50, verbose_name='Email')
    products = models.ManyToManyField(Product, related_name='product', verbose_name='Продукты заказа')
