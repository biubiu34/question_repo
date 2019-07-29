from . import views
from django.conf.urls import url

urlpatterns = [
    url(r'^logtest/$', views.logtest, name="logtest"),
    # 注册  
    url(r'register/$', views.test, name="register"),
    # 登录  
    url(r'login/$', views.test, name="login"),
    # 退出  
    url(r'logout/$', views.test, name="logout"),
    # 忘记密码  
    url(r'password/forget/$', views.test, name="password_forget"),
    #  重置密码  
    url(r'password/reset/token/$',views.test, name="password_reset"),

]