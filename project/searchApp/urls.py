from django.urls import path
from .views import SearchResultsListView, autocomplete
app_name='searchApp'
urlpatterns = [
    path('search/', SearchResultsListView.as_view(), name='searchResult'),
    path('autocomplete/', autocomplete, name='autocomplete'),
] 