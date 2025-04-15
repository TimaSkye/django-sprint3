from django.contrib import admin

from .models import Category, Location, Post
from core.admin import CategoryAdmin, LocationAdmin, PostAdmin

admin.site.empty_value_display = 'Не задано'

admin.site.register(Category, CategoryAdmin)
admin.site.register(Location, LocationAdmin)
admin.site.register(Post, PostAdmin)
