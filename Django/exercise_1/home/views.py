from django.views.generic import ListView
from django.shortcuts import render
from .models import SiteUrlModel
from django.views.decorators.http import require_http_methods


@require_http_methods(['GET'])
def sites_view(request):
    sites = SiteUrlModel.objects.all()
    return render(request, 'exercise_1/index.html', {'sites': sites})


class SitesListView(ListView):
    model = SiteUrlModel
    template_name = 'exercise_1/index.html'
    context_object_name = 'sites'


