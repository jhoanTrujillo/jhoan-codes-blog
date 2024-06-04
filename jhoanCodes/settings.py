from pathlib import Path
import os

from dotenv import load_dotenv
import dj_database_url
import cloudinary

cloudinary.config(
    cloud_name=os.environ.get('CLOUD_NAME'),
    api_key=os.environ.get('CLOUDINARY_API_KEY'),
    api_secret=os.environ.get('CLOUDINARY_SECRET_KEY')
)

load_dotenv()

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent
TEMPLATES_DIR = os.path.join(BASE_DIR, 'templates')
# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.environ.get('SECRET_KEY')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ALLOWED_HOSTS = ['127.0.0.1', '.herokuapp.com', ]

# Application definition
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    # Cloudinary
    'cloudinary_storage',
    # Django allauth apps
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    'allauth.socialaccount.providers.google',
    'django.contrib.sites',
    'cloudinary',
    # Summernote app
    'django_summernote',
    # Crispy forms
    'crispy_forms',
    "crispy_bulma",
    'blog',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    # Add white noise middleware to app for static file deployment
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    # Allauth django app middleware
    "allauth.account.middleware.AccountMiddleware",
]

ROOT_URLCONF = 'jhoanCodes.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [TEMPLATES_DIR],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                # Needed for allauth functionalities
                'django.template.context_processors.request',
            ],
        },
    },
]

WSGI_APPLICATION = 'jhoanCodes.wsgi.application'

# Add local and heroku enviroment to trusted sources
# Allows blog post data to show in admin
CSRF_TRUSTED_ORIGINS = [
    "http://127.0.0.1:*",
    "https://*.herokuapp.com"
]

# Calls database url from env.py to keep it secret.
# uses the dj_database_url module to access a database
# From its URL
DATABASES = {
    'default': dj_database_url.parse(os.environ.get('DATABASE_URL'))
}


# Password validation
# https://docs.djangoproject.com/en/5.0/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME':
            'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME':
            'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME':
            'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME':
            'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

ACCOUNT_EMAIL_VERIFICATION = 'none'

# Internationalization
# https://docs.djangoproject.com/en/5.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.0/howto/static-files/

STATIC_URL = 'static/'
STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static')]
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')


# Default primary key field type
# https://docs.djangoproject.com/en/5.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# Authentication backend for allauth for latest version
AUTHENTICATION_BACKENDS = (
    "django.contrib.auth.backends.ModelBackend",
)

SITE_ID = 1
# Redirects for allauth login and logout actions
LOGIN_REDIRECT_URL = '/'
LOGOUT_REDIRECT_URL = '/'

# Crispy App for django packages for styling
CRISPY_ALLOWED_TEMPLATE_PACKS = "bulma"
CRISPY_TEMPLATE_PACK = "bulma"

CLOUD_NAME = os.environ.get('CLOUD_NAME'),
CLOUDINARY_API_KEY = os.environ.get('CLOUDINARY_API_KEY'),
CLOUDINARY_SECRET_KEY = os.environ.get('CLOUDINARY_SECRET_KEY')

CLOUDINARY_URL = (
    f"cloudinary://{CLOUDINARY_API_KEY}:{CLOUDINARY_SECRET_KEY}@{CLOUD_NAME}"
    )
