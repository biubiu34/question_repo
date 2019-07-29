from django.conf.urls import url

from  . import views

urlpatterns = [
    #个人资料
    url(r"^profile/$",views.test,name='profile'),
    url(r"^change_passwd/$",views.test,name='change_passwd'),
    url(r"^answer/$",views.test,name='answer'),
    url(r"^comtribute/$",views.test,name='contribute'),
    url(r'^approval/$', views.test, name='approval'),
    url(r'^approval/id/$', views.test, name='approval_pass'),
]