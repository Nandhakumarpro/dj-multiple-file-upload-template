from django.urls import path, include
from . import api_views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'projects', api_views.ProjectView, basename='project')
urlpatterns = router.urls

# urlpatterns = [
#  	path("project/", .as_view({"get": "list", "post": "create"}), name="project-views"),
#  ]