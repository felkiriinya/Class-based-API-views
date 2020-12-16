from django.conf.urls import url
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns=[
    url('^$',views.landing, name='landing'),
    url(r'^api/watches/$', views.WatchList.as_view()),
    url(r'^api/watches/(\d+)$', views.OneWatchType.as_view()),
    # url(r'^api/createonewatch/$', views.CreateOneWatch.as_view()),
]   