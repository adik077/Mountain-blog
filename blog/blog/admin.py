from django.contrib import admin
from .models import Post, Category, Profile, Comments


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    search_fields = ['title','author','creation_date','is_active','is_highlited']
    list_display = ['title','author','creation_date','is_active','is_highlited']
    list_filter = ['creation_date']


admin.site.register(Category)
admin.site.register(Profile)
admin.site.register(Comments)



