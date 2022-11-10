
from django.urls import include, path
from .import views
from django.contrib.auth.views import LoginView,LogoutView

urlpatterns = [
    path('inicio/', views.inicio, name = "inicio"),
    path('index/', views.indexView, name = "index"),
    path('login/',LoginView.as_view(),name="login_url"),
    path('register/',views.registerView,name="register_url"),
    path('logout/',LogoutView.as_view(),name="logout"),
]