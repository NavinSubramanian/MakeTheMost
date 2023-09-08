from django.urls import path
from . import views

urlpatterns = [
    path('',views.home, name="home"),
    path('ingridients/',views.ingridients, name="ingridients"),
    path('ingridients/<str:pk>',views.sepitem, name="seperateitems"),
]