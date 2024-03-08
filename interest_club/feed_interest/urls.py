from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='feed'),
    path('search-groups/', views.SearchResultsView.as_view(), name='search-groups'),
    path("group/<int:pk>", views.PostDetailView.as_view(), name='group_inside')
]
