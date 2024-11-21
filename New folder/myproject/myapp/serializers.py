from django.contrib.auth.models import User  # Import User model
from rest_framework import serializers
from .models import Client, Project
from django.contrib.auth.models import User  # Import User model

class ClientSerializer(serializers.ModelSerializer):
    created_by = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = Client
        fields = ['id', 'client_name', 'created_at', 'updated_at', 'created_by']

class ProjectSerializer(serializers.ModelSerializer):
    client = serializers.PrimaryKeyRelatedField(queryset=Client.objects.all())
    users = serializers.PrimaryKeyRelatedField(many=True, queryset=User.objects.all())

    class Meta:
        model = Project
        fields = ['id', 'name', 'client', 'users', 'created_at', 'updated_at']

class ClientDetailSerializer(ClientSerializer):
    projects = ProjectSerializer(many=True, read_only=True)

    class Meta(ClientSerializer.Meta):
        fields = ClientSerializer.Meta.fields + ['projects']