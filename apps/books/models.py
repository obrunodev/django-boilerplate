from django.db import models
from django.template.defaultfilters import slugify
from django.urls import reverse


class Book(models.Model):
    title = models.CharField(max_length=100)
    slug = models.SlugField()
    pages = models.IntegerField()
    author = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("books_update", kwargs={"pk": self.pk})

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        return super().save(*args, **kwargs)
