from django.conf.urls import url
from django.views.generic.base import TemplateView
from .models import New
# from .twviews import GoodListView, GoodDetailView
from django.views.generic.dates import TodayArchiveView
from .lwviews import (GoodListView, GoodDetailView, NewsArchiveView,\
    YearArchiveView, DayArchiveView,)
from .CUDview import GoodDelete, GoodCreate, GoodUpdate


urlpatterns = (
    url(r'^(?:(?P<id>\d+))?$', GoodListView.as_view(), name='index'),
    url(r'^good/(?P<id>\d+)$', GoodDetailView.as_view(), name='good'),
    url(r'^about$', TemplateView.as_view(), name='about'),
    url(r'^$', NewsArchiveView.as_view(), name='news_archive'),
    url(r'^(?P<year>\d{4})/$', YearArchiveView.as_view(), name='year_archive'),
    url(r'^(?P<year>\d{4})/(?P<month>\d+)/$', YearArchiveView.as_view(), name='month_archive'),
    url(r'^(?P<year>\d{4})/(?P<month>\d+)/(?P<day>\d+)/$', DayArchiveView.as_view(), name='day_archive'),
    url(r'^today/$', TodayArchiveView.as_view(model = New, date_field='pub_date', template_name='day_archive.html'),
                                              name='today_archive'),
    url(r'^(?P<id>\d+)/add/$', GoodCreate.as_view(), name='good_add'),
    url(r'^good/(?P<id>\d+)/edit/$', GoodUpdate.as_view(), name='good_edit'),
    url(r'^good/(?P<id>\d+)/delete/$', GoodDelete.as_view(), name='good_delete'),
)