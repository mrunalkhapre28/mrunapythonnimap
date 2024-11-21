# # Django REST API for Machine Test

# ## Project Setup
# 1. Create a Django project and app.
#    ```bash
#    django-admin startproject myproject
#    cd myproject
#    python manage.py startapp myapp
#    ```
# 2. Add `myapp` and `rest_framework` to `INSTALLED_APPS` in `settings.py`.

# ## Models
# ```python
# from django.contrib.auth.models import User
# from django.db import models

# class Client(models.Model):
#     client_name = models.CharField(max_length=100)
#     created_at = models.DateTimeField(auto_now_add=True)
#     updated_at = models.DateTimeField(auto_now=True)
#     created_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)

#     def __str__(self):
#         return self.client_name

# class Project(models.Model):
#     name = models.CharField(max_length=100)
#     client = models.ForeignKey(Client, on_delete=models.CASCADE, related_name='projects')
#     users = models.ManyToManyField(User)
#     created_at = models.DateTimeField(auto_now_add=True)
#     updated_at = models.DateTimeField(auto_now=True)

#     def __str__(self):
#         return self.name
# ```

# ## Serializers
# ```python
# from rest_framework import serializers
# from .models import Client, Project

# class ClientSerializer(serializers.ModelSerializer):
#     created_by = serializers.StringRelatedField(read_only=True)
    
#     class Meta:
#         model = Client
#         fields = ['id', 'client_name', 'created_at', 'updated_at', 'created_by']

# class ProjectSerializer(serializers.ModelSerializer):
#     client = serializers.PrimaryKeyRelatedField(queryset=Client.objects.all())
#     users = serializers.PrimaryKeyRelatedField(many=True, queryset=User.objects.all())
    
#     class Meta:
#         model = Project
#         fields = ['id', 'name', 'client', 'users', 'created_at', 'updated_at']

# class ClientDetailSerializer(ClientSerializer):
#     projects = ProjectSerializer(many=True, read_only=True)
    
#     class Meta(ClientSerializer.Meta):
#         fields = ClientSerializer.Meta.fields + ['projects']
# ```

# ## Views
# ```python
# from rest_framework import generics, status
# from rest_framework.response import Response
# from rest_framework.permissions import IsAuthenticated
# from .models import Client, Project
# from .serializers import ClientSerializer, ProjectSerializer, ClientDetailSerializer

# class ClientListCreateView(generics.ListCreateAPIView):
#     queryset = Client.objects.all()
#     serializer_class = ClientSerializer
#     permission_classes = [IsAuthenticated]

#     def perform_create(self, serializer):
#         serializer.save(created_by=self.request.user)

# class ClientRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Client.objects.all()
#     serializer_class = ClientDetailSerializer
#     permission_classes = [IsAuthenticated]

# class ProjectCreateView(generics.CreateAPIView):
#     serializer_class = ProjectSerializer
#     permission_classes = [IsAuthenticated]

#     def perform_create(self, serializer):
#         client_id = self.kwargs['client_id']
#         client = Client.objects.get(id=client_id)
#         serializer.save(client=client)

# class UserProjectsView(generics.ListAPIView):
#     serializer_class = ProjectSerializer
#     permission_classes = [IsAuthenticated]

#     def get_queryset(self):
#         return Project.objects.filter(users=self.request.user)
# ```

# ## URLs
# ```python
# from django.urls import path
# from .views import (
#     ClientListCreateView,
#     ClientRetrieveUpdateDestroyView,
#     ProjectCreateView,
#     UserProjectsView,
# )

# urlpatterns = [
#     path('clients/', ClientListCreateView.as_view(), name='client-list-create'),
#     path('clients/<int:pk>/', ClientRetrieveUpdateDestroyView.as_view(), name='client-detail'),
#     path('clients/<int:client_id>/projects/', ProjectCreateView.as_view(), name='project-create'),
#     path('projects/assigned/', UserProjectsView.as_view(), name='user-projects'),
# ]
# ```

# ## Testing with Django Admin and REST API
# 1. Use the Django admin panel to create users.
# 2. Access the REST API endpoints to manage clients and projects as required.

# ## Example GitHub/GitLab Repository
# Ensure to upload your code to a GitHub or GitLab repository and share the link.
