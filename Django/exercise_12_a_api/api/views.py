from .models import BugModel
from .serializers import BugsSerializer
from django.http import Http404
from django.utils.decorators import method_decorator
from django.views.decorators.http import require_http_methods
from rest_framework import generics
from rest_framework.response import Response


@method_decorator(require_http_methods(["GET"]), name='dispatch')
class BugsView(generics.ListAPIView):

    queryset = BugModel.objects.all()
    serializer_class = BugsSerializer

    def list(self, request, *args, **kwargs):
        instance = self.filter_queryset(self.get_queryset())
        page = self.paginate_queryset(instance)
        if page is not None:
            serializer = self.get_pagination_serializer(page)
        else:
            serializer = self.get_serializer(instance, many=True)
        try:
            custom_representation = {'bugs': serializer.data}
        except TypeError:
            raise Http404
        return Response(custom_representation)

    def get_queryset(self):
        project_id = self.request.GET.get('project_id')
        user_id = self.request.GET.get('user_id')

        try:
            bugs = BugsView.find_bugs(project_id, user_id)
        except (ValueError, KeyError, AttributeError):
            raise Http404
        else:
            if not bugs:
                return Http404
            return bugs

    @staticmethod
    def find_bugs(project_id, user_id):

        filter_options = tuple(map(lambda x: True if x != '' else False, [project_id, user_id]))

        filter_by = {
            (True, False): 'BugModel.objects.filter(project=project_id)',
            (False, True): 'BugModel.objects.filter(user=user_id)',
            (True, True): 'BugModel.objects.filter(project=project_id, user=user_id)',
        }

        return eval(filter_by[filter_options])
