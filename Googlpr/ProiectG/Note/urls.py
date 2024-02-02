from django.urls import path
from . import views


urlpatterns = [
    path("", views.home, name="home"),
    path("update/<int:id>", views.update, name="update"),
    path("list", views.lista, name="list"),
    path("creat", views.creat, name="creat"),
    path("delete/<int:id>", views.delete, name="delete"),
    path("nota/<int:id>", views.nota, name="nota"),
]