from doctest import master
from django.db import models


class Genre(models.Model):
    name = models.CharField(max_length=50, verbose_name='Gênero')

    def __str__(self):
        return self.name


class Book(models.Model):
    title = models.CharField(max_length=200, verbose_name='Título')
    author = models.CharField(max_length=200, verbose_name='Autor')
    genre = models.ForeignKey(Genre, on_delete=models.SET_NULL, null=True, verbose_name='Gênero')
    price = models.DecimalField(verbose_name='Preço', max_digits=10, decimal_places=2)

    def __str__(self):
        return self.title
