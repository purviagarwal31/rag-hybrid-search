from django.urls import path
from .views import index, search_view
from pipeline.api import search_api

urlpatterns = [
    path('', index, name='home'),
    path('search/', search_view, name='search'),
    path('api/search/', search_api, name='search_api')
]
