from django.db import models
from django.urls import reverse
from markdown import markdown


class Category(models.Model):
    name = models.CharField(max_length=255)

    class Meta:
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.name


class Article(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField(max_length=4095)
    image = models.ImageField(
        upload_to='article_images',
        null=True,
        blank=True
    )
    author = models.ForeignKey(
        'auth.User',
        on_delete=models.CASCADE,
        null=True,
    )
    category = models.ForeignKey(
        Category,
        on_delete=models.PROTECT,
        null=True,
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('djappy:detail', kwargs={'pk':self.pk})

    def content_markdown(self):
        return markdown(self.content)
