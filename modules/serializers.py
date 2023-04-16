from rest_framework import serializers
from .models import *

# сериализатор на более низком уровне
class Edu_ModuleSerializer(serializers.Serializer):
    title = serializers.CharField(max_length=100)
    description = serializers.CharField(max_length=255)

    def create(self, validated_data):
        return Edu_module.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.title = validated_data['title']
        instance.description = validated_data['description']
        instance.save()
        return instance

# сериализатор в абстрактном виде
class SectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Section
        fields = '__all__'