from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=100, verbose_name='Nome')
    slug = models.SlugField(null=False, unique=True)
    description = models.CharField(max_length=300, verbose_name='Descrição')
    price = models.FloatField(verbose_name='Preço')
    quantity = models.IntegerField(verbose_name='Quantidade')
    
    def __str__(self):
        return self.name
