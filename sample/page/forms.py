from django import forms
from .models import Good, Category, BlogArticle
from .validaters import validate_positive


# NAME_ERROR_LIST = {'name':{'required':'Укажите название товара',
#                            'min_length':'Слишком короткое название',
#                            'max_length':'Слишком длинное название'}}


# class GoodForm(ModelForm):
#     class Meta:
#         model = Good
#         fields = ['name', 'description', 'in_stock']
#         labels = {'name': 'Название',
#                   'descriptions':'Описание',
#                   'in_stock':'Есть в наличии'}
#         help_texts = {'name':'Должно быть уникальным'}
#         error_messages = {'name':{'required':'Укажите название товара',
#                                   'min_length':'Слишком короткое название',
#                                   'max_length':'Слишком длинное название'}}
#         widgets = {'description':forms.Textarea, 'category':forms.RadioSelect}
#         required_css_class = 'required'
#         error_css_class = 'error'

#     def clean(self):
#         clean_data = super(GoodForm, self).clean()
#         if clean_data['price'] == clean_data['new_price']:
#             raise ValueError('Цена с учетом скидки должна быть меньше!',
#                              code = 'invalid')
#         return clean_data


# class GoodForm(forms.ModelForm):
#     class Meta:
#         model = Good
#     name = forms.CharField(label='Название', help_text='Должно быть уникальным',
#                            error_messages = NAME_ERROR_LIST)
#     description = forms.CharField(widget=forms.Textarea, label='Описание')
#     category = forms.ModelChoiceField(queryset=Category.objects.all(),
#                                       label='Категория', empty_label=None)
#     price = forms.FloatField(label = 'Цена', validators = [validate_positive])
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


class LoginForm(forms.Form):
    username = forms.CharField(label='Имя')
    password = forms.CharField(widget=forms.PasswordInput, label='Пароль')