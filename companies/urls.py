from django.urls import path
from .views import *

app_name = 'companies'

urlpatterns = [
    path('', CompanyListView.as_view(), name='company-list'),
    path('<int:pk>/', CompanyDetailView.as_view(), name='company-detail'),
    path('<int:pk>/update/', CompanyUpdateView.as_view(), name='company-update'),
    path('<int:pk>/delete/', CompanyDeleteView.as_view(), name='company-delete'),
    path('create/', CompanyCreateView.as_view(), name='company-create'),
]
