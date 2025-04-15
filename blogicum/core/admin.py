from django.contrib import admin


class CategoryAdmin(admin.ModelAdmin):
    """Настройка админ-панели модели Категории."""

    list_display = ('title', 'description', 'slug', 'is_published', 'created_at')
    list_editable = ('description', 'slug', 'is_published')
    search_fields = ('title',)
    list_filter = ('title',)
    list_display_links = ('title',)


class LocationAdmin(admin.ModelAdmin):
    """Настройка админ-панели модели Локации."""

    list_display = ('name', 'is_published', 'created_at')
    list_editable = ('is_published',)
    search_fields = ('name',)
    list_filter = ('name',)
    list_display_links = ('name',)


class PostAdmin(admin.ModelAdmin):
    """Настройка админ-панели модели Публикации."""

    list_display = (
        'title',
        'text',
        'pub_date',
        'author',
        'location',
        'category',
        'is_published',
        'created_at',
    )
    list_editable = (
        'text',
        'pub_date',
        'author',
        'location',
        'category',
        'is_published',
    )
    search_fields = (
        'title',
        'author',
        'location',
        'category',
    )
    list_filter = (
        'title',
        'pub_date',
        'author',
        'location',
        'category',
    )
    list_display_links = ('title',)
