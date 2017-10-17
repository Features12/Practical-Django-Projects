from django.views.generic.base import ContextMixin
from django.views.generic.dates import ArchiveIndexView, YearArchiveView, MonthArchiveView, DayArchiveView
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView

from page.models import Category, Good, New


class CategoryListMixin(ContextMixin):
    def get_context_data(self, **kwargs):
        context = super(CategoryListMixin, self).get_context_data(**kwargs)
        context['cats'] = Category.objects.order_by('name')
        return context


# Список объектов
class GoodListView(ListView, CategoryListMixin):
    template_name = 'index.html'
    paginate_by = 10
    cat = None

    def get(self, request, *args, **kwargs):
        if self.kwargs['id'] == None:
            self.cat = Category.objects.first()
        else:
            self.cat = Category.objects.get(pk = self.kwargs['id'])
        return super(GoodListView, self).get(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super(GoodListView, self).get_context_data(**kwargs)
        # context['cats'] = Category.objects.order_by('name')
        context['category'] = self.cat
        return context

    def get_queryset(self):
        return Good.objects.filter(category = self.cat).order_by('name')


# Вывод на детальную страницу объектов из списка
class GoodDetailView(DetailView, CategoryListMixin):
    template_name = 'good.html'
    model = Good
    pk_url_kwarg = 'id'

    def get_context_data(self, **kwargs):
        context = super(GoodDetailView, self).get_context_data(**kwargs)
        try:
            context['pn'] = self.request.GET['page']
        except KeyError:
            context['pn'] = '1'
        # context['cats'] = Category.objects.order_by('name')
        return context


# Вывод по датам новостей
class NewsArchiveView(ArchiveIndexView):
    model = New
    date_field = 'pub_date'
    template_name = 'news_archive.html'

    def get_context_data(self, **kwargs):
        context = super(NewsArchiveView, self).get_context_data(**kwargs)
        context['cats'] = Category.objects.order_by['name']
        return context


# Вывод по годам
class YearNewsArchiveView(YearArchiveView):
    model = New
    date_field = 'pub_date'
    template_name = 'year_archive.html'
    make_object_list = True


# Вывод по месяцам
class MonthNewsArchiveView(MonthArchiveView):
    model = New
    date_field = 'pub_date'
    template_name = 'month_archive.html'
    make_object_list = True
    month_format = '%m'


# Вывод по дням
class DayNewsArchiveView(DayArchiveView):
    model = New
    date_field = 'pub_date'
    template_name = 'day_archive.html'
    make_object_list= True
    month_format = '%m'