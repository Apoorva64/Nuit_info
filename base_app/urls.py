from base_app import views
from django.urls import path

app_name = 'base_app'
urlpatterns = [path('', views.index_view, name='index'),
               path('medal_of_honor_detail/<int:pk>/', views.MedalOfHonorDetailView.as_view(),
                    name="medal_of_honor_detail"),
               path('medal_of_honor_list/', views.MedalOfHonorListView.as_view(), name="medal_of_honor_list"),

               path('rescue_boat_detail/<int:pk>/', views.RescueBoatDetailView.as_view(),
                    name="rescue_boat_detail"),
               path('rescue_boat_list/', views.RescueBoatListView.as_view(), name="rescue_boat_list"),

               path('rescue_station_detail/<int:pk>/', views.RescueStationDetailView.as_view(),
                    name="rescue_station_detail"),
               path('rescue_station_list/', views.RescueStationListView.as_view(), name="rescue_station_list"),

               path('rescued_boat_detail/<int:pk>/', views.RescuedBoatDetailView.as_view(),
                    name="rescued_boat_detail"),
               path('rescued_boat_list/', views.RescuedBoatListView.as_view(), name="rescued_boat_list"),

               path('rescuer_detail/<int:pk>/', views.RescuerDetailView.as_view(),
                    name="rescuer_detail"),
               path('rescuer_list/', views.RescuerListView.as_view(), name="rescuer_list"),

               path('search/', views.search_page, name="search"),

               path('rescue_detail/<int:pk>/', views.RescueDetailView.as_view(), name="rescue_detail"),
               path('rescue_list/', views.RescueListView.as_view(), name="rescue_list"),

               path('art_detail/<int:pk>/', views.ArtDetailView.as_view(), name="art_detail"),
               path('art_list/<int:pk>/', views.ArtListView.as_view(), name="art_list"),

               path('quote_detail/<int:pk>/', views.QuoteDetailView.as_view(), name="quote_detail"),
               path('quote_list/<int:pk>/', views.QuoteListView.as_view(), name="quote_list"),

               path('create_rescuer/', views.RescuerCreateView.as_view(), name="create_rescuer")

               ]
