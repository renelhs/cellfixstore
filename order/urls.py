from django.urls import path
from .views import DashboardView, OrderListView, OrderCreateView, OrderUpdateView, OrderDeleteView
from product.views import ProductAjaxView

app_name = 'order'

urlpatterns = [
    path('dashboard/', DashboardView.as_view(), name='dashboard'),
    path('list/', OrderListView.as_view(), name='list'),
    path('create/', OrderCreateView.as_view(), name='create'),
    path('update/<int:pk>/', OrderUpdateView.as_view(), name='update'),
    path('delete/<int:pk>/', OrderDeleteView.as_view(), name='delete'),
    path('product/ajax/', ProductAjaxView.as_view(), name='product_ajax'),
]
