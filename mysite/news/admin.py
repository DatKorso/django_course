from django.contrib import admin

from .models import News, Category

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id','title')
    list_display_links = ('id', 'title')
    search_fields = ('title',)

class NewsAdmin(admin.ModelAdmin):
    list_display = ('id','title','created_at','updated_at','category', 'is_published')
    list_display_links = ('id', 'title')
    search_fields = ('id', 'title')
    list_editable = ('is_published',)
    list_filter = ('is_published', 'category')

admin.site.register(News, NewsAdmin)
admin.site.register(Category, CategoryAdmin)