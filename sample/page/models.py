from django.db import models

CATEGORIES = (
    (1, 'Metla'),
    (2, 'Venik'),
    (3, 'Schetki'),
)


class Category(models.Model):
    name = models.CharField(max_length=30, unique=True)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'Category'


# модель товара
class Good(models.Model):
    name = models.CharField(max_length=50, unique=True, verbose_name='Name')
    descriptions = models.TextField()
    in_stock = models.BooleanField(default=True, db_index=True, verbose_name='In Stock')
    price = models.FloatField(null=True, blank=True)
    category = models.ForeignKey(Category, null=True, blank=True, on_delete=models.SET_NULL)

    def __str__(self):
        s = self.name
        if not self.in_stock:
            s = s + ' (No in stock)'
        return s

    class Meta:
        db_table = 'Good'
        ordering = ['-price', 'name']
        unique_together = ('category', 'name')
        verbose_name = 'Tovar'
        verbose_name_plural = 'Tovars'

        # category = models.IntegerField(choices=CATEGORIES, default=1, db_index=True)

        # def get_in_stock(self):
        #     if self.in_stock:
        #         return '+'
        #     else:
        #         return ''


class BlogArticle(models.Model):
    title = models.CharField(max_length=150, unique_for_month='pubdate')
    pubdate = models.DateField()
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'BlogArticle'
