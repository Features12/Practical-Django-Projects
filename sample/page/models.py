from django.db import models
from django.db.models.fields import PositiveSmallIntegerField
# from django.contrib.comments.moderation import CommentModerator, moderator
from django.core.urlresolvers import reverse
from taggit.managers import TaggableManager


# moderator.reqister(Blog, BlogModerator)


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
    thumbnail_width = PositiveSmallIntegerField()
    thumbnail_height = PositiveSmallIntegerField()
    thumbnail = models.ImageField(upload_to='goods/thumbnails/%Y/%m/%d', width_field=thumbnail_width,
                                  height_field=thumbnail_height)
    category = models.ForeignKey(Category, null=True, blank=True, on_delete=models.SET_NULL)
    tags = TaggableManager(blank=True, verbose_name='Тэги')

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

    def save(self, *args, **kwargs):
        try:
            this_record = Good.objects.get(id = self.id)
            if this_record.thumbnail != self.thumbnail:
                this_record.thumbnail.delete(save = False)
        except:
            pass
        super(Good, self).save(*args, **kwargs)


        # category = models.IntegerField(choices=CATEGORIES, default=1, db_index=True)

        # def get_in_stock(self):
        #     if self.in_stock:
        #         return '+'
        #     else:
        #         return ''

        def  get_absolute_url(self):
            return reverse('good', kwargs={'good_id': self.id})


class BlogArticle(models.Model):
    title = models.CharField(max_length=150, unique_for_month='pubdate')
    pubdate = models.DateField()
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'BlogArticle'
        permissions = (('can_blog', 'Ведение блога'),)


class New(models.Model):
    title = models.CharField(max_length=100, db_index=True)
    description = models.TextField()
    content = BBCodeTextField() # TextField но в формате BBcode [i]{TEXT}[/i]
    pub_date = models.DateField(db_index=True, auto_now_add=True)


class Blog(models.Model):
    title = models.CharField(max_length=120)
    body = models.TextField()
    pub_date = models.DateField(auto_now_add=True)
    enable_comments = models.BooleanField(default=True)


# class BlogModerator(CommentModerator):
#     enable_field = 'enable_comments'
#     email_notification = True
#     auto_moderate_field = 'pub_date'
#     moderate_after = 30