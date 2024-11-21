# settings.py

# Add necessary imports at the top (if not already present)
import os
from pathlib import Path
import os
from pathlib import Path

# Base directory
BASE_DIR = Path(__file__).resolve().parent.parent

REST_FRAMEWORK = {
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.IsAuthenticated',
    ]
}


# Static files settings
STATIC_URL = '/static/'
STATICFILES_DIRS = [
    BASE_DIR / "static",  # Directory where static files are stored
]

ALLOWED_HOSTS = ['*']
DEBUG = True

SECRET_KEY = 'your-secret-key-here'  # Replace with a unique key


# Application definition
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',  # Ensure this is included
    'myapp',           # Your app name
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'myproject.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'myproject.wsgi.application'



# Database settings (update with your actual database credentials)
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'myproject_db',  # Use the name you just created
        'USER': 'postgres',       # Your PostgreSQL username
        'PASSWORD': '1920',  # Your PostgreSQL password
        'HOST': 'localhost',
        'PORT': '',  # Leave blank for default port
    }
}
# Other settings...cls
