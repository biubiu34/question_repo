from . import views
from django.conf.urls import url

urlpatterns = [
    url(r'^logtest/$', views.logtest, name="logtest"),

]