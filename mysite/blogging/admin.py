from django.contrib import admin
from .models import Post, Category

# Register your models here.


class CategoryInline(admin.TabularInline):
    model = Category.posts.through
    extra = 1


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    inlines = [CategoryInline]


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    exclude = ("posts",)
