from django.conf.urls import url
from django.views.generic import TemplateView
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^question/$', views.QuestionsList.as_view(), name="questions"),
    # url(r'^question_detail/(?P<id>\d+)/$', views.QuestionsDetail.as_view(), name="question_detail"),
    url(r'^question/(?P<id>\d+)/$', views.QuestionDetail.as_view(), name="question_detail"),

]