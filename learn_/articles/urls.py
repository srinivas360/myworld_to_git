from django.urls import path, re_path
# from django.urls import url
from . import views
# from ..learn_ import views

app_name = 'articles'

urlpatterns = [
    path('', views.article_list, name='list'),
    # path('detail', views.article_detail)
    path('create/', views.article_create, name="create"),
    re_path('^(?P<slug>[\w-]+$)', views.article_detail, name='detail'),
]