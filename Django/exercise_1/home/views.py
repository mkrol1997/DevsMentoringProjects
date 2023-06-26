from django.views.generic import ListView
from django.shortcuts import render
from .models import SiteUrlModel


def sites_view(request):
    sites = SiteUrlModel.objects.all()
    return render(request, 'exercise_1/home.html', {'sites': sites})


class SitesListView(ListView):
    model = SiteUrlModel
    template_name = 'exercise_1/home.html'
    context_object_name = 'sites'


