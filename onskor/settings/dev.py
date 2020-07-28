from .base import *  # noqa

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = "0euto$n_o=3o4twnlp5@tdytiw+0$l4(tpwm4)+nqtmuh^7+pn"

# SECURITY WARNING: define the correct hosts in production!
ALLOWED_HOSTS = ["*"]

EMAIL_BACKEND = "django.core.mail.backends.console.EmailBackend"

INSTALLED_APPS = INSTALLED_APPS + ["debug_toolbar"]  # noqa

MIDDLEWARE = MIDDLEWARE + ["debug_toolbar.middleware.DebugToolbarMiddleware"]  # noqa

INTERNAL_IPS = ["127.0.0.1"]


try:
    from .local import *  # noqa
except ImportError:  # noqa
    pass
