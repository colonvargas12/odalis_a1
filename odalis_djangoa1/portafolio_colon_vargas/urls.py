from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('mi_marca.urls')),
    path('principal/', include('principal.urls')),
]
