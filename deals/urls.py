from django.urls import path
from .views import *

app_name = "deals"

urlpatterns = [
    path('', DealListView.as_view(), name='deal-list'),
    path('<int:pk>/', DealDetailView.as_view(), name='deal-detail'),
    path('<int:pk>/update/', DealUpdateView.as_view(), name='deal-update'),
    path('<int:pk>/delete/', DealDeleteView.as_view(), name='deal-delete'),
    path('create/', DealCreateView.as_view(), name='deal-create'),
    path('categories/', CategoryListView.as_view(), name='category-list'),
]
