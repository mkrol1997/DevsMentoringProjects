from .models import BugModel
from django.http import HttpResponse
from django.utils.decorators import method_decorator
from django.shortcuts import render
from django.views import View
from django.views.decorators.http import require_http_methods
import json


@method_decorator(require_http_methods(["GET"]), name='dispatch')
class BugsView(View):
    def get(self, request):
        project_id = request.GET.get('project_id', '')
        user_id = request.GET.get('user_id', '')

        try:
            bugs_query = BugsView.find_bugs(project_id, user_id)
        except (ValueError, KeyError):
            return render(request, 'bugs/index.html')

        bugs_query_json = [bug.json() for bug in bugs_query]
        if not bugs_query_json:
            return HttpResponse(status=404)
        return HttpResponse(json.dumps({'bugs': bugs_query_json}), content_type="application/json")

    @staticmethod
    def find_bugs(project_id, user_id):

        filter_options = tuple(map(lambda x: True if x != '' else False, [project_id, user_id]))

        filter_by = {
            (True, False): 'Bug.objects.filter(project=project_id)',
            (False, True): 'Bug.objects.filter(user=user_id)',
            (True, True): 'Bug.objects.filter(project=project_id, user=user_id)',
        }

        return eval(filter_by[filter_options])
