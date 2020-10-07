from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('wine/<slug:slug>/', views.PostDetailView.as_view(), name='post-detail'),
    path('countries/', views.CountryListView.as_view(), name='countries'),
    path('country/<slug:slug>/', views.CountryDetailView.as_view(), name='country-detail'),
    path('types/', views.TypeListView.as_view(), name='types'),
    path('type/<slug:slug>/', views.TypeDetailView.as_view(), name='type-detail'),
    path('varieties/', views.VarietyListView.as_view(), name='varieties'),
    path('variety/<slug:slug>/', views.VarietyDetailView.as_view(), name='variety-detail'),
]