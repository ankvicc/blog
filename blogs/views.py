from django.shortcuts import render, redirect, get_object_or_404
from .models import BlogPost
from .forms import BlogPostForm

def index(request):
    """Главная страница блога, отображающая список записей."""
    posts = BlogPost.objects.order_by('-date_added')  # Записи сортируются по дате (новые сверху)
    context = {'posts': posts}
    return render(request, 'blogs/index.html', context)


# Страница "О блоге"
def about(request):
    return render(request, 'blogs/about.html')

# Страница "Контакты"
def contact(request):
    if request.method == 'POST':
        # Здесь может быть логика обработки формы
        message = request.POST.get('message', '')
        return render(request, 'blogs/contact.html', {'success': True})
    return render(request, 'blogs/contact.html')


def new_post(request):
    """Создание новой записи."""
    if request.method != 'POST':
        # Создаем пустую форму
        form = BlogPostForm()
    else:
        # Обрабатываем отправленные данные
        form = BlogPostForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('blogs:index')

    # Вывести пустую или недействительную форму
    context = {'form': form}
    return render(request, 'blogs/new_post.html', context)


def edit_post(request, post_id):
    """Редактирование существующей записи блога."""
    post = get_object_or_404(BlogPost, id=post_id)

    if request.method != 'POST':
        # Начальное заполнение формы текущими данными записи
        form = BlogPostForm(instance=post)
    else:
        # Обработка отправленных данных
        form = BlogPostForm(instance=post, data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('blogs:index')

    context = {'post': post, 'form': form}
    return render(request, 'blogs/edit_post.html', context)