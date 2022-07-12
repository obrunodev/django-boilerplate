from django.db import models


class BaseModel(models.Model):
    created_at = models.DateTimeField('Criado em', auto_now_add=True)
    updated_at = models.DateTimeField('Atualizado em', auto_now=True)

    class Meta:
        abstract = True


class Genre(BaseModel):
    name = models.CharField(max_length=50, verbose_name='Gênero')

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = 'Gênero'
        verbose_name_plural = 'Gêneros'


class Book(BaseModel):
    title = models.CharField(max_length=200, verbose_name='Título')
    author = models.CharField(max_length=200, verbose_name='Autor')
    genre = models.ForeignKey(Genre, on_delete=models.SET_NULL, null=True, verbose_name='Gênero')
    price = models.DecimalField(verbose_name='Preço', max_digits=10, decimal_places=2)

    def __str__(self):
        return self.title
        
    class Meta:
        verbose_name = 'Livro'
        verbose_name_plural = 'Livros'
