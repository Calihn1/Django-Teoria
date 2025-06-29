from django.urls import path
from .views import (
    LanguageListView, LanguageDetailView, LanguageDeleteView,
    FrameworkCreateView, FrameworkUpdateView, FrameworkDeleteView
)

app_name = 'examples'

urlpatterns = [
    path('', LanguageListView.as_view(), name='language-list'),
    path('<int:pk>/', LanguageDetailView.as_view(), name='language-detail'),
    path('create/', FrameworkCreateView.as_view(), name='framework-create'),
    path('<int:pk>/update/', FrameworkUpdateView.as_view(), name='framework-update'),
    path('<int:pk>/deleteFramework/', FrameworkDeleteView.as_view(), name='framework-delete'),
    path('<int:pk>/deleteLanguage/', LanguageDeleteView.as_view(), name='language-delete'),

]
