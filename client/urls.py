from django.urls import path
from .views import ClientListView, ClientCreateView, ClientUpdateView, ClientDeleteView

app_name = 'client'

urlpatterns = [
    path('list/', ClientListView.as_view(), name='list'),
    path('create/', ClientCreateView.as_view(), name='create'),
    path('update/<int:pk>/', ClientUpdateView.as_view(), name='update'),
    path('delete/<int:pk>/', ClientDeleteView.as_view(), name='delete'),
]
