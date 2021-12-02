from base_app import views
from django.urls import path

app_name = 'base_app'
urlpatterns = [path('', views.index_view, name='index'),
               path('medal_of_honor_detail/<int:pk>/', views.MedalOfHonorDetailView.as_view(),
                    name="medal_of_honor_detail"),
               path('medal_of_honor_list/', views.MedalOfHonorListView.as_view(), name="medal_of_honor_list")
               ]
