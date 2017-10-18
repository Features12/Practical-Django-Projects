from django.http.response import  Http404
from django.shortcuts import render, redirect
from django.core.paginator import Paginator, InvalidPage
from django.views.generic.base import TemplateView

from page.forms import GoodForm
from page.models import Category, Good


# def index(request, id):
#     try:
#         page_num = request.GET['page']
#     except KeyError:
#         page_num = 1
#     cats = Category.objects.all().order_by('name')
#     if id == None:
#         cat = Category.objects.first()
#     else:
#         cat = Category.objects.get(id = id)
#     paginator = Paginator(Good.objects.filter(category = cat).order_by('name'), 10)
#     try:
#         goods = paginator.page(page_num)
#     except InvalidPage:
#         goods = paginator.page(1)
#     return render(request, 'index.html', {'category': cat, 'cats':cats, 'goods':goods})


# def good(request, id):
#     try:
#         page_num = request.GET['page']
#     except KeyError:
#         page_num = 1
#     cats = Good.objects.all().order_by('name')
#     try:
#         good = Good.objects.get(id=id)
#     except Good.DoesNotExist:
#         raise Http404
#     return render(request, 'good.html', {'good':good, 'cats':cats, 'pn':page_num})


# class AboutView(TemplateView):
#     template_name = 'about.html'


# class GoodDetailView(TemplateView):
#     template_name = 'good.html'
#     def get_context_data(self, **kwargs):
#         context = super(GoodDetailView, self).get_context_data(**kwargs)
#         context['good'] = Good.objects.get(pk = id)
#         return context


def good_create(request, id):
    if id == None:
        cat = Category.objects.first()
    else:
        cat = Category.objects.get(id = id)
        if request.method == 'POST':
            form = GoodForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect('index', id = cat.id)
            else:
                return render(request, 'good_add.html',
                              {'category':cat, 'form': form})
        else:
            form = GoodForm(initial={'category':cat})
            return render(request, 'good_add.html', {'category':cat,
                                                     'form':form})

