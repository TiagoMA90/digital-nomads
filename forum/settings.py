import os
import dj_database_url
from dotenv import load_dotenv
from pathlib import Path

# Load environment variables from .env file (for local development)
load_dotenv()

# Base directory of your project
BASE_DIR = Path(__file__).resolve().parent.parent
TEMPLATES_DIR = [
    os.path.join(BASE_DIR, 'templates'),
    os.path.join(BASE_DIR, 'users', 'templates'),
    os.path.join(BASE_DIR, 'blog', 'templates')
]

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.environ.get('SECRET_KEY')

# Set DEBUG to False for production
DEBUG = False

# Set allowed hosts for Heroku, localhost, and Gitpod
ALLOWED_HOSTS = ['digital-nomad.herokuapp.com', 'localhost', '127.0.0.1', '.gitpod.io', '8000-tiagoma90-digitalnomads-xktq52s41f9.ws-eu118.gitpod.io/']

# CSRF for Debug mode
CSRF_TRUSTED_ORIGINS = [
    "https://8000-tiagoma90-digitalnomads-xktq52s41f9.ws-eu118.gitpod.io",
    "https://*.gitpod.io"
]

# Application definition
INSTALLED_APPS = [
    'blog.apps.BlogConfig',
    'users.apps.UsersConfig',
    'crispy_forms',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'cloudinary_storage',
    'django.contrib.staticfiles',
    'cloudinary',
    'forum',
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

ROOT_URLCONF = 'forum.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': TEMPLATES_DIR,
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

WSGI_APPLICATION = 'forum.wsgi.application'

# Database configuration for Heroku (PostgreSQL)
DATABASE_URL = os.environ.get("DATABASE_URL")

# Ensure DATABASE_URL is a string and not bytes
if isinstance(DATABASE_URL, bytes):
    DATABASE_URL = DATABASE_URL.decode('utf-8')  # Decode it to a string

DATABASES = {
    'default': dj_database_url.parse(DATABASE_URL)
}

# Password validation settings
AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

# Static files (CSS, JavaScript, Images)
CRISPY_TEMPLATE_PACK = 'bootstrap4'

STATIC_URL = '/static/'
STATICFILES_STORAGE = 'cloudinary_storage.storage.StaticHashedCloudinaryStorage'
STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static')]
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

# Media storage (Cloudinary)
DEFAULT_FILE_STORAGE = 'cloudinary_storage.storage.MediaCloudinaryStorage'

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# Email settings for Gmail (using your email credentials)
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = os.environ.get('EMAIL_HOST_USER')
EMAIL_HOST_PASSWORD = os.environ.get('EMAIL_HOST_PASS')

# Redirect after login
LOGIN_REDIRECT_URL = 'blog-home'
