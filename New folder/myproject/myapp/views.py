from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from .models import Client, Project
from .serializers import ClientSerializer, ProjectSerializer, ClientDetailSerializer

from django.http import HttpResponse

def home(request):
    return HttpResponse("Welcome to the Home Page!")

class ClientListCreateView(generics.ListCreateAPIView):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user)

class ClientRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Client.objects.all()
    serializer_class = ClientDetailSerializer
    permission_classes = [IsAuthenticated]

class ProjectCreateView(generics.CreateAPIView):
    serializer_class = ProjectSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        client_id = self.kwargs['client_id']
        client = Client.objects.get(id=client_id)
        serializer.save(client=client)

class UserProjectsView(generics.ListAPIView):
    serializer_class = ProjectSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Project.objects.filter(users=self.request.user)