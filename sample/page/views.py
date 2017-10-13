from django.http.response import  Http404
from django.shortcuts import render
from django.core.paginator import Paginator, InvalidPage
from page.models import Category, Good


def index(request, id):
    try:
        page_num = request.GET['page']
    except KeyError:
        page_num = 1
    cats = Category.objects.all().order_by('name'
    if id == None:
        cat = Category.objects.first()
    else:
        cat = Category.objects.get(id = id)
    paginator = Paginator(Good.objects.filter(categoy = cat).order_by('name'), 10)
    try:
        goods = paginator.page(page_num)
    except InvalidPage:
        goods = pag.page(1)
    return render(request, 'index.html', {'category': cat, 'cats':cats, 'goods':goods})


def good(request, id):
    try:
        page_num = request.GET['page']
    except KeyError:
        page_num = 1
    cats = Good.objects.all().order_by('name')
    try:
        good = Good.objects.get(id=id)
    except Good.DoesNotExist:
        raise Http404
    return render(request, 'good.html', {'good':good, 'cats':cats, 'pn':page_num})