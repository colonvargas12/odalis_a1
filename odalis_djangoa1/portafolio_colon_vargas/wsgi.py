import os
from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'portafolio_colon_vargas.settings')
application = get_wsgi_application()
