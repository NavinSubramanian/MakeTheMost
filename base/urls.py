from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('home', views.home, name="home"),
    path('login/',views.LoginPage, name="Login"),
    path('logout/',views.logoutUser, name="Logout"),
    path('signup/',views.SignupPage, name="Register"),
    path('ingridients/', views.ingridients, name="ingridients"),
    path('ingridients/<str:pk>/', views.sepitem, name="seperateitems"),
    path('ingridients/<str:pk>/<str:pl>/', views.seprecipe, name="seperaterecipes"),
    path('ingridients/<str:pk>/<str:pl>/<str:ps>', views.recdetail, name="recipedetail"),
    path('searched/', views.search, name="search-ingi"),
    path('findrecipe/', views.findrecipe, name="findrecipe"),
]