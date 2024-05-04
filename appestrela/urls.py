from django.urls import path
from . import views


urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('cadastro/', views.cadastro, name='cadastro'),
    path('login/', views.login, name='login'),
    path('index', views.index, name='index'),
    path('post/<int:pk>/', views.post_detail, name='post_detail'),
    path('carousel/', views.carousel, name='carousel'),

]