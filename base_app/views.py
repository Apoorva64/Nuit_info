from django.shortcuts import render
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from base_app import models
from django.db.models import CharField
from django.db.models import Q


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


class RescueDetailView(DetailView):
    model = models.Rescue
    template_name = 'detail_views/rescue_detail.html'

class RescueListView(ListView):
    model = models.Rescue
    template_name = 'list_views/rescue_list.html'


def search_page(request):
    if request.method == 'POST':
        print(request.POST)
        string = request.POST.get('search_query')
        rescue_result = models.Rescue.objects.filter(description__contains=string)
        rescue_boat_result = models.RescueBoat.objects.filter(name__contains=string)
        rescued_boat_result = models.RescuedBoat.objects.filter(name__contains=string)
        medal_of_honor_result = models.MedalOfHonor.objects.filter(name__contains=string)
        rescuer_result = models.Rescuer.objects.filter(last_name__contains=string)
        rescue_station_result = models.RescueStation.objects.filter(name__contains=string)

        # rescue_boat_result = models.RescueBoat.objects.annotate(search=SearchVector('name', 'id_plate')).filter(
        #     search=string)
        # rescued_boat_result = models.RescuedBoat.objects.annotate(search=SearchVector('name', 'id_plate')).filter(
        #     search=string)
        #
        # medal_of_honor_result = models.RescueBoat.objects.annotate(search=SearchVector('name', 'description')).filter(
        #     search=string)
        #
        # rescuer_result = models.Rescuer.objects.annotate(
        #     search=SearchVector('first_name', 'last_name', 'description', 'birth_date', 'death_date')).filter(
        #     search=string)
        # rescue_result = models.RescueBoat.objects.annotate(search=SearchVector('description')).filter(
        #     search=string)

        return render(request, 'search.html', {'search': string,
                                               'results': [rescue_result, rescuer_result, rescue_boat_result,
                                                           rescued_boat_result, medal_of_honor_result,
                                                           rescue_station_result]})
    else:
        return render(request, 'search.html', {})
