from django.urls import path
from .views import ConfigurationUpdateView

app_name = 'config'

urlpatterns = [
    path('general/<int:pk>/', ConfigurationUpdateView.as_view(), name='general')
]
