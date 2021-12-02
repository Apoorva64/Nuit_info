from django.shortcuts import render
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from base_app import models


# Create your views here.
def index_view(request):
    return render(request, 'index.html')


class MedalOfHonorDetailView(DetailView):
    model = models.MedalOfHonor
    template_name = 'medal_of_honor_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


class MedalOfHonorListView(ListView):
    model = models.MedalOfHonor
    template_name = 'medal_of_honor_list.html'
