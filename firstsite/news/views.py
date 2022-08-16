from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views.generic import ListView, DetailView, CreateView

from .models import News, Category
from .forms import NewsForm


# Create your views here.
class HomeNews(ListView):
    model = News
    template_name = 'news/home_list.html'
    context_object_name = 'news'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(HomeNews, self).get_context_data(**kwargs)
        context['title'] = 'Main page'
        return context

    def get_queryset(self):
        return News.objects.order_by('-created_at').filter(is_published=True)


class NewsByCategory(ListView):
    model = News
    template_name = 'news/home_list.html'
    context_object_name = 'news'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(NewsByCategory, self).get_context_data(**kwargs)
        context['title'] = Category.objects.get(pk=self.kwargs['category_id'])
        return context

    def get_queryset(self):
        return News.objects.order_by('-created_at').filter(category_id=self.kwargs['category_id'], is_published=True)

class ViewNews(DetailView):
    model = News
    context_object_name = 'news_item'

class CreateNews(CreateView):
    form_class = NewsForm
    template_name = 'news/add_news.html'

# def index(request):
#     news = News.objects.order_by('-created_at')
#     # res = '<h1>Спосок новостей</h1>'
#     # for item in news:
#     #     res += f'<div>\n<p>{item.title}</p>\n<p>{item.contetnt}</p>\n</div>\n<hr>\n'
#     # return HttpResponse(res)
#     context = {'news': news, 'title': 'THIS IS NEWS'}
#     return render(request, 'news/index.html', context)

# def get_category(request, category_id):
#     news = News.objects.filter(category_id=category_id)
#     category = Category.objects.get(pk=category_id)
#     return render(request, 'news/category.html', {'news': news, 'category': category})


# def view_news(request, news_id):
#     news_item = News.objects.get(pk=news_id)
#     return render(request, 'news/view_news.html', {'news_item': news_item})


# def add_news(request):
#     if request.method == 'POST':
#         form = NewsForm(request.POST)
#         if form.is_valid():
#             # print(form.cleaned_data)
#             news = form.save()
#             return redirect(news)
#     else:
#         form = NewsForm()
#     return render(request, 'news/add_news.html', {'form': form})
