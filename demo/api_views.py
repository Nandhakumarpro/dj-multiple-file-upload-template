from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework import viewsets
from django.http import HttpResponse
from rest_framework.response import Response

from .serializers import ProjectSerializer, PandasSOResourceSerializer
from .models import Project, PandasSOResource

class ProjectView(viewsets.ModelViewSet):
	queryset = Project.objects.all()
	serializer_class = ProjectSerializer

	def create(self, request):
		serlzr = ProjectSerializer(data={**request.POST.dict(),\
					"images": [{"image":image} for image in\
					 request.FILES.getlist("images")]})

		if serlzr.is_valid(raise_exception=True):
			serlzr.save()
			return Response(serlzr.data, status=200)

		# return 

class PandasSOResourceView(viewsets.ModelViewSet):
	authentication_classes = [SessionAuthentication, BasicAuthentication]
	queryset = PandasSOResource.objects.all()
	serializer_class = PandasSOResourceSerializer

	