from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.test, name='index'),
    url(r'^questions/$', views.test, name="questions"),
    url(r'^question/$', views.test, name="question"),
    # 题目详情，捕获了一个参数
    url(r'^question/id/$', views.test, name="question_detail"),
]