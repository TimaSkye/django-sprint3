from django.http import Http404
from django.shortcuts import render, get_object_or_404
from django.utils.timezone import now

from blog.models import Post, Category


def index(request) -> None:
    """Функция рендера главной страницы проекта."""
    post_list = Post.objects.filter(
        pub_date__lte=now(),
        is_published__exact=True,
        category__is_published__exact=True,
    ).order_by('-pub_date')[:5]
    return render(request, 'blog/index.html',
                  {'post_list': post_list})


def post_detail(request, post_id: int) -> None:
    """Функция рендера развернутой страницы поста."""
    post = get_object_or_404(Post, pk=post_id)
    if (post.pub_date > now() or not post.is_published
            or not post.category.is_published):
        raise Http404("Пост не найден или недоступен.")
    return render(request, 'blog/detail.html',
                  {'post': post})


def category_posts(request, category_slug: str) -> None:
    """Функция рендера страницы категорий поста."""
    category = get_object_or_404(Category, slug=category_slug)
    if not category.is_published:
        raise Http404("Категория не найдена или недоступна.")
    posts = Post.objects.filter(
        category__exact=category,
        is_published__exact=True,
        pub_date__lte=now(),
    ).order_by('-pub_date')

    context = {
        'category': category,
        'category_posts': posts,
    }
    return render(request, 'blog/category.html', context)
