from django import forms
from .models import Good, Category, BlogArticle


# class GoodForm(ModelForm):
#     class Meta:
#         model = Good
#         fields = ['name', 'description', 'in_stock']
#         labels = {'name': 'Название',
#                   'descriptions':'Описание',
#                   'in_stock':'Есть в наличии'}
#         help_texts = {'name':'Должно быть уникальным'}


# class GoodForm(forms.ModelForm):
#     class Meta:
#         model = Good
#     name = forms.CharField(label='Название', help_text='Должно быть уникальным')
#     description = forms.CharField(widget=forms.Textarea, label='Описание')
#     category = forms.ModelChoiceField(queryset=Category.objects.all(),
#                                       label='Категория', empty_label=None)
#     in_stock = forms.BooleanField(initial=True, label='Есть в наличии')


class BlogArticleForm(forms.ModelForm):

    class Meta:
        model = BlogArticle
    pub_date = forms.DateField(input_formats=['%j.%d.%y'])


class GoodForm(forms.Form):

    class Meta:
        model = Good
    name = forms.CharField(label='Название', help_text='Должно быть уникальным')
    description = forms.CharField(widget=forms.Textarea, label='Описание')
    category = forms.ModelChoiceField(queryset=Category.objects.all(),
                                      label='Категория', empty_label=None)
    in_stock = forms.BooleanField(initial=True, label='Есть в наличии')

    def get(self, request, *args, **kwargs):
        good = Good.objects.get(id = self.kwargs['id'])
        self.form = GoodForm({'name': good.name, 'description':good.descriptions,
                              'category':good.category, 'in_stock':good.in_stock})

    # def post(self, request, *args, **kwargs):
    #     pass
        