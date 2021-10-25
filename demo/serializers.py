from rest_framework import serializers
from .models import Project, ProjectRefImages


class ProjectRefImagesSerializer(serializers.ModelSerializer):
	class Meta:
		model = ProjectRefImages
		fields = ("image", )

class ProjectSerializer(serializers.ModelSerializer):
	images = ProjectRefImagesSerializer(many=True, write_only=True)
	class Meta:
		model = Project
		fields = "__all__"


	def create(self, validated_data):
		images = validated_data.pop("images")
		project = Project.objects.create(**validated_data)

		for image in images:
			ProjectRefImages.objects.create(project=project,\
				**image)

		return project