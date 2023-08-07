import os
import yaml
from django.contrib.messages import constants as messages

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

credentials = yaml.safe_load(open(os.path.join(os.path.dirname(BASE_DIR), 'credentials.yaml')))

MESSAGE_TAGS = {
    messages.DEBUG: 'alert-info',
    messages.INFO: 'alert-info',
    messages.SUCCESS: 'alert-success',
    messages.WARNING: 'alert-warning',
    messages.ERROR: 'alert-danger',
}


SECRET_KEY = credentials['secret_key']

DEBUG = credentials['debug']

ALLOWED_HOSTS = credentials['allowed_hosts']

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    
    #Apps
    'frontend_cargo.apps.FrontendCargoConfig',
    'backend_cargo.apps.BackendCargoConfig',

    #3rd Party Apps
    'crispy_forms', 
    'django_extensions',
    'ckeditor',
    'ckeditor_uploader',

    #all_auth
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
 
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

ROOT_URLCONF = 'core.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, '../templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'backend_cargo.context_processors.get_siteoption',
            ],
        },
    },
]

WSGI_APPLICATION = 'core.wsgi.application'


# Database
# https://docs.djangoproject.com/en/2.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': credentials['db_engine'],
        'NAME': credentials['db_name'],
        'USER': credentials['db_username'],
        'PASSWORD': credentials['db_password'],
        'PORT': credentials['db_port'],
        'HOST': credentials['db_host'],
    }
}

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

ACCOUNT_FORMS = {
    'login': 'backend_cargo.forms.UserLoginForm',
    # 'signup': 'pages.forms.UserRegistrationForm',
    # 'change_password': 'pages.forms.PasswordChangeForm',
    # 'set_password': 'pages.forms.PasswordSetForm',
    # 'reset_password': 'pages.forms.PasswordResetForm',
    # 'reset_password_from_key': 'pages.forms.PasswordResetKeyForm'
}

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'Asia/Kathmandu'

USE_I18N = True

USE_L10N = True

USE_TZ = False

CRISPY_TEMPLATE_PACK = "bootstrap4"

VALID_IMAGE_FORMAT = ['jpg', 'png', 'jpeg', 'heic', 'gif']
STATIC_URL = '/django-static/'
STATICFILES_DIRS = (os.path.join(os.path.dirname(BASE_DIR), "static"), )
STATIC_ROOT = os.path.join(os.path.dirname(BASE_DIR), 'assets/')

MEDIA_ROOT = os.path.join(os.path.dirname(BASE_DIR), "media/")
MEDIA_URL = '/media/'

CKEDITOR_UPLOAD_PATH = 'ckeditoruploads/'

CKEDITOR_CONFIGS = {
    'default': {
        'toolbar': 'Custom',
    }
}
