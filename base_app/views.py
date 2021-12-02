from django.shortcuts import render
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from base_app import models


# Create your views here.
def index_view(request):
    return render(request, 'index.html')


class MedalOfHonorDetailView(DetailView):
    model = models.MedalOfHonor
    template_name = 'detail_views/medal_of_honor_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


class MedalOfHonorListView(ListView):
    model = models.MedalOfHonor
    template_name = 'list_views/medal_of_honor_list.html'


class RescueBoatDetailView(DetailView):
    model = models.RescueBoat
    template_name = 'detail_views/rescue_boat_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


class RescueBoatListView(ListView):
    model = models.RescueBoat
    template_name = 'list_views/rescue_boat_list.html'


class RescuedBoatDetailView(DetailView):
    model = models.RescuedBoat
    template_name = 'detail_views/rescued_boat_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


class RescuedBoatListView(ListView):
    model = models.RescuedBoat
    template_name = 'list_views/rescued_boat_list.html'


class RescuerDetailView(DetailView):
    model = models.Rescuer
    template_name = 'detail_views/rescuer_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


class RescuerListView(ListView):
    model = models.Rescuer
    template_name = 'list_views/rescuer_list.html'


class RescueStationDetailView(DetailView):
    model = models.RescueStation
    template_name = 'detail_views/rescue_station_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


class RescueStationListView(ListView):
    model = models.RescueStation
    template_name = 'list_views/rescue_station_list.html'

