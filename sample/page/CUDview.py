from django.urls.base import reverse
from django.views.generic import CreateView, DeleteView, UpdateView
from django.views.generic.edit import ProcessFormView

from page.forms import GoodForm
from page.lwviews import CategoryListMixin
from .models import New, Category, Good, BlogArticle


class GoodEditMixin(CategoryListMixin):
    def get_context_data(self, **kwargs):
        context = super(GoodEditMixin, self).get_context_data(**kwargs)
        try:
            context['pn'] = self.request.GET['page']
        except KeyError:
            context['pn'] = '1'
        return context
    

class GoodEditView(ProcessFormView):
    def post(self, request, *args, **kwargs):
        try:
            pn = request.GET['page']
        except KeyError:
            pn = '1'
            self.success_url = self.success_url + '?page=' + pn
            return super(GoodEditView, self).post(request, *args, **kwargs)

class GoodCreate(CreateView, GoodEditMixin):
    model = Good
    template_name = 'good_add.html'
    form_class = GoodForm
    # success_url = '/'

    def get(self, request, *args, **kwargs):
        if self.kwargs['id'] != None:
            self.initial['category'] = Category.objects.get(pk = self.kwargs['id'])
        return super(GoodCreate, self).get(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        self.success_url = reverse('index', kwargs={'id':Category.objects.get(id=self.kwargs['id']).id})
        return super(GoodCreate, self).post(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super(GoodCreate, self).get_context_data(**kwargs)
        context['category'] = Category.objects.get(id = self.kwargs['id'])
        return context


class GoodUpdate(UpdateView, GoodEditMixin, GoodEditView):
    model = Good
    template_name = 'good_edit.html'
    pk_url_kwarg = 'id'
    form_class = GoodForm

    def post(self, request, *args, **kwargs):
        self.success_url = reverse('index',
                            kwargs={'id':Good.objects.get(id = self.kwargs['id']).category.id})
        return super(GoodUpdate, self).post(request, *args, **kwargs)


class GoodDelete(DeleteView, GoodEditMixin,GoodEditView):
    model = Good
    template_name = 'good_delete.html'
    pk_url_kwarg = 'id'

    def post(self, request, *args, **kwargs):
        self.success_url = reverse('index',
                        kwargs={'id': Good.objects.get(id = kwargs['id']).category.id})
        return super(GoodDelete, self).post(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super(GoodDelete, self).get_context_data(**kwargs)
        context['good'] = Good.objects.get(id = kwargs['id'])
        return context

