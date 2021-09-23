from django.db import models
from django.urls import reverse_lazy

class Category(models.Model):
    title = models.CharField(max_length=150, db_index=True, verbose_name='Наименование')

    def get_absolute_url(self):
        return reverse_lazy('category', kwargs={"category_id":self.pk})

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'
        ordering = ['title']


class News(models.Model):
    title = models.CharField(max_length=150, db_index=True, verbose_name='Наименование')
    content = models.TextField(blank=True, verbose_name='Содержимое')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Создано')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Обновлено')
    photo = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True, verbose_name='Изображение')
    category = models.ForeignKey(Category, on_delete=models.PROTECT, verbose_name='Категория', null=True)
    is_published = models.BooleanField(default=True, verbose_name='Опубликовано')

    def get_absolute_url(self):
        return reverse_lazy('view_news', kwargs={"news_id":self.pk})

    def __str__(self):
        return self.title

    class Meta:
        verbose_name ='Новость'
        verbose_name_plural = 'Новости'
        ordering = ['-created_at']