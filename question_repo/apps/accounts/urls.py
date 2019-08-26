from django.conf.urls import url
from django.views.generic import TemplateView
from . import views

#基于类的视图，就可以在视图函数的时候不需要进行if 判断get和post方法
urlpatterns = [
    # 注册
    url(r'register/$', views.Register.as_view(), name="register"),
    # 登录
    url(r'login/$', views.Login.as_view(), name="login"),
    # 退出
    url(r'logout/$', views.logout, name="logout"),
    # 忘记密码
    url(r'password/forget/$', views.test, name="password_forget"),
    # 重置密码
    url(r'password/reset/token/$',views.test, name="password_reset"),
]