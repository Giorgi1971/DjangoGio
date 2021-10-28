from django.urls import path
from .views import *


app_name='group'

urlpatterns = [
    path('', GroupListView.as_view(), name='groups'),
    path('<int:pk>/', GroupDetailView.as_view(), name='group'),
    path('new/', GroupCreateView.as_view(), name='create_group'),
    path('<int:pk>/update/', GroupUpdateView.as_view(), name='group_update'),
    path('<int:pk>/delete/', GroupDeleteView.as_view(), name='group_delete'),
]