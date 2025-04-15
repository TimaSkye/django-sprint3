from django.http import Http404
from django.shortcuts import render


# posts_dict: dict[int, dict[str, str]] = {post['id']: post for post in posts}


def index(request) -> None:
    """Функция рендера главной страницы проекта."""
    return render(request, 'blog/index.html', {'posts': posts[::-1]})


def post_detail(request, post_id: int) -> None:
    """Функция рендера развернутой страницы поста."""
    post: dict[str, str] | None = posts_dict.get(post_id)
    if not post:
        raise Http404(f"Пост с id {post_id} не найден.")
    return render(request, 'blog/detail.html', {'post': post})


def category_posts(request, category_slug: str) -> None:
    """Функция рендера страницы категорий поста."""
    return render(request, 'blog/category.html', {'category_posts': category_slug})
