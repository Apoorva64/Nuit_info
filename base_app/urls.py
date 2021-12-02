from base_app import views
from django.urls import path

app_name = 'base_app'
urlpatterns = [path('', views.index_view, name='index')]
