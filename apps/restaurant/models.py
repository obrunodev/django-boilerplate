from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=100, verbose_name='Nome')
    slug = models.SlugField(null=False, unique=True)
    description = models.CharField(max_length=300, verbose_name='Descrição')
    category = models.ForeignKey(Category,
                                 on_delete=models.SET_NULL,
                                 blank=True,
                                 null=True)
    price = models.FloatField(verbose_name='Preço')
    quantity = models.IntegerField(verbose_name='Quantidade')

    def __str__(self):
        return self.name


class Purchase(models.Model):
    product = models.ForeignKey(Product, null=True, on_delete=models.SET_NULL)
    cost = models.FloatField()
    quantity = models.IntegerField()
    total_cost = models.FloatField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.product


class Cart(models.Model):
    product = models.ForeignKey(Product, null=True, on_delete=models.CASCADE)
    cost = models.FloatField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Sale(models.Model):
    value = models.FloatField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
