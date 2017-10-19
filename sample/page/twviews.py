from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin
from django.http.response import Http404
from django.shortcuts import redirect
from django.views.generic.base import TemplateView
from django.core.paginator import Paginator, InvalidPage
from django.forms.models import modelformset_factory, inlineformset_factory
from page.forms import GoodForm
from page.models import Category, Good


CategoryFormset = modelformset_factory(Category, labels={'name':'Название'},
                                       help_texts={'name':'Должно быть уникально'})
formset = CategoryFormset(queryset = Category.objects.order_by('-name'))

CategoryGoodFormset = inlineformset_factory(Category, Good)

# class GoodListView(TemplateView):
#     template_name = 'index.html'
#     def get_context_data(self, **kwargs):
#         context = super(GoodListView, self).get_context_data(**kwargs)
#         try:
#             page_num = self.request.GET['page']
#         except KeyError:
#             page_num = 1
#         context['cats'] = Category.objects.order_by['name']
#         if kwargs['id'] == None:
#             context['cats'] = Category.objects.first()
#         else:
#             context['category'] = Category.objects.get(id = kwargs['id'])
#         paginator = Paginator(Good.objects.filter(category = context['category']).order_by('name'), 1)
#         try:
#             context['goods'] = paginator.page(page_num)
#         except InvalidPage:
#             context['goods'] = paginator.page(1)
#         return context


# class GoodDetailView(TemplateView):
#     template_name = 'good.html'
#     def get_context_data(self, **kwargs):
#         context = super(GoodDetailView, self).get_context_data(**kwargs)
#         try:
#             context['pn'] = self.request.GET['page']
#         except Good.DoesNotExist:
#             raise Http404
#         return context


class GoodCreate(SuccessMessageMixin ,TemplateView):
    form = None
    template_name = 'good_add.html'
    success_message = 'Товар успешно добавлен в список!'

    def get(self, request, *args, **kwargs):
        if self.kwargs['id'] == None:
            cat = Category.objects.first()
        else:
            cat = Category.objects.get(id = self.kwargs['id'])
        # try:
        #     in_stock = request.session['in_stock']
        # except:
        #     in_stock = True
        self.form = GoodForm(initial={'Category':cat, 'in_stock':request.session.get('in_stock', True)})
        return  super(GoodCreate, self).get(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        if self.kwargs['id'] == None:
            cat = Category.objects.first()
        else:
            cat = Category.objects.get(id = self.kwargs['id'])
        self.form = GoodForm(request.POST)
        if self.form.is_valid():
            request.session['in_stock'] = self.form.cleaned_data['in_stock']
            self.form.save()
            messages.add_message(request, messages.SUCCESS,'Товар успешно добавлен в список')
            return redirect('index', id = cat.id)
        return super(GoodCreate, self).post(request, *args, **kwargs)
        
    def get_context_data(self, **kwargs):
        context = super(GoodCreate, self).get_context_data(**kwargs)
        context['form'] = self.form
        return context

    def post(self, request, *args, **kwargs):
        if self.kwargs['id'] == None:
            cat = Category.objects.first()
        else:
            cat = Category.objects.get(id = self.kwargs['id'])
        self.form = GoodForm(request.POST)
        if self.form.is_valid():
            self.form.save()
            return redirect('index', id = cat.id)
        else:
            return super(GoodCreate, self).post(request, *args, **kwargs)


class GoodUpdate(TemplateView):
    form = None
    template_name = 'good_edit.html'

    def get(self, request, *args, **kwargs):
        self.form = GoodForm(instance=Good.objects.get(id = self.kwargs['id']))
        return super(GoodUpdate, self).get(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super(GoodUpdate, self).get_context_data(**kwargs)
        context['good'] = Good.objects.get(id = self.kwargs['id'])
        context['form'] = self.form
        return context
    
    def post(self, request, *args, **kwargs):
        good = Good.objects.get(id = self.kwargs['id'])
        self.form = GoodForm(request.POST, instance=good)
        if self.form.is_valid():
            self.form.save()
            return redirect('index', id = good.category.id)
        else:
            return super(GoodUpdate, self).post(request, *args, **kwargs)