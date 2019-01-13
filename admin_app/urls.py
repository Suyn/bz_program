from django.urls import path

from admin_app import views

urlpatterns=[
    path("getcaptcha/",views.getcaptcha,name="getcaptcha"),
    path("login_page/",views.login_page,name="login_page"),
    path("login_logic/", views.login_logic, name="login_logic"),
    path("send_code/", views.send_code, name="send_code"),
    path("login_logic_phone/", views.login_logic_phone, name="login_logic_phone"),
    path("regist_page/", views.regist_page, name="regist_page"),
    path("regist_logic/", views.regist_logic, name="regist_logic"),
    path("check_captcha/",views.check_captcha,name="check_captcha"),
    path("check_phone/",views.check_phone,name="check_phone"),
    path("check_pwd/", views.check_pwd, name="check_pwd"),
    path("check_nike/", views.check_nike, name="check_nike"),
]