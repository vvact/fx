from .base import *

# SECURITY WARNING: don't run with debug turned on in production!

# Database
# https://docs.djangoproject.com/en/5.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}



# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.1/howto/static-files/

STATIC_URL = 'static/'  # URL to access static files

# Directory where additional static files are located during development
STATICFILES_DIRS = [
    BASE_DIR / "static"  # Ensure this directory exists
]

# Directory where static files will be collected for deployment
STATIC_ROOT = BASE_DIR / "staticfiles"  # Collectstatic command will gather files here

