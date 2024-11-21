from django.contrib import admin
from django.urls import path, include
from myapp.views import home  # Import the home view

urlpatterns = [
    path('', home, name='home'),  # Add this line for the home page
    path('admin/', admin.site.urls),
    path('api/', include('myapp.urls')),  # Ensure this line is present
]