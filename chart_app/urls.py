from django.urls import path

from chart_app import views

urlpatterns=[
    path("demo/",views.demo,name="demo"),
]