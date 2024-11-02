import os
from pathlib import Path

MESSAGE_STORAGE = 'django.contrib.messages.storage.session.SessionStorage'
SECRET_KEY = "DCFGV8794315ubhvh84CaviTFgyuvgh9846513cgh8465CFG"
BASE_DIR = Path(__file__).resolve().parent.parent
TEMPLATE_DIR= BASE_DIR/"templates"
STATIC_DIR = BASE_DIR/"static"
DEBUG = True
STATIC_URL = '/static/'
LOGIN_REDIRECT_URL = 'dashboard/'  

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'applications',  
]

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [TEMPLATE_DIR],  # Correct path for templates
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

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]
CSRF_TRUSTED_ORIGINS = ['http://localhost', 'http://127.0.0.1']

ROOT_URLCONF = 'application_portal.urls'
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
ALLOWED_HOSTS = ['127.0.0.1', 'localhost']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

