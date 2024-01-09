from django.urls import path, include
from . import views

app_name = 'menu'
urlpatterns = [
    path('', views.Firstview.as_view(), name='first'),
    path('menu/', views.HomeView.as_view(), name='home'),
    path('category/<slug:category_slug>/', views.HomeView.as_view(), name='category_filter'),
    path('<slug:slug>/', views.ProductDetailView.as_view(), name='product_detail'),
]
